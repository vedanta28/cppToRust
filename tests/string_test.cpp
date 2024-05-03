#include <iostream>
#include <string>

using namespace std;

int main() {
    // Creating a string
    string s = "Hello, World!";
    
    // Printing original string
    cout << "Original string: " << s << endl;
    
    // size() and length(): Getting the size/length of the string
    cout << "Size of string: " << s.size() << endl;
    cout << "Length of string: " << s.length() << endl;
    
    // resize(): Resizing the string
    s.resize(7);
    cout << "Resized string: " << s << endl;
    
    // clear(): Clearing the string
    s.clear();
    cout << "Cleared string: " << s << endl;
    
    // empty(): Checking if the string is empty

    if (s.empty()) {
        cout << "String is empty" << endl;
    } else {
        cout << "String is not empty" << endl;
    }
    
    // operator= : Assigning a new value to the string
    s = "New Value";
    cout << "New value assigned: " << s << endl;
    
    // operator[] and at(): Accessing characters in the string
    cout << "Character at index 2: " << s[2] << endl;
    cout << "Character at index 4: " << s.at(4) << endl;
    
    // back() and front(): Getting the first and last characters of the string
    cout << "First character: " << s.front() << endl;
    cout << "Last character: " << s.back() << endl;
    
    // operator+= and append(): Appending to the string
    s += " appended";
    cout << "String after operator+=: " << s << endl;
    
    s.append(" with append");
    cout << "String after append: " << s << endl;
    
    // push_back(): Appending a single character
    s.push_back('!');
    cout << "String after push_back: " << s << endl;
    
    // assign(): Assigning a value with specified length
    s.assign(5, 'A');
    cout << "String after assign: " << s << endl;
    
    // replace(): Replacing part of the string with another string
    s.replace(2, 3, "XYZ");
    cout << "String after replace: " << s << endl;
    
    // swap(): Swapping the contents of two strings
    string anotherString = "Another string";
    cout << "Before swap: " << s << ", " << anotherString << endl;
    s.swap(anotherString);
    cout << "After swap: " << s << ", " << anotherString << endl;
    
    // pop_back(): Removing the last character from the string
    s.pop_back();
    cout << "String after pop_back: " << s << endl;
    
    // substr(): Extracting a substring
    string substr = s.substr(2, 4);
    cout << "Substring: " << substr << endl;

}
