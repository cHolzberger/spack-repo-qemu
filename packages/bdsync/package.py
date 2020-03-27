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
#     spack install bdsync
#
# You can edit this file again by typing:
#
#     spack edit bdsync
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bdsync(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/TargetHolding/bdsync/archive/v0.10.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.11.1', sha256='ee24781c9b063bd9da2c10a82b8c75dee1a813d0472d2dcce2b783a7dd9b55c7')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('openssl')
#    depends_on('pandoc',type=('build'))
    def build(self, spec,prefix):
        make("bdsync")
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('bdsync', prefix.bin)
