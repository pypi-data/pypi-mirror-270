# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snapmap_archiver']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=23.2.1,<24.0.0',
 'alive-progress>=3.1.5,<4.0.0',
 'httpx>=0.27.0,<0.28.0',
 'loguru>=0.7.2,<0.8.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['snapmap-archiver = snapmap_archiver.__main__:main']}

setup_kwargs = {
    'name': 'snapmap-archiver',
    'version': '2.3.0',
    'description': 'Download all Snap Map content from a specific location.',
    'long_description': '# snapmap-archiver\n\nDownload all Snap Map content from a specific location.\n\n![snapmap-archiver splash](/.github/img/Splash.png)\n\n[View on PyPI](https://pypi.org/project/snapmap-archiver/)\n\n## Installation (for general usage)\n\nInstall with `pip` or `pipx` or whatever trendy Python package manager you use:\n\n```sh\npip install snapmap-archiver\n```\n\n## Local Development Setup\n\nInstall Poetry with `pip` or `pipx`:\n\n```sh\npip install poetry\n```\n\nInstall the project dependencies:\n\n```sh\npoetry install\n```\n\nRun the app with Poetry:\n\n```sh\npoetry run python3 main.py [...args]\n```\n\n## Usage\n\n```sh\nsnapmap-archiver -o [OUTPUT DIR] -l="[LATITUDE],[LONGITUDE]"\n```\n\nUnfortunately you have to use the arbitrary `-l="lat,lon"` (with the equals sign) rather than just `-l "lat,lon"` when parsing negative numbers as `argsparse` interprets said numbers as extra arguments.\n\n### Optional Arguments\n\n#### Location\n\n`-l` is not required if an input file or Snap URL is provided. It can also be used multiple times to download Snaps from multiple locations in one command.\n\nE.g\n\n```sh\nsnapmap-archiver -o ~/Desktop/snap -l=\'123.123,123.123\' -l \'445.445,445.445\'\n```\n\n#### Input File\n\nWith `-f` or `--file`, you can specify a file containing a list of line-separated Snap URLs or IDs.\n\nE.g\n\n```sh\nsnapmap-archiver -o ~/Desktop/snaps -f ~/Desktop/snaps.txt\n```\n\nInside `snaps.txt`:\n\n```\nhttps://map.snapchat.com/ttp/snap/Example/@-33.643495,115.741281,11.86z\nExample\nhttps://map.snapchat.com/ttp/snap/Example/\nhttps://map.snapchat.com/ttp/snap/Example/\n```\n\n#### Snap URL\n\nYou can also just pass 1 or more normal Snap URLs or IDs to the package to download it individually like this:\n\n```sh\nsnapmap-archiver -o ~/Desktop/snap \'https://map.snapchat.com/ttp/snap/Example/@-33.643495,115.741281,11.86z\' \'Example\'\n```\n\n#### Time Filter\n\nUse the `-t` flag with a Unix timestamp or day, hour, or minute interval to skip the download of any snaps older than that point.\n\nExample with a Unix timestamp:\n\n```sh\nsnapmap-archiver -t 1714392291 -l \'-123,123\'\n```\n\nExamples with a dynamic time filter:\n\n```sh\nsnapmap-archiver -t 3d -l=\'-123,123\'  # Removes anything older than 3 days\nsnapmap-archiver -t 5h -l=\'-123,123\'  # Removes anything older than 5 hours\nsnapmap-archiver -t 30m -l=\'-123,123\'  # Removes anything older than 30 minutes\n```\n\n#### Export JSON\n\nYou can export a JSON file with info about downloaded snaps with the `--write-json` argument, which will contain information like the time the Snap was posted, and the Snap location.\n\nIt will write `archive.json` to the specified output directory.\n\n#### Snap Radius\n\nThe radius from the coordinates you provide that will be included for downloads. `-r 20000` will download all Snaps within a 20km radius of your coordinates.\n\n#### Zoom Depth\n\nYou can input a custom zoom depth value (`-z`) that correlates to a zoom level in the GUI. ArcGIS has documentation about this [here](https://developers.arcgis.com/documentation/glossary/zoom-level/), but essentially the lower the number, the further zoomed-out you are. `5` is the default and shouldn\'t cause any issues.\n\n#### Debug Mode\n\nEnable debug logs with `-d`/`--debug`.\n',
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
