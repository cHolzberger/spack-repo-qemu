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
#     spack install qemu
#
# You can edit this file again by typing:
#
#     spack edit qemu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Qemu(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://download.qemu.org/qemu-4.1.1.tar.xz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.2.0-rc4', sha256='d93edb940370f4255488f8ad8f5afc1e3b8189ea20136aaef8056b155b9dc765')
    version('4.1.1', sha256='ed6fdbbdd272611446ff8036991e9b9f04a2ab2e3ffa9e79f3bab0eb9a95a1d2')

    patch('https://github.com/saveriomiroddi/qemu-pinning/commit/master.patch', sha256='686547aff57011e7e7c9b4dbdd85811704441e2319687d1a120e0e0aafd7bf07', when="@4.1.1:")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [
                "--extra-cflags=-DNCURSES_WIDECHAR=1 -fno-semantic-interposition -O3 -falign-functions=32",

                "--enable-modules",
                      "--disable-capstone",
                                    "--disable-werror",
        "--disable-bsd-user",
        "--disable-guest-agent",
           "--enable-curses",
#"--enable-libssh",
"--enable-kvm",
"--target-list=x86_64-softmmu x86_64-linux-user",
"--disable-sdl",
"--disable-gtk",
"--enable-vnc",
"--enable-vnc-sasl",
"--enable-vnc-jpeg",
"--enable-vnc-png",
"--enable-curl",
#"--enable-spice",
"--enable-rbd",
"--enable-attr",
"--enable-cap-ng",
"--enable-vhost-net",
"--enable-vhost-scsi",
"--enable-vhost-vsock",
"--enable-vhost-kernel",
"--enable-vhost-user",
"--enable-tools",
"--enable-libusb",
"--enable-usb-redir",
"--enable-avx2",
"--enable-dmg",
"--enable-linux-aio",
"--enable-tpm",
"--enable-opengl",
"--enable-libiscsi",
"--enable-coroutine-pool",
"--enable-jemalloc",
"--enable-numa",
"--enable-rdma",
"--enable-modules",
"--enable-trace-backends=simple,log",
"--enable-nettle",
# virtfs + xattr ... required
"--enable-virtfs",
"--enable-attr",
#Support xfsctl() notification and syncing for XFS backed virtual disks.
"--enable-xfsctl",
#--enable-netmap
#--enable-virglrenderer
#--enable-libnfs
#--with-confsuffix="/ms"
"--enable-pie",
"--audio-drv-list=pa",
"--enable-membarrier",
"--disable-qom-cast-debug"
                ]
        return args
