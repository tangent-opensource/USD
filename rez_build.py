import os, subprocess, sys
import shutil
import glob

# Eventually we might build directly from the Sidefx fork
# https://github.com/sideeffects/USD
# but for now we just copy to a rezified location

if __name__ == "__main__":
    src = os.environ["HOUDINI_ROOT"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"]
    inc_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/include"
    lib_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/lib"

    if 'win' in str(sys.platform):

        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)

        print("Starting install")

        shutil.copytree(src + "/toolkit/include/pxr", inc_dst + "/pxr")

        os.mkdir(lib_dst)

        lib_files = glob.glob(src + '/custom/houdini/dsolib/libpxr_*.lib')

        for f in lib_files:
            #print(f)
            shutil.copy(f, lib_dst + "/" + os.path.basename(f))

        dll_files = glob.glob(src + '/bin/libpxr_*.dll')

        for f in dll_files:
            #print(f)
            shutil.copy(f, lib_dst + "/" + os.path.basename(f))

        print("Install complete")
