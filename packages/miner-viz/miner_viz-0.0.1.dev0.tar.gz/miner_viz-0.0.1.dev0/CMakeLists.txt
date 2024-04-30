# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

# scikit-build-core 已经设置了这些环境变量
# 也可以在这里硬编码
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

# 避免cmake的一些警告
set(CMAKE_POLICY_DEFAULT_CMP0077 NEW)

# 使用C++ 11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
# fPIC
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# zstd
set(ZSTD_BUILD_STATIC ON)
set(ZSTD_BUILD_SHARED OFF)
set(ZSTD_BUILD_PROGRAMS OFF)
set(ZSTD_INSTALL OFF)
add_subdirectory(third_party/zstd/build/cmake)

# zlib
set(ZLIB_BUILD_EXAMPLES OFF)
add_subdirectory(third_party/zlib)

# crc32c
set(CRC32C_BUILD_TESTS OFF)
set(CRC32C_BUILD_BENCHMARKS OFF)
set(CRC32C_INSTALL OFF)
set(CRC32C_USE_GLOG OFF)
add_subdirectory(third_party/crc32c)

# snappy
set(SNAPPY_BUILD_TESTS OFF)
set(SNAPPY_BUILD_BENCHMARKS OFF)
set(SNAPPY_INSTALL OFF)
add_subdirectory(third_party/snappy)

# 不构建LevelDB的测试
set(LEVELDB_BUILD_TESTS OFF)
set(LEVELDB_BUILD_BENCHMARKS OFF)
set(LEVELDB_INSTALL OFF)
add_subdirectory(third_party/mojang-leveldb)

add_subdirectory(third_party/example)
add_subdirectory(third_party/example2)

# Find the module development requirements (requires FindPython from 3.17 or
# scikit-build-core's built-in backport)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

# Python包
# Add a library using FindPython's tooling (pybind11 also provides a helper like
# this)
python_add_library(_core MODULE src/main_py.cc src/zstd_example.cc src/zlib_example.cc src/crc32c_example.cc src/snappy_example.cc WITH_SOABI)
target_link_libraries(_core PRIVATE pybind11::headers)

target_include_directories(_core PRIVATE ${PROJECT_SOURCE_DIR}/include)

target_link_libraries(_core PRIVATE
    example
    leveldb
    libzstd_static
    zlibstatic
    crc32c
    snappy
)

# 二进制产物
# add_executable(mviz-bin src/main.cc src/zstd_example.cc src/zlib_example.cc src/crc32c_example.cc src/snappy_example.cc)

# target_include_directories(mviz-bin PRIVATE ${PROJECT_SOURCE_DIR}/include)

# target_link_libraries(mviz-bin PRIVATE
#     example
#     leveldb
#     libzstd_static
#     zlibstatic
#     crc32c
#     snappy
# )

# 定义一个宏，作为例子
target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

# The install directory is the output (wheel) directory
install(TARGETS _core DESTINATION miner_viz)
