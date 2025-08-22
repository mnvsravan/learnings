#include <stdio.h>

int main() {
    int i;  
    for (i = 0; i < 10; i++) {  // initialization, condition, increment
        if (i == 5) 
            continue;   // skip the rest of the loop when i equals 5
        
        printf("The value of i is %d\n", i);
    }
    return 0;  // should be after the loop
}
