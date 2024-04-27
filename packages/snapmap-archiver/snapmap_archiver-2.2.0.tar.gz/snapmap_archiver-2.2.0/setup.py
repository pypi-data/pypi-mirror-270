# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snapmap_archiver']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['snapmap-archiver = snapmap_archiver:main']}

setup_kwargs = {
    'name': 'snapmap-archiver',
    'version': '2.2.0',
    'description': 'Download all Snap Map content from a specific location.',
    'long_description': '# snapmap-archiver\n\nA tool written in Python **3.10** to download all Snapmaps content from a specific location.\n\n## Install Python 3.10+\n\nBe sure to check that you\'re using a version of Python that is 3.10 or above. **This project will not work on Python 3.9 or below!**\n\n![snapmap-archiver splash](/.github/img/Splash.png)\n\n`pip install snapmap-archiver`\n\n[View on PyPI](https://pypi.org/project/snapmap-archiver/)\n\n## Setup (for working in a Python environment)\n\nInstall dependencies with `pip`.\n\n```sh\npip install -r requirements.txt\n```\n\n## Usage\n\n```sh\nsnapmap-archiver -o [OUTPUT DIR] -l="[LATITUDE],[LONGITUDE]"\n```\n\nUnfortunately you have to use the arbitrary `-l="lat,lon"` rather than just `-l "lat,lon"` when parsing negative numbers as `argsparse` interprets said numbers as extra arguments.\n\n### Optional Arguments\n\n#### Location\n\n`-l` is not required if an input file or Snap URL is provided. It can also be used multiple times to download Snaps from multiple locations in one command.\n\nE.g\n\n```sh\nsnapmap-archiver -o ~/Desktop/snap -l=\'123.123,123.123\' -l \'445.445,445.445\'\n```\n\n#### Input File\n\nWith `-f` or `--file`, you can specify a file containing a list of line-separated Snap URLs or IDs.\n\nE.g\n\n```sh\nsnapmap-archiver -o ~/Desktop/snaps -f ~/Desktop/snaps.txt\n```\n\nInside `snaps.txt`:\n\n```\nhttps://map.snapchat.com/ttp/snap/Example/@-33.643495,115.741281,11.86z\nExample\nhttps://map.snapchat.com/ttp/snap/Example/\nhttps://map.snapchat.com/ttp/snap/Example/\n```\n\n#### Snap URL\n\nYou can also just pass 1 or more normal Snap URLs or IDs to the package to download it individually like this:\n\n```sh\nsnapmap-archiver -o ~/Desktop/snap \'https://map.snapchat.com/ttp/snap/Example/@-33.643495,115.741281,11.86z\' \'Example\'\n```\n\n#### Export JSON\n\nYou can export a JSON file with info about downloaded snaps with the `--write-json` argument, which will contain information like the time the Snap was posted, and the Snap location.\n\nIt will write `archive.json` to the specified output directory.\n\n#### Snap Radius\n\nThe radius from the coordinates you provide that will be included for downloads. `-r 20000` will download all Snaps within a 20km radius of your coordinates.\n',
    'author': 'Miles Greenwark',
    'author_email': 'Millez.Dev@gmail.com',
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
