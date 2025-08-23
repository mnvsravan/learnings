#include <stdio.h>
int change(int a); // Function prototype
int change(int a) { // Function definition
    a = 98;  // This change is local to the function (misnomer)
    return 0;
}
    int main() {
    int b=22;
     change(b); // b is passed by value, so the original b in main() is not changed
     printf("The value of b is %d\n",b);// b is still 22 because change() does not modify it
    


    return 0;
}
