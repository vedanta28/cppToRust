#include <iostream>
template <typename T> class TemplExample {
private:
  T obj;
  int size;

public:
  TemplExample(T o, int s) {
    obj = o;
    size = s;
    for (int i = 0; i < size; i++)
      obj += o;
  }
  void print() { std::cout << " " << obj; }
};
int main() {
  // main function
}
