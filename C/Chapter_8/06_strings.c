#include <stdio.h>    // header file for input/output functions like printf
#include <string.h>   // header file for string functions like strcpy

int main() {

    char st[] = "Sravan";    // declare and initialize a string (array of chars with \0 at end)
    char target[30];         // declare an empty target string with enough space

    strcpy(target, st);      // copy the contents of 'st' into 'target'
                             // after this, target contains "Sravan"

    printf("%s %s", st, target); // print both strings: first st, then target

    return 0;   // program ends successfully
}
// this strcpy is used for copying one string to another string , target should have enough capacity to store the string
