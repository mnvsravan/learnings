#include <stdio.h>   // Standard Input/Output header file

// Function to calculate the length of a string
int strlen(char str[]) {  
    int i = 0, count;        // Declare integer variables i (for index) and count (for length)
    char c = str[i];         // Initialize character c with the first element of string
    
    // Loop until null character '\0' is encountered
    while (c != '\0') {      
        c = str[i];          // Update c with current character
        i++;                 // Move to next index
    }
    
    count = i - 1;           // Length = total iterations - 1
    return count;            // Return the calculated length
}

int main() {
    char str[] = "MNV SRAVAN";               // Declare and initialize string with "MNV SRAVAN"
    
    printf("%d", strlen(str));          // Call strlen() function and print the result
    
    return 0;                           // Indicate successful execution
}

 // IF YOU DONT WANT FUCNTION THEN USE 
  // #include <stdio.h>   // Standard Input/Output header file

//int main() {
  //  char str[] = "Harry";   // Declare and initialize string with "Harry"
   // int i, length = 0;      // i for loop index, length to count characters

    //// Loop through each character until '\0' is found
    //for (i = 0; str[i] != '\0'; i++) {
      //  length++;           // Increase count for each character
    //}

    //// Print the length of the string
    //printf("%d", length);   // length = 5 for "Harry"

    //return 0;   // Indicate successful execution
//}
