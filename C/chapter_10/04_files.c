#include <stdio.h>   // Includes the standard input/output library
                     // Required for file handling functions like fopen, fgetc, printf

int main()           // Entry point of the program
{
    FILE *ptr;       // Declares a pointer to FILE, used for handling the file

    // Opens the file "harry.txt" in read mode ("r")
    // If the file does not exist, fopen will return NULL
    ptr = fopen("harry.txt", "r");

    // Reads a single character from the file using fgetc()
    // fgetc(ptr) returns the next character from the file
    char c = fgetc(ptr);   // The first character of the file will be stored in 'c'

    // Prints the character read from the file to the console
    // "%c" is a format specifier for characters
    printf("%c", c);

    // Example of writing a character (currently commented out)
    // fputc('c', ptr);   // Would write 'c' to the file if opened in write/append mode

    return 0;        // Indicates successful program execution
}

