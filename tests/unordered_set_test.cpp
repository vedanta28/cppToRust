#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    // Declare an unordered_set of integers
    unordered_set<int> mySet;

    // Check if the unordered_set is empty
    if (mySet.empty()) {
        cout << "Unordered_set is empty" << endl;
    } else {
        cout << "Unordered_set is not empty" << endl;
    }

    // Insert elements into the unordered_set
    mySet.insert(5);
    mySet.insert(10);
    mySet.insert(15);
    mySet.insert(20);

    // Get the size of the unordered_set
    cout << "Size of unordered_set: " << mySet.size() << endl;

    // Count occurrences of an element in the unordered_set
    cout << "Count of 10 in unordered_set: " << mySet.count(10) << endl;
    cout << "Count of 25 in unordered_set: " << mySet.count(25) << endl;

    // Erase an element from the unordered_set
    mySet.erase(15);

    // Check the size after erasing
    cout << "Size of unordered_set after erasing: " << mySet.size() << endl;

    // Swap unordered_sets
    unordered_set<int> anotherSet;
    anotherSet.insert(100);
    anotherSet.insert(200);
    mySet.swap(anotherSet);

    cout << "Size of mySet after swapping: " << mySet.size() << endl;
    cout << "Size of anotherSet after swapping: " << anotherSet.size() << endl;

    // Clear the unordered_set
    mySet.clear();

    cout << "Size of mySet after clearing: " << mySet.size() << endl;
}
