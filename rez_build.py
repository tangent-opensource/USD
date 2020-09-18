import os
import shutil

# When we move to a proper rez build, this file will be deprecated

if __name__ == "__main__":
    
    # Copy Tangent USD Build to rez build dir

    src = os.environ["TMP_USD_BUILD_PATH"]
    dst = str(os.environ["REZ_BUILD_INSTALL_PATH"]) + "/build"

    print("Copying: {0} : {1}".format(src, dst))

    try:
        shutil.copytree(src, dst)
    except:
        print(" - Files already exist.")
        pass

    print("Complete!")
    

