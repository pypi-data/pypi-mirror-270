from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from poetry.console.commands.build import BuildCommand
from poetry.console.commands.group_command import GroupCommand
from poetry.core.factory import Factory
from poetry.core.packages.dependency_group import MAIN_GROUP
from poetry.core.poetry import Poetry

if TYPE_CHECKING:
	from collections.abc import Mapping
	from typing import Any, Final

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
		toml_content: Mapping[str, Any] = self.poetry.pyproject.data
		self.poetry_local_conf: dict[str, Any] = self.poetry.local_config.copy()

		# From plugin's section
		self._groups2mix: Mapping[Group, list[Group]] | dict = toml_content.get(
			'tool', {},
		).get(self.plugin_section)

		del toml_content


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
		if group_name == 'poetry':  # or just "main"
			return poetry_main_deps
		return poetry_group.get(group_name, {}).get('dependencies', {})


	def mix_deps(
		self: JuiceCommand,
		poetry_group: Table,
		poetry_main_deps: Table,
		log_level: str = 'info',
	) -> None:
		self.line('Mixing juice..', log_level)
		for to_mix, groups in self._groups2mix.items():
			to_mix_deps = self._get_group_deps(to_mix, poetry_group, poetry_main_deps)
			for group_name in groups:
				group_deps = self._get_group_deps(group_name, poetry_group, poetry_main_deps)
				self.line(f'{group_name} -> {to_mix}', log_level)
				self.line(f'	{group_deps}', log_level)
				to_mix_deps.update(group_deps)


	def recreate_poetry(self: JuiceBuildCommand) -> None:
		factory: Factory = Factory()
		poetry_file = factory.locate(Path.cwd())  # NOTE: Better use as constant..
		local_config: Mapping[str, Any] = self.poetry_local_conf

		# Checking validity
		check_result = factory.validate(local_config)
		if check_result['errors']:
			message = ''
			for error in check_result['errors']:
				message += f'  - {error}\n'

			raise RuntimeError('The Poetry configuration is invalid:\n' + message)

		# Load package
		# If name or version were missing in package mode, we would have already
		# raised an error, so we can safely assume they might only be missing
		# in non-package mode and use some dummy values in this case.
		name: str = local_config.get('name', 'non-package-mode')
		assert isinstance(name, str)
		version: str = local_config.get('version', '0')
		assert isinstance(version, str)
		package = factory.get_package(name, version)
		package = factory.configure_package(
			package, local_config, poetry_file.parent, with_groups=True,
		)

		new_poetry: Poetry = Poetry(poetry_file, local_config, package)
		self.set_poetry(new_poetry)


	def handle(self: JuiceLookCommand) -> int:
		self.pre_handle()

		# TODO: Better type check..

		poetry_main_deps: dict = self.poetry_local_conf.get('dependencies', {})
		poetry_group: dict = self.poetry_local_conf.get('group', {})

		self.mix_deps(poetry_group, poetry_main_deps, 'info')

		# Recreate poetry because we don't want manually change every stuff that poetry already do
		self.recreate_poetry()

		return BuildCommand.handle(self)
