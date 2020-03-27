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
#     spack install tgt
#
# You can edit this file again by typing:
#
#     spack edit tgt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Tgt(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/fujita/tgt/archive/v1.0.79/tgt-1.0.79.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.0.79', sha256='6736d799a202ff665549359859441c6d2b5e3425bffef9ee60ab5a101342a40d')
    def patch(self):
        filter_file("-Werror","","usr/Makefile")
    def build(self, spec, prefix):
        q = ['PREFIX={0}'.format(prefix)]
        make(*q)
    def install(self, spec, prefix):
        q = ['PREFIX={0}'.format(prefix)]
        make("install", *q)
 
    # FIXME: Add dependencies if required.
    # depends_on('foo')
#    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter('Makefile')
        # makefile.filter('CC = .*', 'CC = cc')
