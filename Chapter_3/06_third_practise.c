#include <stdio.h>

int main() {
    char alpha = 'a';
    if(alpha >62 && alpha < 122){
        printf("the alphabet is lowercase\n");
    }
    else if(alpha <62 && alpha > 123){
        printf("the alphabet is uppercase\n");
    }
    return 0;

    }
    
    // ASCII values for 'a' to 'z' are 97 to 122 and for 'A' to 'Z' are 65 to 90