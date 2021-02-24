
echo "USD Build: Installing to $env:REZ_BUILD_INSTALL_PATH"

pushd $env:REZ_BUILD_SOURCE_PATH
md build
cd build
cmake.exe -G "Visual Studio 15 2017 Win64" -Wno-dev --no-warn-unused-cli "-DCMAKE_INSTALL_PREFIX=$env:REZ_BUILD_INSTALL_PATH" "-DCMAKE_MODULE_PATH=$env:CMAKE_MODULE_PATH" -DCMAKE_BUILD_TYPE=Release -DREZ_BUILD_TYPE=local -DREZ_BUILD_INSTALL=1 "$env:REZ_BUILD_SOURCE_PATH" -DPXR_ENABLE_PYTHON_SUPPORT=OFF
cmake --build . --config Release --target INSTALL
popd

echo "USD Install complete."

