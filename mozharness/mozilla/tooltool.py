import os

from mozharness.base.errors import PythonErrorList
from mozharness.base.log import FATAL

class TooltoolMixin(object):
    """Mixin class for handling tooltool manifests.
    Requires self.config['tooltool_servers'] to be a list of base urls
    """
    def tooltool_fetch(self, manifest, output_dir=None):
        """docstring for tooltool_fetch"""
        tooltool = self.query_exe('tooltool.py', return_type='list')
        cmd = tooltool
        for s in self.config['tooltool_servers']:
            cmd.extend(['--url', s])
        cmd.extend(['fetch', '-m', manifest, '-o'])
        self.run_command(cmd, cwd=output_dir, error_list=PythonErrorList)

    def create_tooltool_manifest(self, contents, path=None):
        """ Currently just creates a manifest, given the contents.
        We may want a template and individual values in the future?
        """
        if path is None:
            dirs = self.query_abs_dirs()
            path = os.path.join(dirs['abs_work_dir'], 'tooltool.tt')
        self.write_to_file(path, contents, error_level=FATAL)
        return path
