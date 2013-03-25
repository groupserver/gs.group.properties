# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.properties',
    version=version,
    description="GroupServer Group Properties",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='group properties',
    author='Alice Murphy',
    author_email='alice@onlinegroups.net',
    url='http://onlinegroups.net/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
        'zope.viewlet',
        'Zope2',
        'gs.content.form',
        'gs.group.base',
        'gs.group.home',
        'gs.group.member.viewlet',
        'gs.group.privacy',
        'gs.viewlet',

    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
