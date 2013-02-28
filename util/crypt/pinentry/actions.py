#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-rpath \
                         --disable-pinentry-gtk \
                         --enable-pinentry-curses \
                         --infodir=/usr/share/info")

def build():
    autotools.make()

def install():
    autotools.install()

    # We're using pinentry-wrapper as additional file instead of upstream pinentry symlink.
    pisitools.remove("/usr/bin/pinentry")

    pisitools.dosym("pinentry-gtk-2", "/usr/bin/pinentry-gtk")
    pisitools.dosym("pinentry-qt4", "/usr/bin/pinentry-qt")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
