#include <stdio.h>   // Required for file handling functions: fopen, fscanf, fprintf, fclose

int main() {
    FILE *ptr;   // File pointer used to open/read/write files
    int num;     // Variable to store integer read from the file

    // Step 1: Open the file in read mode ("r")
    ptr = fopen("int.txt", "r");  
    // "r" = read mode → file must already exist, otherwise fopen will return NULL

    fscanf(ptr, "%d", &num);  
    printf("The number read from file is: %d\n", num);
    // Read an integer from the file and store it in variable 'num'
    // Example: if int.txt contains 5 → num = 5

    fclose(ptr);  
    // Close the file after reading to free resources and avoid data corruption

    // Step 2: Open the same file again, but this time in write mode ("w")
    ptr = fopen("int.txt", "w");  
    // "w" = write mode → creates new empty file OR erases existing contents

    fprintf(ptr, "%d", 2 * num); 
    printf("Wrote %d to the file.\n", 2 * num); 
    // Write double the value of 'num' into the file
    // Example: if num was 5 → writes 10 into int.txt

    fclose(ptr);  
    // Close the file after writing to ensure data is saved properly

    return 0;  
    // Program ends successfully
}
