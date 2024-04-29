## Poetry Dependency Juice Plugin

This plugin simplifies the process of managing dependencies in your Poetry projects by allowing you to mix dependencies from specified groups and wrap the `poetry build` command into `poetry jbuild`.
It provides an easy way to create custom mixes of dependencies and execute the build command with those mixes.

See difference:

#### Poetry build:
```bash
poetry build && pkginfo -f requires_dist dist/*.whl
```

#### output:
```plaintext
Building poetry-plugin-deps-juice (0.0.2)
  - Building sdist
  - Built poetry_plugin_deps_juice-0.0.2.tar.gz
  - Building wheel
  - Built poetry_plugin_deps_juice-0.0.2-py3-none-any.whl
requires_dist: ['poetry (>=1.8.0,<2.0.0)']
```

#### Juice build:
```bash
poetry jbuild && pkginfo -f requires_dist dist/*.whl
```

#### output:
```plaintext
Mixing juice..
base -> poetry
        {'poetry-core': '^1.7.0', 'wheel': '^0.42.0'}
setup -> poetry
        {'build': '^1.0.3', 'setuptools': '^69.0.3'}
Building poetry-plugin-deps-juice (0.0.2)
  - Building sdist
  - Built poetry_plugin_deps_juice-0.0.2.tar.gz
  - Building wheel
  - Built poetry_plugin_deps_juice-0.0.2-py3-none-any.whl
requires_dist: ['build (>=1.0.3,<2.0.0)', 'poetry (>=1.8.0,<2.0.0)', 'poetry-core (>=1.7.0,<2.0.0)', 'setuptools (>=69.0.3,<70.0.0)', 'wheel (>=0.42.0,<0.43.0)']
```

### Usage

1. **Installation**:

   Install the plugin using Poetry:

   ```bash
   pip install poetry-plugin-deps-juice
   ```

   or

   ```bash
   pip install --user poetry-plugin-deps-juice
   ```

   or at least

   ```bash
   poetry self add poetry-plugin-deps-juice
   ```

2. **Define Dependency Mix**:

   Add your dependency mix to the `pyproject.toml` file under the `[tool.poetry-plugin-deps-juice]` section:

   ```toml
   [tool.poetry-plugin-deps-juice]
   "fancy" = [
        "base",
        "setup",
   ]
   ```

   Here, `poetry` is the custom mix name, and `base` and `setup` are the groups of dependencies to be mixed.

   To mix into default group `[tool.poetry.dependencies]` use:

   ```toml
   [tool.poetry-plugin-deps-juice]
   "poetry" = [
        "base",
        "setup",
   ]
   ```

3. **Execute Juice Command**:

   Now you can use the defined mix with Poetry:

   ```bash
   poetry jbuild
   ```

   This command will mix dependencies from the specified groups and execute the `poetry build` command.

   This is easier than manually merging all dependencies into one group or adding them manually to the `[tool.poetry.dependencies]` option. When installing the built package using pip, only dependencies listed in the `[tool.poetry.dependencies]` option are installed (in current time). This plugin simplifies the process by allowing you to create mixes on-the-fly for the final package.

4. **List Available Dependency Mixes**:

   To get a list of available mixes along with their corresponding groups, run:

   ```bash
   poetry juice-list
   ```

   This will display a list of mixes and their associated groups:

   ```plaintext
   "poetry" <-
           "base"
           "setup"
   ```

### Contributing

Feel free to contribute to this plugin by reporting issues, suggesting features, or submitting pull requests on [GitHub](https://github.com/BlackCatDevel0per/poetry-plugin-deps-juice).

### License

This plugin is licensed under the Apache 2. License. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.
