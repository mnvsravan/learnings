#include <stdio.h>   // Required for printf
#include <string.h>  // Required for strcpy

// Define struct employee and create alias Emp
typedef struct employee
{
    int code;        // Employee code (integer ID)
    float salary;    // Employee salary
    char name[10];   // Employee name (string up to 9 chars + '\0')
} Emp; // <-- typedef alias (now we can use "Emp" instead of "struct employee")

int main()
{
    // Declare a variable e1 of type Emp
    Emp e1;
    Emp *ptr=&e1;

    // Assign values
    e1.code = 4511;               // set code
    strcpy(e1.name, "Harry");     // copy string "Harry" into name
    e1.salary = 54.44;            // set salary

    // Print employee details
    printf("Code: %d\n", e1.code);
    printf("Name: %s\n", e1.name);
    printf("Salary: %.2f\n", e1.salary);

    return 0; // end of program
}
 // typedef is a keyword in C that allows you to create a new name (alias) for an existing data type.

//It does not create a new type, it just gives a convenient nickname.

//This makes code easier to read and write.