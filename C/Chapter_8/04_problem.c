#include <stdio.h>     // Header file for standard input/output functions like printf
#include <string.h>    // Header file that contains strlen (to calculate string length)

// Function to copy one string into another (like strcpy)
void mystrcpy(char target[], char source[]) {

    // Loop through each character of source until its length
    for (int i = 0; i < strlen(source); i++) {
        target[i] = source[i];   // Copy character from source[i] to target[i]
    }

    // After copying all characters, add null character '\0' at the end
    // This ensures target string is properly terminated
    target[strlen(source)] = '\0';
}

int main() {
    char source[] = "SRAVAN";   // Declare and initialize source string
    char target[30];           // Declare target string with enough space (30 chars)

    mystrcpy(target, source);  // Call function to copy source into target

    // Print both source and target strings
    // Output will show: SRAVAN SRAVAN
    printf("%s %s", source, target);

    return 0;   // Return 0 → successful program execution
}
