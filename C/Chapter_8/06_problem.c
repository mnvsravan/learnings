#include <stdio.h>    // For input/output functions
#include <string.h>   // For strlen() function

int main() {
    // Character to search for
    char c = 'r';

    // Flag to indicate if character is found; 0 = not found, 1 = found
    int contains = 0;

    // String to search in
    char str[] = "Harry";

    // Loop through each character of the string
    for (int i = 0; i < strlen(str); i++) {
        // Check if current character matches 'c'
        if (str[i] == c) {
            contains = 1;   // Set flag to true
            break;       // Exit the function early since character is found
        }
    }

    // Check the flag and print result
    if (contains) {
        printf("Yes it contains\n");
    } else {
        printf("Does not contain\n");
    }

    return 0;   // Indicate successful program termination
}
