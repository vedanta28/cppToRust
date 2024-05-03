#include <iostream>
#include <deque>
#include <queue>

using namespace std;

int main() {
    // Create a deque
    deque<int> deque1;

    // PushBack
    deque1.push_back(1);
    deque1.push_back(2);
    deque1.push_back(3);

    // Display
    cout << "Deque 1: ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    cout << endl;

    // Create another deque
    deque<int> deque2 = {6, 7, 8, 9, 10};

    // PushBack
    deque2.push_back(4);
    deque2.push_back(5);

    cout << "Deque 2: ";
    for (size_t i = 0; i < deque2.size(); ++i) {
        cout << deque2[i] << " ";
    }
    cout << endl;

    // Swap
    deque1.swap(deque2);

    // Display after swap
    cout << "Deque 1 (after swap): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    cout << endl;
    cout << "Deque 2 (after swap): ";
    for (size_t i = 0; i < deque2.size(); ++i) {
        cout << deque2[i] << " ";
    }
    cout << endl;

    // Access an element by index
    cout << "Element at index 1 in deque 1: " << deque1[1] << endl;

    // Display front and back elements
    cout << "Front element of deque 1: " << deque1.front() << endl;
    cout << "Back element of deque 1: " << deque1.back() << endl;

    // Check if deque1 is empty
    if (deque1.empty()){
        cout << " The deque is empty \n";
    } else {
        cout<< " The deque is not empty() \n";
    }
    //  << (deque1.empty() ? "Yes" : "No") << endl;

    // Display size of deque1
    cout << "Size of deque 1: " << deque1.size() << endl;

    // Clear
    deque1.clear();
    cout << "Deque 1 (after clear): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    cout << endl;

    // PushFront and PopFront
    deque1.push_front(10);
    deque1.push_front(20);
    deque1.push_front(30);
    cout << "Deque 1 (after push_front): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    cout << endl;
    deque1.pop_front();
    cout << "Deque 1 (after pop_front): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    cout << endl;

    // Resize
    deque1.resize(5, 99);
    cout << "Deque 1 (after resize): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    cout << endl;

    // EmplaceFront
    deque1.emplace_front(50);
    cout << "Deque 1 (after emplace_front): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
    deque1=deque2;
    cout << endl;
    cout << "Deque 1 (after assignment): ";
    for (size_t i = 0; i < deque1.size(); ++i) {
        cout << deque1[i] << " ";
    }
}