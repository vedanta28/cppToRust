#include <iostream>

int main() {
    int p = 1;
    int *q = &p;
    (*q)++;
    (*q) += 1;
    printf("%d", *q);
    printf("%d", p);
}