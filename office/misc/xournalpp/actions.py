#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

w = "-Wno-unused-result -Wno-deprecated-declarations"

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")

	shelltools.export("CFLAGS", "-lpthread")
	pisitools.cxxflags.add(w)
	cmaketools.configure("-DCMAKE_BUILD_TYPE=Release", sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make("translations")

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
	shelltools.cd("..")

	pisitools.dodoc("AUTHORS", "CHANGELOG.md", "LICENSE", "README.md")
