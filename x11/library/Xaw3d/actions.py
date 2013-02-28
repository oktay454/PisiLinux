#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libXaw3d-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --enable-arrow-scrollbars \
                         --enable-gray-stipples \
                         --enable-multiplane-bitmaps")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dodoc("ChangeLog","COPYING","README","src/README.XAW3D")
