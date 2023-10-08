#include "iostream"
template <typename T> class Array {
private:
  T *ptr;
  int size;

public:
  Array(T arr[], int s) {
    ptr = new T[s];
    size = s;
    for (int i = 0; i < size; i++)
      ptr[i] = arr[i];
  }
  void print() {
    for (int i = 0; i < size; i++)
      std::cout << " " << *(ptr + i);
  }
};
