#include <stdio.h>   // Include the standard input/output library
                      // Provides functions like printf, scanf, fopen, fscanf, etc.

int main()  // Entry point of the program
{
    FILE *ptr;   // Declare a pointer 'ptr' of type FILE
                 // FILE is a structure used for file handling in C
                 // 'ptr' will point to the file we want to work with

    ptr = fopen("harry.txt", "r");  
    // fopen() is used to open a file
    // "harry.txt" is the name of the file we want to open
    // "r" indicates that we are opening the file in read mode
    // The function returns a pointer to the file, which is stored in 'ptr'
    // If the file does not exist or cannot be opened, ptr will be NULL

    int num;   // Declare an integer variable 'num' to store values read from the file

    fscanf(ptr, "%d", &num);  
    // fscanf() reads formatted input from a file
    // ptr is the file pointer from which we read
    // "%d" specifies that we are reading an integer
    // &num is the address of the variable where the read value will be stored
    // This reads the first integer from the file "harry.txt"

    printf("The value of num is %d \n", num);  
    // printf() prints output to the console
    // "%d" is a placeholder for an integer
    // num is the value that will replace %d in the output
    // \n moves the cursor to a new line after printing

    fscanf(ptr, "%d", &num);  
    // Read the second integer from the file
    // fscanf automatically moves the file pointer forward
    // so the next fscanf reads the next value in the file

    printf("The value of num is %d \n", num);  
    // Print the second integer read from the file

    return 0;  
    // Return 0 indicates that the program executed successfully
}
 // look at that harrytxt it prints the same numbers 