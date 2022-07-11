# apm
Simple installation and uninstallation AppImages on Linux.

With this program, you no longer have to go to a website and manually download AppImage. Just type `apm -install appname (e.g. appimagelauncher)`, and this program will also make it easy to uninstall, run and find new AppImage.
## Usage
```bash
usage: apm [-h] [-install INSTALL] [-remove REMOVE] [-seeall] [-search SEARCH] [-run RUN]

options:
  -h, --help        show this help message and exit
  -install INSTALL  Install AppImages
  -remove REMOVE    Uninstall AppImages
  -seeall           See all installed AppImages
  -search SEARCH    Search AppImage in repository
  -run RUN          Run installed AppImage
```
## Add new AppImages
AppImages is located in the `appimages.json` file.
To add an AppImage, type the following into the file:
```json
  "appname": "url-to-download-appimg",
```
## Build
### dependencies
- org.freedesktop.Sdk - v21.08
- org.freedesktop.Platform - v21.08

For build this app, use `flatpak-builder`:
```
flatpak-builder build flatpak.yml --install --user
```
