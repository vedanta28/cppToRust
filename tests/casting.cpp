#include <iostream>

int main() {
  int a = 5;
  int b = (int)a;
  long long c = a;
  int d = (long long)((int) a);
  int e = static_cast<int>(c);
  std::cout << ":";
}
