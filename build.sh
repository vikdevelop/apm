 #!/usr/bin/sh
git clone https://github.com/vikdevelop/apm ~/.cache/apm > /dev/null 2>&1
cd ~/.cache/apm
echo "Installing depency runtime and SDK"
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install runtime/org.freedesktop.Platform/x86_64/21.08 runtime/org.freedesktop.Sdk/x86_64/21.08 org.flatpak.Builder -y > /dev/null 2>&1
echo "Building apm with flatpak builder"
flatpak run org.flatpak.Builder build flatpak.yml --install --user > /dev/null 2>&1
python3 flatpak.py
echo "Done! Try run APM with command: 'apm --help' or 'flatpak run com.github.vikdevelop.apm --help'"
