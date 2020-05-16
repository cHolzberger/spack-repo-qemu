from spack import *
import os
import shutil

class Cni(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/containernetworking/cni/archive/v0.7.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.7.1', sha256='4517eabfd65aea2012dc48d057bf889a0a41ed9837387d95cd1e36c0dbddcfd4')

    build_directory = os.path.join( "src", "github.com", "containernetworking", "cni" )
    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('go', type="build")
    depends_on('go-md2man', type='build')

    def do_stage(self, mirror_only=False):
       """ move the source dir to src/github.com/xxx/xxx go likes it this way """
       super().do_stage(mirror_only)
       stsrc = self.stage.source_path
       srcpath = os.path.join( stsrc, self.build_directory )
       ppath = ancestor (srcpath)
       shutil.move(stsrc, stsrc+"_old")
       mkdirp(ppath)
       shutil.move(stsrc+"_old",srcpath)


    def build(self, spec, prefix):
        env['GOPATH'] = self.stage.source_path
        go = which('go')
        with working_dir( os.path.join( self.build_directory, "cnitool" )):
            go('build')

    def install(self,spec,prefix):
        env['GOPATH'] = self.stage.source_path
        go = which('go')
        with working_dir( os.path.join( self.build_directory, "cnitool" )):
            go('install')
        mkdirp(os.path.join(prefix,"bin"))
        install(os.path.join(self.stage.source_path, "bin", "cnitool"), os.path.join(prefix,"bin","cnitool") )
