from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.console.commands.build import BuildCommand
from poetry.console.commands.group_command import GroupCommand
from poetry.core.packages.dependency_group import MAIN_GROUP

if TYPE_CHECKING:
	from typing import Any, Final, Mapping

	from poetry.poetry import Poetry
	from tomlkit.items import Table

	from poetry_plugin_deps_juice.plugins import Group



class JuiceCommand(GroupCommand):

	name: str
	description: str

	plugin_section: Final[str] = 'poetry-plugin-deps-juice'

	poetry: Poetry


	@property
	def default_groups(self: JuiceCommand) -> set[str]:
		return {MAIN_GROUP}


	def pre_handle(self: JuiceCommand):
		# print(self.poetry.local_config['group'])
		# print(self.poetry.local_config['dependencies'])
		# exit()
		self.toml_content: Mapping[str, Any] = self.poetry.pyproject.data
		self.poetry_local_conf: Mapping[str, Any] = self.poetry.local_config

		self._groups2mix: Mapping[Group, list[Group]] | dict = self.toml_content.get(
			'tool', {},
		).get(self.plugin_section)


# TODO: Add, remove, update groups

class JuiceLookCommand(JuiceCommand):

	name = 'juice-look'
	description = 'List of groups to mix from toml.'


	def handle(self: JuiceLookCommand) -> int:
		self.pre_handle()

		for to_mix, groups in self._groups2mix.items():
			self.line(f'"{to_mix}" <-', 'info')
			for group in groups:
				self.line(f'	"{group}"', 'info')

		return 0


class JuiceBuildCommand(JuiceCommand, BuildCommand):

	name: str = 'jbuild'
	description: str = "Wrapper around poetry's build command."


	def _get_group_deps(
		self: JuiceBuildCommand,
		group_name: str,
		poetry_group: Table,
		poetry_main_deps: Table,
	) -> Table | dict:
		if group_name == 'poetry':
			return poetry_main_deps
		return poetry_group.get(group_name, {}).get('dependencies', {})


	def handle(self: JuiceLookCommand) -> int:
		self.pre_handle()

		# TODO: Better type check..
		# poetry: Mapping[str, Any] = self.toml_content.get('tool', {}).get('poetry', {})
		# poetry_main_deps: Table = poetry.get('dependencies', {})
		# poetry_group: Table = poetry.get('group', {})

		poetry_main_deps: Table = self.poetry_local_conf.get('dependencies', {})
		poetry_group: Table = self.poetry_local_conf.get('group', {})

		self.line('Mixing juice..', 'info')
		for to_mix, groups in self._groups2mix.items():
			to_mix_deps = self._get_group_deps(to_mix, poetry_group, poetry_main_deps)
			for group_name in groups:
				group_deps = self._get_group_deps(group_name, poetry_group, poetry_main_deps)
				self.line(f'{group_name} -> {to_mix}', 'info')
				self.line(f'	{group_deps}', 'info')
				to_mix_deps.update(group_deps)

		# print(poetry_main_deps)

		return BuildCommand.handle(self)
