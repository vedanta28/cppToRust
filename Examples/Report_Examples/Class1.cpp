#include <bits/stdc++.h>
using namespace std;

class Rectangle
{
public:
    int area()
    {
        return width * height;
    }
    int width;

    int perimeter()
    {
        return 2 * (width + height);
    }

    int setWidth(int w)
    {
        width = w;
        return w;
    }

    int setHeight(int h)
    {
        height = h;
        return h;
    }

    int myRandomProp;

    Rectangle()
    {
        printf("Do nothing\n");
        width = 5;
        height = 9;
        myRandomProp = 10;
    }

    int height;
};

int main()
{
    Rectangle r;
    Rectangle r(45, 45);

    SomeRandomClass c(78, c);

    r.setWidth(4);
    r.setHeight(5);
    cout << "Area of r: " << r.area() << "\n";
    cout << "Perimeter of r: " << r.perimeter() << "\n";
    r.setWidth(6);
    r.setHeight(7);
    cout << "New area of r: " << r.area() << "\n";
    cout << "New perimeter of r: " << r.perimeter() << "\n";

    return 0;
}