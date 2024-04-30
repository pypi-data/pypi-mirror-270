# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docketalarm_api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'docketalarm-api',
    'version': '1.0.0',
    'description': 'Wrapper to interact with DocketAlarm API',
    'long_description': None,
    'author': 'Ezequiel Ghiena',
    'author_email': 'ezequiel.ghiena@vlex.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
