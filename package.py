# -*- coding: utf-8 -*-

name = 'usd'

version = '19.11-houdini-18.0.532-ta.1.0.0'

authors = [
    'benjamin.skinner',
    'pixar',
    'sidefx',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

private_build_requires = [
    'python-2',
    'houdini-18.0.532',
]

# These could probably be broken down into more specific houdini versions
# technically they are mismatched. But it works for now...
requires = [
    'zlib-1.2.11',
    'tbb-2019.U9',
    'boost-1.61.0-houdini',
    'oiio-2.0.10-houdini',
    'PyOpenGL-3',
    'python-2.7',
]

# This package requires no building, only env setup
build_command = 'python {root}/rez_build.py'

def commands():
    # Split and store version and package version
    split_versions = str(version).split('-')
    env.USD_VERSION.set(split_versions[0])
    env.USD_PACKAGE_VERSION.set(split_versions[1])

    env.USD_ROOT.append( '{root}' )

    env.USD_INCLUDE_DIR.set( '{root}/include' )
    env.USD_LIBRARY_DIR.set( '{root}/lib' )
    env.USD_PYTHON_DIR.set( '{root}/lib/python' )


    env.USD_HOUDINI.set("1")
