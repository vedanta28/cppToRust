#include <iostream>
#include <stack>

using namespace std;

int main() {
  stack<int> s1;
  if (s1.empty()) { // Vector is Empty
    cout << "Stack is Empty\n";
  } else {
    cout << "Stack is Non-Empty\n";
  }
  s1.push(10);
  s1.push(20);
  s1.emplace(20);
  cout << "S1.size() = " << s1.size() << "\n";
  while (!s1.empty()) {
    cout << s1.top() << " ";
    s1.pop();
  }
  cout << "\n";

  stack<int> s2;
  s2 = s1;
  s1.push(4);
  cout << "Before swap\n";
  cout << " s1.len() = " << s1.size() << "\n";
  cout << " s2.len() = " << s2.size() << "\n";
  s1.swap(s2);
  cout << "After swap\n";
  cout << " s1.len() = " << s1.size() << "\n";
  cout << " s2.len() = " << s2.size() << "\n";
}
