#include "example2/example2.h"
#include <string>
#include <iostream>
namespace example2 {
    void generate_output2(const std::string& text)
    {
        for(int i = 0; i < 3; ++i) std::cout << text << "2\n";
    }
}
