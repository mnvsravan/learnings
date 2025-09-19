#include <stdio.h>    // header file for input/output functions like printf
#include <string.h>   // header file for string functions like strcpy, strcat

int main() {

    char st[] = "Sravan";       // declare and initialize a string (array of chars with \0 at the end)
    char s1[30] = "the best";   // declare s1 with extra space (30 chars) so strcat can add more text
    char s2[30] = " ofc";         // declare and initialize another string
    char target[30];            // declare an empty target string with space for 30 chars

    strcpy(target, st);         // copy the contents of st ("Sravan") into target
                                // after this line, target contains "Sravan"

    strcat(s1, s2);             // append s2 (" ofc") to the end of s1 ("the best")
                                // now s1 contains "the best ofc"

    printf("%s\n", target);     // prints the copied string -> "Sravan"
    printf("%s\n", s1);         // prints the concatenated string -> "the best ofc"

    return 0;                   // program ends successfully
}

// this strcat is used to concatenate two strings