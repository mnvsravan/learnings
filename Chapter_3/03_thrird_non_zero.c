#include <stdio.h>

int main() {
    if (1){
        printf("This is a non-zero condition\n");
    } 
    if (232424){
        printf("This is another non-zero condition\n");
    }
    if ('k'){
        printf("This is a non-zero condition with a variable\n");
    } else {
        printf("The variable k is zero or not defined\n");
    }   
    if (0){
        printf("This will not print because 0 is false\n");
    } else {
        printf("This will print because 0 is false\n");
    }       
    return 0;
}
