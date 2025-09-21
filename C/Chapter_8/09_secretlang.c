#include <stdio.h>   // Standard Input/Output library for printf
#include <string.h>  // String library for strlen

int main() {
    // Declare and initialize a character array (string)
    // This string is in Hindi + English: "Mera pizza ka last slice ghar pe hai"
    char str[] = "Mera pizza ka last slice ghar pe hai";

    // Loop through each character in the string using strlen to get length
    for (int i = 0; i < strlen(str); i++) {
        // Increment the ASCII value of each character by 1
        // For example: 'a' becomes 'b', 'z' becomes '{', ' ' becomes '!'
        str[i] = str[i] + 1;
    }

    // Print the modified string
    // The result will be a weird-looking string because all characters are shifted
    printf("%s", str);

    // Return 0 to indicate successful execution
    return 0;
}
