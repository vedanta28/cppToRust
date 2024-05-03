#include <iostream>

using namespace std;

namespace myapp
{
  namespace xd
  {
    namespace tl {}
    void tr() { cout << "Inside\n"; }
  } // namespace xd
  void pr() { cout << "Hello\n"; }
} // namespace myapp

int main()
{
  myapp::pr();
  using namespace myapp::xd;
  tr();
}
