# apm
Simple installation and uninstallation AppImages on Linux.

With this program, you no longer have to go to a website and manually download AppImage. Just type `apm -install appname (e.g. appimagelauncher)`, and this program will also make it easy to uninstall, update and find new AppImage.
## Usage
```bash
usage: apm [-h] [-install INSTALL] [-remove REMOVE] [--installed]
           [-search SEARCH] [-update] [--update-with-name UPDATE_WITH_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -install INSTALL      Install AppImages
  -remove REMOVE        Uninstall AppImages
  --installed           See all installed AppImages
  -search SEARCH        Search AppImages in repository
  -update               Update installed AppImage
  --update-with-name UPDATE_WITH_NAME
                        Update AppImage manually
```
## Add new AppImages
AppImages is located in `appimages.json` file.
To add an AppImage, type following into file:
```json
  "appname": "url-to-download-appimg",
```
## Build
For build this app, you can use this simple command:
```bash
wget -qO /tmp/build.sh https://raw.githubusercontent.com/vikdevelop/apm/main/build.sh && sh /tmp/build.sh
```
