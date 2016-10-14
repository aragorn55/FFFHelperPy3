from __future__ import print_function
import glob
import os
import subprocess
class ProcessFiles(object):
    blacklist = [__file__, 'venv', 'venv3', 'build', 'dist']


    def walker(self, path):
        """Folder walker that collects .py files
        """
        files = []
        for fn in glob.glob(os.path.join(path, "*")):
            if fn in [os.path.join(path, x) for x in self.blacklist]:
                continue
            if os.path.isdir(fn):
                files.extend(self.walker(fn))
            elif os.path.splitext(fn)[-1] == '.py':
                files.append(fn)
        return files


    def future(self, path):
        """Runs futurize on python files
        See: http://python-future.org/automatic_conversion.html
        """
        print(path)
        print(subprocess.check_output(['futurize', '--stage1', path])) # '-w', '--unicode-literals'
        print()


    if __name__ == '__main__':
        for fn in walker('.'):
            future(fn)