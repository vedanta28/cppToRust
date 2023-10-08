// Function Definition
void do_nothing(int k)
{
    k = k + 1;
    k++;
    printf("This function does nothing\n");
}

// Function Definitions
int fib(int n)
{
    int a = 0, b = 1, c;
    if (n == 0)
        return a;

    // Conditional
    for (int i = 2; i <= n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

char random_function(char a, char b, bool status)
{
    return status ? a : b;
}

// Driver code
int main()
{

    // Simple Declarations
    int n = 11;
    int a = fib(n);
    bool flag = false;
    char input1 = 'm';

    char output = random_function('l', input1, flag);

    do_nothing(555);
    cout << output << endl;
    cout << "Fibonacci " << fib(n) << endl;
}
