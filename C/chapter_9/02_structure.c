#include <stdio.h>

// Define a structure to represent an employee
struct employee {
    int code;       // employee code (unique ID)
    float salary;   // employee salary
    char name[50];  // employee name (string)
};

int main() {
    // Declare three employee variables
    struct employee e1, e2, e3;

    // -------- Employee 1 Input --------
    printf("Enter the value of code\n");
    scanf("%d", &e1.code);  // input code for employee 1

    printf("Enter the value of salary\n");
    scanf("%f", &e1.salary);  // input salary for employee 1

    printf("Enter the value of name\n");
    scanf("%s", e1.name);  // input name for employee 1 (string input)

    // Print employee 1 details
    printf("%d %.2f %s\n", e1.code, e1.salary, e1.name);


    // -------- Employee 2 Input --------
    printf("Enter the value of code\n");
    scanf("%d", &e2.code);  // input code for employee 2

    printf("Enter the value of salary\n");
    scanf("%f", &e2.salary);  // input salary for employee 2

    printf("Enter the value of name\n");
    scanf("%s", e2.name);  // input name for employee 2

    // Print employee 2 details
    printf("%d %.2f %s\n", e2.code, e2.salary, e2.name);


    // -------- Employee 3 Input --------
    printf("Enter the value of code\n");
    scanf("%d", &e3.code);  // input code for employee 3

    printf("Enter the value of salary\n");
    scanf("%f", &e3.salary);  // input salary for employee 3

    printf("Enter the value of name\n");
    scanf("%s", e3.name);  // input name for employee 3

    // Print employee 3 details
    printf("%d %.2f %s\n", e3.code, e3.salary, e3.name);

    return 0; // end of program
}
