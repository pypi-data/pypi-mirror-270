# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eink_calendar', 'eink_calendar.api', 'eink_calendar.ui']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.100.0,<3.0.0',
 'google-auth-httplib2>=0.1.1,<0.2.0',
 'google-auth-oauthlib>=1.1.0,<2.0.0',
 'inky[example-depends,rpi]>=1.5.0,<2.0.0',
 'pillow>=10.0.1,<11.0.0',
 'pysdl2>=0.9.16,<0.10.0',
 'pyxdg>=0.28,<0.29']

entry_points = \
{'console_scripts': ['eink_calendar = eink_calendar.__main__:main']}

setup_kwargs = {
    'name': 'eink-calendar',
    'version': '0.1.0',
    'description': '',
    'long_description': '# eInk Calendar\n\nDisplays Google Calendar events on an Inky Impression display.\n\n![Example showing how the UI looks](https://i.imgur.com/cKqnSmU.png)\n',
    'author': 'Tyler Compton',
    'author_email': 'xaviosx@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
