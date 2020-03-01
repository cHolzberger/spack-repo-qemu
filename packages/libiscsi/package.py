# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install libiscsi
#
# You can edit this file again by typing:
#
#     spack edit libiscsi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Libiscsi(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/sahlberg/libiscsi/archive/1.19.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.19.0', sha256='c7848ac722c8361d5064654bc6e926c2be61ef11dd3875020a63931836d806df')
    version('1.18.0', sha256='464d104e12533dc11f0dd7662cbc2f01c132f94aa4f5bd519e3413ef485830e8')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('glib')
    depends_on('libgcrypt')
    depends_on('popt')

    def autoreconf(self, spec, prefix):
       autoreconf('--force', '--install')

    def configure_args(self):
       args=['--disable-werror', 'CFLAGS=-O2', 'CXXFLAGS=-O2'] 
       return args
