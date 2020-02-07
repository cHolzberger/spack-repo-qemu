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
#     spack install ddrescue
#
# You can edit this file again by typing:
#
#     spack edit ddrescue
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ddrescue(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://ftp.fau.de/gnu/ddrescue/ddrescue-1.24.tar.lz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('1.24.tar.lz',  extension='tar.lz',   sha256='4b5d3feede70e3657ca6b3c7844f23131851cbb6af0cecc9721500f7d7021087')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
