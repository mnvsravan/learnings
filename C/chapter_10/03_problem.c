#include <stdio.h>

int main() {
    int ch;            
    FILE *ptr, *ptr2;

    ptr = fopen("harry.txt", "r");   // open source file for reading
    ptr2 = fopen("harry3.txt", "a"); // open destination file in append mode

    if (ptr == NULL || ptr2 == NULL) {
        printf("Error opening file!\n");
        return 1; 
    }

    // for loop to read each character until EOF
    for (ch = fgetc(ptr); ch != EOF; ch = fgetc(ptr)) {
        // Write each character twice with no space
        fprintf(ptr2, "%c%c", ch, ch);  
        printf("%c%c", ch, ch);         
    }

    fclose(ptr);   
    fclose(ptr2);  

    return 0; 
}


