#include <vector>
#include <iostream>

using namespace std;
 
int main() {
    vector<int> v1;
    v1.push_back(10);
    v1.emplace_back(20);
    // Print output: 10 20
    for (size_t i = 0; i < v1.size(); i++) {
        cout << v1[i] << " ";
    }
    cout << "\n";
    v1.pop_back();
    // Print output: 10
    for (size_t i = 0; i < v1.size(); i++) {
        cout << v1[i] << " ";
    }
    cout << "\n";

    vector<int> v2 = {1, 2, 3};
    // Print output: 1, 2, 3
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
    v2 = v1; 
    // Print output: 10
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
    v2.assign(3, 3);
    // Print output: 3, 3, 3
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
    v2.resize(2);
    // Print output: 3, 3
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
    v2.resize(4, 5);
    // Print output: 3, 3, 5, 5
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
    cout << v2[1] << " " << v2.at(1) << " " << v2.size() << " " << v2.front() << " " << v2.back() << endl; // 3 3 4 3 5
    v2.clear();
    if (v2.empty()) { // Vector is Empty
        cout << "Vector is Empty\n";
    } else {
        cout << "Vector is Non-Empty\n";
    }
    v2 = {1, 2};

    // Print output: 10
    for (size_t i = 0; i < v1.size(); i++) {
        cout << v1[i] << " ";
    }
    cout << "\n";
    
    // Print output: 1 2
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
    v1.swap(v2);
    // Print output: 1 2
    for (size_t i = 0; i < v1.size(); i++) {
        cout << v1[i] << " ";
    }
    cout << "\n";
    // Print output: 10
    for (size_t i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";
}