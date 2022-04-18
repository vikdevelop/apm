# apm
Simple installation and uninstallation AppImages on Linux.

With this program, you no longer have to go to a website and manually download AppImage. Just type apm install appname, and this program will also make it easy to uninstall and find new AppImage.
## Usage
```bash
usage: main.py [-h] [-install INSTALL] [-remove REMOVE] [-seeall] [-search SEARCH]

optional arguments:
  -h, --help        show this help message and exit
  -install INSTALL  Install AppImages
  -remove REMOVE    Uninstall AppImages
  -seeall           See all installed AppImages
  -search SEARCH    Search AppImages
```
## Add new packages
AppImages is located in the appimages.json file.
To add an AppImage, type the following into the file:
```json
  "appname": "url-to-download-appimg",
```
