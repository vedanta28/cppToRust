int main()
{
    // While Loop
    int n = 15, a = 10, b = 10;
    int c = 200;
    while (a + b)
    {
        b = b + 1;
    }

    // For Loop
    for (int i = 2; i <= n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
}