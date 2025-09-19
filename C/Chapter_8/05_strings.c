#include <stdio.h>
#include <string.h>

int main() {
    // Correct way: use a char array for a string
    char st[] = "Sravan";  // compiler automatically adds '\0' at the end

    printf("%d", strlen(st)); // prints number of characters (without '\0')

    return 0;
}
