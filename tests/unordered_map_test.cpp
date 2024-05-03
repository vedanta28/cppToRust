#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
  unordered_map<int, int> mp;
  unordered_map<int, vector<string>> vecmp;
  vector<string> v = {"a"};
  vecmp.insert({1, v});
  if (mp.empty()) {
    cout << "Set is empty" << endl;
  } else {
    cout << "Set is not empty" << endl;
  }
  mp.insert({1, 1});
  mp.insert({2, 2});
  cout << "Size of mp:" << mp.size() << endl;
  cout << "Count of 1 in mp:" << mp.count(1) << endl;
  cout << "Count of 3 in mp:" << mp.count(3) << endl;
  mp.erase(1);
  cout << "Size of mp after removing:" << mp.size() << endl;

  // Swap maps
  unordered_map<int, int> mp2;
  mp2.insert({3, 3});
  mp2.insert({5, 5});
  mp.swap(mp2);

  cout << "Size of mp after swapping:" << mp.size() << endl;
  cout << "Size of mp2 after swapping:" << mp2.size() << endl;

  mp.clear();
  cout << "size of mp after clear" << mp.size() << endl;
}
