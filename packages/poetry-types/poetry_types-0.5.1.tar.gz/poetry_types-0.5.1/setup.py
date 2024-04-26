# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_types', 'poetry_types.commands']

package_data = \
{'': ['*']}

install_requires = \
['packaging<25.0', 'poetry>=1.6,<2.0', 'tomlkit<1.0']

entry_points = \
{'poetry.application.plugin': ['poetry-types = '
                               'poetry_types.poetry_types:PoetryTypes']}

setup_kwargs = {
    'name': 'poetry-types',
    'version': '0.5.1',
    'description': 'A poetry plugin that adds/removes type stubs as dependencies like the mypy --install-types command.',
    'long_description': '# poetry-types\n\n[![PyPI version](https://badge.fury.io/py/poetry-types.svg)](https://badge.fury.io/py/poetry-types)\n[![GitHub license](https://img.shields.io/github/license/jvllmr/poetry-types)](https://github.com/jvllmr/poetry-types/blob/master/LICENSE)\n[![GitHub issues](https://img.shields.io/github/issues/jvllmr/poetry-types)](https://github.com/jvllmr/poetry-types/issues)\n![PyPI - Downloads](https://img.shields.io/pypi/dd/poetry-types)\n![Tests](https://github.com/jvllmr/poetry-types/actions/workflows/main.yml/badge.svg)\n\n## Description\n\nThis is a plugin to poetry for the upcoming poetry 1.2 plugin feature.\nIt installs/removes/updates typing stubs via following commands:\n\n- `poetry types add <package names>`\n- `poetry types remove <package names>`\n- `poetry types update <package names>`\n\n## Usage examples\n\n- `poetry types add openpyxl` adds `openpyxl` to your project\n- `poetry types update` adds `types-openpyxl` if `openpyxl` is present, but `types-openpyxl` is not\n- `poetry types update` removes `types-openpyxl` if `types-openpyxl` is present, but `openpyxl` is not\n\n## Installation\n\nRun `poetry self add poetry-types` for global install or run `poetry add -D poetry-types` to use this plugin with your project.\n\n## Usage with pre-commit\n\n```yaml\n- repo: https://github.com/jvllmr/poetry-types\n  rev: v0.5.1\n  hooks:\n    - id: poetry-types\n```\n\n### poetry-types has to be skipped with pre-commit.ci\n\n```yaml\nci:\n  skip: [poetry-types]\n```\n',
    'author': 'Jan Vollmer',
    'author_email': 'jan@vllmr.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jvllmr/poetry-types',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
