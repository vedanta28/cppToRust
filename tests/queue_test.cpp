#include <iostream>
#include <queue>

using namespace std;

int main() {
    // Create a queue
    queue<int> myQueue;

    // Push elements to the queue
    myQueue.push(1);
    myQueue.push(2);
    myQueue.push(3);

    // Display front and back elements
    cout << "Front element: " << myQueue.front() << endl;
    cout << "Back element: " << myQueue.back() << endl;

    // Check if the queue is empty
    if(myQueue.empty()){
        cout << "Queue is empty" << endl;
    } else {
        cout << "Queue is not empty" << endl;
    }

    // Display the size of the queue
    cout << "Size of the queue: " << myQueue.size() << endl;

    // Create another queue
    queue<int> anotherQueue;

    // Copy the contents of the first queue to the second using operator=
    anotherQueue = myQueue;

    // Display the elements of both queues
    cout << "First Queue: ";
    while (!myQueue.empty()) {
        cout << myQueue.front() << " ";
        myQueue.pop();
    }
    cout << endl;

    cout << "Second Queue: ";
    while (!anotherQueue.empty()) {
        cout << anotherQueue.front() << " ";
        anotherQueue.pop();
    }
    cout << endl;

    // Swap the contents of the two queues
    myQueue.push(4);
    myQueue.push(5);
    anotherQueue.push(6);

    cout << "Before Swap - First Queue: 4,5 Second Queue: 6" << endl;

    myQueue.swap(anotherQueue);

    cout << "After Swap - First Queue: ";
    while (!myQueue.empty()) {
        cout << myQueue.front() << " ";
        myQueue.pop();
    }
    cout << endl;

    cout << "After Swap - Second Queue: ";
    while (!anotherQueue.empty()) {
        cout << anotherQueue.front() << " ";
        anotherQueue.pop();
    }
    cout << endl;
}