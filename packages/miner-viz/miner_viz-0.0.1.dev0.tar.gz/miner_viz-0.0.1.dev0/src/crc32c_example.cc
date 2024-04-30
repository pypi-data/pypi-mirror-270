#include <iostream>
#include <crc32c/crc32c.h>

void crc32c_example()
{
    std::uint32_t result;

    // Process a std::string.
    std::string string{"hello, world"};
    string.resize(4);
    result = crc32c::Crc32c(string);

    std::cout << "crc32c(" << string << ") = " << result << "\n";
}