# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install libhugetlbfs
#
# You can edit this file again by typing:
#
#     spack edit libhugetlbfs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Libhugetlbfs(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/libhugetlbfs/libhugetlbfs/releases/download/2.22/libhugetlbfs-2.22.tar.gz"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.22', sha256='94dca9ea2c527cd77bf28904094fe4708865a85122d416bfccc8f4b73b9a6785')
    def build(self, spec, prefix):
        mkdirp( os.path.join (prefix, "lib"))
        q = ['PREFIX={0}'.format(prefix), 'LIB64=lib', 'LIB32=','BUILDTYPE=NATIVEONLY']
        cc = ['CCFLAGS=', 'CXXFLAGS=']

        make (*q, *cc)
    def install(self,spec,prefix):
        q = ['PREFIX={0}'.format(prefix), 'LIB64=lib', 'LIB32=','BUILDTYPE=NATIVEONLY']
        cc = ['CCFLAGS=', 'CXXFLAGS=']

        make ('install', *q, *cc)

#    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter('Makefile')
        # makefile.filter('CC = .*', 'CC = cc')
