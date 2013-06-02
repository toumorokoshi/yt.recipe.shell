import unittest

import zc.buildout.testing


class TestShellBuildout(unittest.TestCase):

    def setUp(self):
        zc.buildout.testing.buildoutSetup(self)
        zc.buildout.install.develop('yt.recipe.shell', self)

    def tearDown(self):
        zc.buildout.testing.buildoutTearDown(self)
