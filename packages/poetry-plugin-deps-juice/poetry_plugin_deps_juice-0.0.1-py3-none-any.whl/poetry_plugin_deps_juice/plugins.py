from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_deps_juice.command import JuiceBuildCommand, JuiceLookCommand

if TYPE_CHECKING:
	from poetry.console.application import Application
	from poetry.console.commands.command import Command
	from poetry.poetry import Poetry

	Group = str


class DependenciesJuiceApplicationPlugin(ApplicationPlugin):
	"""Main class of the plugin."""

	@property
	def commands(self: DependenciesJuiceApplicationPlugin) -> list[type[Command]]:
		"""Property with plugin commands."""
		return [
			JuiceLookCommand,
			JuiceBuildCommand,
		]


	def activate(self: DependenciesJuiceApplicationPlugin, application: Application) -> None:
		"""Add poetry app on plugin activation."""
		self.poetry: Poetry = application.poetry

		super().activate(application=application)
