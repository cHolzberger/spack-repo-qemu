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
#     spack install virglrenderer
#
# You can edit this file again by typing:
#
#     spack edit virglrenderer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Virglrenderer(MesonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/virglrenderer-0.8.2/virglrenderer-virglrenderer-0.8.2.tar.bz2"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.8.2', sha256='fdeaeacea10d32bc22241bb197bc2743dffd0193497d78c5f322619ed2fb6e1f')
    version('0.8.1', sha256='849640686e00887d8bb575ff369832f5f8e5b2765552661aabd4f84a6f4d8329')
    version('0.8.0', sha256='a310139ead53ba0b5bdd713b523bd8668e8963af3eb87e075e73a672a4d7e900')
    version('0.7.0', sha256='c59f1b3205b9d4f8d8f5c98efdb8b2fabb08b5f82152896a83ec5cf8113c1dd9')
    version('0.6.0', sha256='ed9ba60820e8393c671ff4476f6c176466b84a18576750b064f3379fa0796e08')
    version('0.5.0', sha256='2b9d399c3adc1e684699a1fac9d954923bb20c5058a2324b570e5356de18ec6e')
    version('0.4.0', sha256='db376b5a776960b65dd21cf7e8458626c581d55464b6e202dfc1ead02725a7c3')
    version('0.2.0', sha256='f712a2f58924f5062efbdcc3dabd359236936a72ca1274f1a2ea38d2ce027991')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    # FIXME: Add additional dependencies if required.
    # depends_on('foo')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
