#!/usr/bin/sh
git clone https://github.com/vikdevelop/apm /tmp/apm > /dev/null 2>&1
cd /tmp/apm
echo "Installing depency runtime and SDK"
flatpak install runtime/org.freedesktop.Platform/x86_64/21.08 runtime/org.freedesktop.Sdk/x86_64/21.08 -y > /dev/null 2>&1
echo "Building apm"
flatpak-builder build flatpak.yml --install --user > /dev/null 2>&1
python3 flatpak.py
echo "Done! Try run APM with command: 'apm --help' or 'flatpak run com.github.vikdevelop.apm --help'"
