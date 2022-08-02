#!/usr/bin/python
import os
HOME = os.path.expanduser('~')
with open('%s/.bashrc' % HOME, 'a') as b:
  b.write('\nalias apm="flatpak run com.github.vikdevelop.apm"')
with open('%s/.zshrc' % HOME, 'a') as z:
  z.write('\nalias apm="flatpak run com.github.vikdevelop.apm"')
