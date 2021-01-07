# -*- coding: utf-8 -*-

name = 'usd'

version = '20.08-houdini-18.5.351-ta.1.2.0'

authors = [
    'benjamin.skinner',
    'pixar',
    'sidefx',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

private_build_requires = [
    'python-2',
    'houdini-18.5.351',
]

# These could probably be broken down into more specific houdini versions
# technically they are mismatched. But it works for now...
requires = [
    'zlib-1.2.11',
    'tbb-2019.U9',
    'glew-1.13.0-houdini',
    'opensubdiv-3.4.3-houdini',
    'openvdb-7.1.0-houdini',
    'hboost-1.72.0-houdini',
    'oiio-2.0.10-houdini',
#    'PyOpenGL-3', # Removed for linux build
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

    env.USD_BUILD_VARIANT.set("USD_HOUDINI")
    
    env.PATH.append( str(env.USD_LIBRARY_DIR) )
