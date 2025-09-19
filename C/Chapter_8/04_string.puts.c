#include <stdio.h>

int main() {
    char st[30];      // declare a string of size 30

    gets(st);         // take input (⚠️ unsafe, avoid in real projects)
    puts(st);         // print the string with a newline
    printf("%s", st); // print the string without newline

    return 0;         // end program
}
// this puts just makes a new seperate line 