#include <string>
#include <iostream>
#include <zstd.h>

using namespace std;

int CompressString(const string& src, string& dst, int compressionlevel) {
  size_t const cBuffSize = ZSTD_compressBound(src.size());
  dst.resize(cBuffSize);
  auto dstp = const_cast<void*>(static_cast<const void*>(dst.c_str()));
  auto srcp = static_cast<const void*>(src.c_str());
  size_t const cSize = ZSTD_compress(dstp, cBuffSize, srcp, src.size(), compressionlevel);
  auto code = ZSTD_isError(cSize);
  if (code) {
    return code;
  }
  dst.resize(cSize);
  return code;
}

void zstd_example() {
    const std::string& src{"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"};
    std::string dst;
    int result = CompressString(src, dst, 2);
    std::cout << "Result: \"" << dst << "\"" << " code=" << result << "\n";
}