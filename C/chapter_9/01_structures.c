#include <stdio.h>    // For printf function
#include <string.h>   // For strcpy function (string copy)

// Define a new structure named 'employee'
struct employee {
    int code;            // Employee ID or code
    float salary;        // Employee's salary
    char name[10];       // Character array to store employee's name (max 9 chars + '\0')
}; // Note: Semicolon is important after struct definition

int main() {
    // Declare two variables of type struct employee
    struct employee e1;

    // Assign values to the members of structure e1
    e1.code = 4511;                        // Set employee code
    strcpy(e1.name, "MNVSRAVAN");             // Copy string "MNVSRAVAN" into e1.name
    e1.salary = 54.44;                    // Set employee salary

    // Print employee details using format specifiers
    // %d for int, %f for float, %s for string
    printf("%d %f %s", e1.code, e1.salary, e1.name);

    return 0; // Exit the program
}
