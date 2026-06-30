#include <stdio.h>
#include <stdlib.h> // Required for abs()

void update(int *pa, int *pb) {
    int sum = *pa + *pb;
    int diff = abs(*pa - *pb);
    
    *pa = sum;  // Update the value at address pa
    *pb = diff; // Update the value at address pb
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}