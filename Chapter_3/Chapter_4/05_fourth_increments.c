#include <stdio.h>

int main() {
    int i=5;
    printf("The value of i is %d\n",i);
    i=i+5;
    printf("The value of i is %d\n",+i++);
   
    return 0;
    }
    

// ++i increments i by 1 and prints i
//i++ prints i and then increments i by 1
// same for --i and i-- but for decrementing