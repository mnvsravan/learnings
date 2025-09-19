#include <stdio.h>    // header file for input/output functions like printf
#include <string.h>   // header file for string functions like strcpy, strcat

int main() {

    int a= strcmp("far","ajoke");
    printf("%d",a);
    return 0;
}
// this strcmp is used to compare the two strings according to the ascii value 
// it returns 0 if the straings are equal it gives negative if the first is lesser and positve if the second is greater 