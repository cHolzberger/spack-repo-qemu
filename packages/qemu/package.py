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
    url      = "https://download.qemu.org/qemu-4.2.0.tar.xz"
    depends_on("gawk",type=('build', 'link' ))
    depends_on('libelf', type=('build', 'link'))
    depends_on('jemalloc', type=('build', 'link'))
    depends_on("libcap-ng")
    depends_on("curl")
    depends_on("glib")
    depends_on("pixman")
    depends_on("numactl")
    depends_on("libaio")
    depends_on("liburing")
    depends_on("libiscsi")
    depends_on("libusb")
    depends_on("usbredir")
 #   depends_on("libcap")
    depends_on("libattr")
    #depends_on("rdma-core")
    #   depends_on("xfs")
    #  depends_on("xfsinfo")
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('4.2.0', sha256='d3481d4108ce211a053ef15be69af1bdd9dde1510fda80d92be0f6c3e98768f0')

    patch('https://github.com/saveriomiroddi/qemu-pinning/commit/4e4fe6402e9e4943cc247a4ccfea21fa5f608b30.patch', sha256='c6b69ec2820605e24ff490dceefebf78768dc816a1bdaf43ab32b25976e4582e', when="@4.2.0:")

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
"--target-list=x86_64-softmmu",
"--disable-sdl",
"--disable-gtk",
"--enable-vnc",
#"--enable-vnc-sasl",
#"--enable-vnc-jpeg",
#"--enable-vnc-png",
"--enable-curl",
#"--enable-spice",
#"--enable-rbd",
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
#"--enable-dmg",
"--enable-linux-aio",
#"--enable-linux-io-uring",
"--enable-tpm",
#"--enable-opengl",
"--enable-libiscsi",
"--enable-coroutine-pool",
"--enable-jemalloc",
"--enable-numa",
#"--enable-rdma",
#"--enable-trace-backends=simple,log",
#"--enable-nettle",
# virtfs + xattr ... required
"--enable-virtfs",
"--enable-attr",
#Support xfsctl() notification and syncing for XFS backed virtual disks.
#"--enable-xfsctl",
#--enable-netmap
#--enable-virglrenderer
#--enable-libnfs
#--with-confsuffix="/ms"
"--enable-pie",
#"--audio-drv-list=pa",
"--enable-membarrier",
"--disable-qom-cast-debug"
                ]
        return args
