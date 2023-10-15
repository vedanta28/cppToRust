#include "iostream"
template <typename T> class TemplExample {
private:
  T obj;
  int size;

public:
  TemplExample(T arr[], int s);
  void print();
};

template <typename T> TemplExample<T>::TemplExample(T o, int s) {
  obj = o;
  size = s;
  for (int i = 0; i < size; i++)
    obj += o;
}

template <typename T> void TemplExample<T>::print() { std::cout << " " << obj; }
