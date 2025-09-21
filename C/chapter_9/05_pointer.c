#include <stdio.h>   // Required for printf and other standard I/O functions

// Define a structure called "employee"
struct employee
{
    int code;        // Employee code (integer, unique ID)
    float salary;    // Employee salary (float number)
    char name[10];   // Employee name (string of up to 9 characters + '\0')
}; // <-- semicolon is IMPORTANT after struct definition

int main()
{
    // Step 1: Declare a variable 'e1' of type struct employee
    struct employee e1;

    // Step 2: Assign a value to e1's 'code' field
    e1.code = 56;

    // Step 3: Declare a pointer to struct employee
    struct employee *ptr;

    // Step 4: Assign the address of e1 to the pointer
    ptr = &e1; // this can we written as struct employee *ptr = &e1;


    // Step 5: Access structure members using the pointer
    // Option 1: Using (*ptr).member
    printf("Employee code (using (*ptr).code): %d\n", (*ptr).code);

    // Option 2: Using the arrow operator (shortcut for (*ptr).member)
    printf("Employee code (using ptr->code): %d\n", ptr->code);

    return 0; // end of program
}
