#include <stdio.h>

int main() {
    char name1[50], name2[50];  // arrays for employee names
    int salary1, salary2;       // salaries
    FILE *ptr;                  // file pointer

    ptr = fopen("employee.txt", "w");  // open file for writing
    if (ptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Employee 1 input
    printf("Enter the name of Employee 1\n");
    scanf("%s", name1);

    printf("Enter the salary of Employee 1\n");
    scanf("%d", &salary1);

    // Employee 2 input
    printf("Enter the name of Employee 2\n");
    scanf("%s", name2);

    printf("Enter the salary of Employee 2\n");
    scanf("%d", &salary2);

    // Write Employee 1 data
    fprintf(ptr, "%s ", name1);
    fprintf(ptr, "%d", salary1);
    fprintf(ptr, "\n");

    // Write Employee 2 data
    fprintf(ptr, "%s ", name2);
    fprintf(ptr, "%d", salary2);
    fprintf(ptr, "\n");

    fclose(ptr);  // close file

    printf("Data written successfully to employee.txt\n");

    return 0;
}
