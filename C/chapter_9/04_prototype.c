#include <stdio.h>   // Required for input/output functions (printf, scanf)
#include <string.h>  // Required for string functions (like strcpy)

// Define a structure called "employee"
struct employee
{
    int code;        // Employee code (integer, unique ID)
    float salary;    // Employee salary (float number)
    char name[10];   // Employee name (character array / string)
}; // <-- semicolon is IMPORTANT after struct definition

// Function prototype (declaration)
void show(struct employee e);

// Function definition
// This function takes a struct employee as input and prints its details
void show(struct employee e)
{
    // Print the employee details
    printf("Code is %d\nSalary is %f\nName is %s\n", e.code, e.salary, e.name);
}

// Main function: program execution starts here
int main()
{
    // Declare a variable 'e1' of type struct employee
    struct employee e1;

    // Assign values to the fields of e1
    e1.code = 4511;                   // set employee code
    strcpy(e1.name, "Harry");         // copy string "Harry" into e1.name
    e1.salary = 54.44;                // set employee salary

    // Call the show() function to display employee details
    show(e1);

    return 0; // end of program (return 0 means successful execution)
}
