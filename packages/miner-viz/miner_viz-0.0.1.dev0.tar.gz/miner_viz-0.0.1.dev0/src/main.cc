#include <iostream>
#include <example/example.h>
#include "main.h"


int main() {
    std::cout << "hello, world\n";
    example::generate_output("EX1");

    zstd_example();
    zlib_example();
    crc32c_example();
    snappy_example();
    return 0;
}
