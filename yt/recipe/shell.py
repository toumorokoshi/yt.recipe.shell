"""
A recipe to add a shell command into buildout's bin/ folder

Example buildout recipe:
[django-test]
recipe = yt.recipe.shell
executable = /bin/bash
script = ./bin/django test myapp
name = test

allows:
bin/test
"""
import logging
import os
import zc.buildout


class Shell(object):

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.logger = logging.getLogger(self.name)

        for param in ['script', 'name']:
            if param not in options:
                raise zc.buildout.UserError('%s variable is required!' % param)
        self.executable = self.option['executable'] if 'executable' in self.options else "/usr/bin/env sh"
        self.script = options['script']
        self.script_name = options['name']

    def install(self):
        script_path = os.path.join(self.buildout['buildout']['directory'], 'bin', self.script_name)
        with open(script_path, 'w') as fh:
            fh.write("#!%s\n" % self.executable)
            fh.write(self.script)
        os.chmod(script_path, 509)  # 509 is 0775
        return script_path

    update = install
