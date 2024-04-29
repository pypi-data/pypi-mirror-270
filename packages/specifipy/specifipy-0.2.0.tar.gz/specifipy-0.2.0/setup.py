# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['specifipy',
 'specifipy.file_scanners',
 'specifipy.parsers',
 'specifipy.parsers.structure']

package_data = \
{'': ['*'], 'specifipy': ['resources/icons/*']}

install_requires = \
['docstring-parser>=0.15,<0.16', 'py-d2==1.0.0', 'snakemd>=0.11.0,<0.12.0']

setup_kwargs = {
    'name': 'specifipy',
    'version': '0.2.0',
    'description': 'Python package for auto-generating code diagrams',
    'long_description': 'None',
    'author': 'Bartosz Budzyński',
    'author_email': 'hi@bartosz.blog',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
