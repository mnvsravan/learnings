#include <stdio.h>

int main() {
    int num, a;
    a = 4;

    FILE *fptr;
    fptr = fopen("file.txt", "w");

    // Print multiplication table of 'a'
    for (int i = 1; i <= 10; i++) {
        fprintf(fptr, "%d x %d = %d\n", a, i, a * i);
        // Example: "4 x 1 = 4"
    }

    fclose(fptr);
    return 0;
}

