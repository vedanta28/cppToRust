#include "iostream"
class Car {
private:
  int fuel_eff;
  int size;

public:
  Car(int fe, int s);
  void print();
};

Car::Car(int fe, int s) {
  fuel_eff = fe;
  size = s;
}

void Car::print() {
  std::cout << "Size: " << size << "\n"
            << "Fuel efficiency: " << fuel_eff << "\n";
}
