#include <stdio.h>   // For printf
#include <string.h>  // For strlen

int main() {
    // Encrypted string (example): After original was shifted by +1
    // Let's say the encrypted version is what we want to decrypt:
    char str[] = "Nfsb!qj[[b!lb!mbtu!tmjdf!hibs!qf!ibj";

    // Loop through each character of the string
    for (int i = 0; i < strlen(str); i++) {
        // Subtract 1 from each character’s ASCII value
        str[i] = str[i] - 1;
    }

    // Print the decrypted string
    printf("%s", str);

    return 0;
}

 // see 09.strings