#include <stdio.h>

int main() {
     int st[]={'a','b','c','d', '\0'};
     // this \0 is known as null and this ends this string
     for(int i=0;i<5;i++){
        printf("The charac is %c \n", st[i]);
     }
    return 0;
}
// we can stop by 4 