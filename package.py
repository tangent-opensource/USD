# -*- coding: utf-8 -*-

name = 'usd'

version = '20.05+ta.1.0.0'

authors = [
    'pixar',
    'benjamin.skinner',
]

requires = [
    'python-3',
    'PySide2-5.14.1',
    'PyOpenGL-3.1.5',
]

# TODO: Fill these out with proper build requirements
build_requires = [

]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10', 'visual_studio'],
]

build_command = 'python {root}/rez_build.py'

def pre_build_commands():
    env.TMP_USD_BUILD_PATH.set('C:/dev/builds/usd_20_05')

def commands():
    env.USD_ROOT.append( '{root}/build' )

    env.USD_INCLUDE_DIR.set( '{0}/include'.format(env.USD_ROOT) )
    env.USD_LIBRARY_DIR.set( '{0}/lib'.format(env.USD_ROOT) )
    env.USD_PYTHON_DIR.set( '{0}/lib/python'.format( env.USD_ROOT ) )
    
    env.PATH.append( '{0}/bin'.format( env.USD_ROOT ) )
    env.PATH.append( '{0}/lib'.format( env.USD_ROOT ) )

    env.PYTHONPATH.append( '{0}'.format( env.USD_PYTHON_DIR ) )