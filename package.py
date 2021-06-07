# -*- coding: utf-8 -*-

name = "usd"

version = "21.02-maya.2020.4-ta.1.2.1"

authors = [
    "benjamin.skinner",
    "pixar",
    "kiki",
]


variants = [
    ["platform-windows", "python-2"],
    # ["platform-windows", "python-3"],
]

requires = [
    "boost-1.70.0",
    "oiio-1.8.9",
    "ocio-1.1.1",
    "openvdb-7.0.0",
    "opensubdiv-3.4.3",
    "openexr-2.4.0",
    "tbb-2019",
    "glew-2.0.0",
    "zlib",
    "PyOpenGL",     ## pip
    "Jinja2",       ## pip
    "MarkupSafe",   ## pip
]


@early()
def build_command():
    import sys
    if "win" in str(sys.platform):
        return "{root}\\rez_build.ps1"
    else:
        raise NotImplementedError("OS not yet supported, sorry.")


@early()
def private_build_requires():
    import sys
    if "win" in str(sys.platform):
        return ["visual_studio", "nasm"]
    else:
        return ["gcc-7"]


def commands():
    # Split and store version and package version
    split_versions = str(version).split("-")
    env.USD_VERSION.set(split_versions[0])
    env.USD_PACKAGE_VERSION.set(split_versions[1])

    env.USD_ROOT.append("{root}")

    env.USD_INCLUDE_DIR.set("{root}/include")
    env.USD_LIBRARY_DIR.set("{root}/lib")
    env.USD_PYTHON_DIR.set("{root}/lib/python")
    
    env.PATH.append("{root}/bin")
    env.PATH.append("{root}/lib")

    env.PYTHONPATH.append("{0}".format(env.USD_PYTHON_DIR))

