#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
    // Declare a set of integers
    set<int> mySet;
    set<vector<int>> vecSet;
    vector<int> v1 = {1, 2, 3};
    vecSet.insert(v1);


    // Check if the set is empty
    if (mySet.empty()) {
        cout << "Set is empty" << endl;
    } else {
        cout << "Set is not empty" << endl;
    }

    // Insert elements into the set
    mySet.insert(5);
    mySet.insert(10);
    mySet.insert(15);
    mySet.insert(20);

    // Get the size of the set
    cout << "Size of set: " << mySet.size() << endl;

    // Count occurrences of an element in the set
    cout << "Count of 10 in set: " << mySet.count(10) << endl;
    cout << "Count of 25 in set: " << mySet.count(25) << endl;

    // Erase an element from the set
    mySet.erase(15);

    // Check the size after erasing
    cout << "Size of set after erasing: " << mySet.size() << endl;

    // Swap sets
    set<int> anotherSet;
    anotherSet.insert(100);
    anotherSet.insert(200);
    mySet.swap(anotherSet);

    cout << "Size of mySet after swapping: " << mySet.size() << endl;
    cout << "Size of anotherSet after swapping: " << anotherSet.size() << endl;

    // Clear the set
    mySet.clear();

    cout << "Size of mySet after clearing: " << mySet.size() << endl;
}
