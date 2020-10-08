# -*- coding: utf-8 -*-

name = 'usd'

version = '20.05-ta.1.1.0'

authors = [
    'benjamin.skinner',
    'pixar',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

requires = [
    'python-3.7',
    'PySide2-5.12.2',
    'PyOpenGL-3.1.5',
    'oiio-1.8.9',
    'ocio-1.1.1',
    #'openvdb-7.0.0',
    'opensubdiv-3.4.3',
    'openexr-2.4.0',
    'boost-1.69.0',
    'tbb-2019',
    'glew-2.0.0',
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

build_system = "cmake"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.USD_VERSION.set(split_versions[0])
    env.USD_PACKAGE_VERSION.set(split_versions[1])

    env.USD_ROOT.append( '{root}' )

    env.USD_INCLUDE_DIR.set( '{root}/include' )
    env.USD_LIBRARY_DIR.set( '{root}/lib' )
    env.USD_PYTHON_DIR.set( '{root}/lib/python' )
    
    env.PATH.append( '{root}/bin' )
    env.PATH.append( '{root}/lib' )

    env.PYTHONPATH.append( '{0}'.format( env.USD_PYTHON_DIR ) )