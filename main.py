import json
import os
import argparse

apmcli = argparse.ArgumentParser()
apmcli.add_argument("-install", help="Install AppImages", type=str)
apmcli.add_argument("-remove", help="Uninstall AppImages", type=str)
apmcli.add_argument("-seeall", help="See all installed AppImages", action="store_true")

args = apmcli.parse_args()
HOME = os.path.expanduser('~')
with open("appimages.json") as jsondata:
    jsonObject = json.load(jsondata)

if args.install in jsonObject:
    '\033[1m' + 'Installaion AppImage' + '\033[0m'
    print("Searching AppImage: " + args.install + " ... done.")
    print("Name:        Source:\n")
    print(args.install + "      %s" % jsonObject[args.install])
    dialog = input("Would you like to continue? [Y/n]: ")
    if dialog == 'n':
        print("Canceled.")
        exit()
    if dialog == 'y' or 'Y':
        print('\033[1m' + 'Downloading sources' + '\033[0m')
        os.system("wget -c %s" % jsonObject[args.install])
        if not os.path.exists("%s/.AppImage" % HOME):
            os.mkdir("%s/.AppImage" % HOME)
        print('\033[1m' + 'Installing ' + args.install + ' to $HOME/.AppImage' + '\033[0m')
        os.system("mv *.AppImage $HOME/.AppImage/" + args.install + ".AppImage")
        os.system("chmod +x $HOME/.AppImage/" + args.install + ".AppImage")
        print('\033[1m' + 'Creating and moving ' + args.install + '.desktop to $HOME/.local/share/applications/' + '\033[0m')
        with open('%s/.local/share/applications/' % HOME + args.install + '.desktop', 'w') as f:
            f.write("[Desktop Entry]\n")
            f.write("Name=" + args.install + "\n")
            f.write("Type=Application\n")
            f.write("Exec=$HOME/.AppImage/" + args.install + ".AppImage\n")
            f.write("Icon=AppImage\n")
            f.write("Categories=Tools\n")
            f.write("Comment=This is Appimage of" + args.install)
        print('\033[1m' + 'Done!' + '\033[0m')

if args.remove in jsonObject:
    print('\033[1m' + 'Uninstallation AppImage' + '\033[0m')
    print("Name:        Path:\n")
    print(args.remove + "       $HOME/.AppImage/" + args.remove + ".AppImage")
    rm = input("Would you like to continue? [Y/n]: ")
    if rm == 'n':
        print("Canceled.")
        exit()
    if rm == 'Y' or 'y':
        print('\033[1m' + 'Removing ' + args.remove + ' from $HOME/.AppImage directory' + '\033[0m')
        os.remove(os.path.expanduser('~/.AppImage/') + args.remove + ".AppImage")
        print('\033[1m' + 'Removing ' + args.remove + '.desktop from $HOME/.local/share/applications/ directory' + '\033[0m')
        os.remove('%s/.local/share/applications/' % HOME + args.remove + '.desktop')
        print('\033[1m' + 'Done!' + '\033[0m')

if args.seeall:
    print("This is all AppImages installed on your computer:")
    os.system("ls $HOME/.AppImage")
