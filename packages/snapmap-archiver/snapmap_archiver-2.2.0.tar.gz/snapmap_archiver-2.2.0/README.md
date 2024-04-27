# snapmap-archiver

A tool written in Python **3.10** to download all Snapmaps content from a specific location.

## Install Python 3.10+

Be sure to check that you're using a version of Python that is 3.10 or above. **This project will not work on Python 3.9 or below!**

![snapmap-archiver splash](/.github/img/Splash.png)

`pip install snapmap-archiver`

[View on PyPI](https://pypi.org/project/snapmap-archiver/)

## Setup (for working in a Python environment)

Install dependencies with `pip`.

```sh
pip install -r requirements.txt
```

## Usage

```sh
snapmap-archiver -o [OUTPUT DIR] -l="[LATITUDE],[LONGITUDE]"
```

Unfortunately you have to use the arbitrary `-l="lat,lon"` rather than just `-l "lat,lon"` when parsing negative numbers as `argsparse` interprets said numbers as extra arguments.

### Optional Arguments

#### Location

`-l` is not required if an input file or Snap URL is provided. It can also be used multiple times to download Snaps from multiple locations in one command.

E.g

```sh
snapmap-archiver -o ~/Desktop/snap -l='123.123,123.123' -l '445.445,445.445'
```

#### Input File

With `-f` or `--file`, you can specify a file containing a list of line-separated Snap URLs or IDs.

E.g

```sh
snapmap-archiver -o ~/Desktop/snaps -f ~/Desktop/snaps.txt
```

Inside `snaps.txt`:

```
https://map.snapchat.com/ttp/snap/Example/@-33.643495,115.741281,11.86z
Example
https://map.snapchat.com/ttp/snap/Example/
https://map.snapchat.com/ttp/snap/Example/
```

#### Snap URL

You can also just pass 1 or more normal Snap URLs or IDs to the package to download it individually like this:

```sh
snapmap-archiver -o ~/Desktop/snap 'https://map.snapchat.com/ttp/snap/Example/@-33.643495,115.741281,11.86z' 'Example'
```

#### Export JSON

You can export a JSON file with info about downloaded snaps with the `--write-json` argument, which will contain information like the time the Snap was posted, and the Snap location.

It will write `archive.json` to the specified output directory.

#### Snap Radius

The radius from the coordinates you provide that will be included for downloads. `-r 20000` will download all Snaps within a 20km radius of your coordinates.
