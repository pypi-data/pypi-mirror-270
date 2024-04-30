#include "example/example.h"
#include <string>
#include <iostream>
#include <example2/example2.h>
namespace example {
    void generate_output(const std::string& text)
    {
        example2::generate_output2(text + " - 2");
    }
}
