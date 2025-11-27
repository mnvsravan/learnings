#include <stdio.h>   // Required for printf
#include <string.h>  // Required for strcpy

// typedef = keyword in C used to give a nickname (alias) to an existing type
// Here we define a structure 'employee' and give it the alias 'Emp'
typedef struct
{
    int code;        // employee code (integer ID)
    float salary;    // employee salary
    char name[10];   // employee name (string up to 9 chars + '\0')
} Emp; // now instead of writing 'struct employee', we can just use 'Emp'

int main()
{
    // Declare a variable 'e1' of type Emp (same as struct employee)
    Emp e1;

    // Declare a pointer to Emp and assign it the address of e1
    Emp *ptr = &e1;   // we can directly write in one line

    // Assign values using pointer (ptr-> is same as (*ptr).field)
    ptr->code = 4511;               // set employee code
    strcpy(ptr->name, "Harry");     // copy string "Harry" into name
    ptr->salary = 54.44;            // set employee salary

    // Print employee details using pointer
    printf("Code   : %d\n", ptr->code);
    printf("Name   : %s\n", ptr->name);
    printf("Salary : %.2f\n", ptr->salary);

    return 0; // end of program
}
