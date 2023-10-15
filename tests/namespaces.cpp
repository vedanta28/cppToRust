#include <iostream>

namespace myapp {
// int x = 10;
// int x = 5;
namespace xd {
namespace tl {}
void tr() { cout << "Inside"; }
} // namespace xd
void pr() { cout << "Hello"; }
} // namespace myapp

int main() {
  // cout << myapp::x;
  myapp::pr();
  using namespace myapp::xd;
  myapp::xd::tr();
}
