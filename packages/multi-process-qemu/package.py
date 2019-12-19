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
#     spack install multi-process-qemu
#
# You can edit this file again by typing:
#
#     spack edit multi-process-qemu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class MultiProcessQemu(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/oracle/qemu/archive/multi-process-qemu-v0.4.zip"
    git = "https://github.com/oracle/qemu.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.4', sha256='11ee38d9d6125db96d8b6ce459e014a278c6850703d172d99e33e156696f74a3')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
