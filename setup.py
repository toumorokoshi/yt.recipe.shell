#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='yt.recipe.shell',
      version='0.1.3',
      description='A buildout recipe to add in shell commands',
      author='Yusuke Tsutsumi',
      author_email='yusuke@yusuketsutsumi.com',
      url='http://github.com/toumorokoshi/yt.recipe.shell',
      packages=['yt.recipe'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ],
      entry_points={'zc.buildout': ['default = yt.recipe.shell:Shell']},
)
