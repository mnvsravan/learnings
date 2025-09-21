#include <stdio.h>
#include <string.h> // needed for strcpy

// Define a structure to represent an employee
struct employee {
    int code;       // employee code (unique ID)
    float salary;   // employee salary
    char name[50];  // employee name (string)
};

int main() {
    // Declare an array of 100 employees
    struct employee instagram[100];

    // Assign employee codes to the first two employees
    instagram[0].code = 100;  // code for employee 1
    instagram[1].code = 77;   // code for employee 2

    // Example: printing them
    printf("Employee 1 code: %d\n", instagram[0].code);
    printf("Employee 2 code: %d\n", instagram[1].code);

    // Create another employee "sravan"
    struct employee sravan;
    sravan.code = 101;
    sravan.salary = 550000000000.00;
    strcpy(sravan.name, "Sravan");  // assign a string to the name field

    // Print details of sravan
    printf("Sravan's code: %d\n", sravan.code);
    printf("Sravan's salary: %.2f\n", sravan.salary);
    printf("Sravan's name: %s\n", sravan.name);
    struct employee eugb = {100, 77.12, "Sravan"};
    printf("Eugb - Code: %d, Salary: %.2lf, Name: %s\n", eugb.code, eugb.salary, eugb.name);



    return 0; // end of program
}
 // we can express in so many ways
