#include <stdio.h>   // Standard Input/Output header file

// Function to slice a string from index m to n
char* slice(char str[], int m, int n) { // here we give m and n cuz we need to slice 
    int i = 0;                        // counter variable
    char* ptr1 = &str[m];              // pointer to starting index (m)
    char* ptr2 = &str[n];              // pointer to ending index (n)

    str = ptr1;                        // make str point to the start position
    

    *ptr2 = '\0';                      // put null character at position n to terminate string
    
    return str;                        // return the new substring (starting from m up to n-1)
}

int main() {
    char str[] = "MNV SRAVAN";         // original string
    
    // slice from index 1 to 5 (indexes start at 0)
    // "Harry bhai" -> substring is "arry"
    printf("%s", slice(str, 1, 5));   
    
    return 0;   // successful execution
}
 // like this 1 and 5 will get elminated and the things between them will be output
 // if we make *ptr 1 also zero then ntg shows 