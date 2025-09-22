#include <stdio.h>  
// This is a preprocessor directive that tells the compiler to include the 
// Standard Input Output library before compilation. 
// It is needed here because we are using printf() function for output.

struct vector{  
    int i;  // Declares an integer member 'i' of the structure
    int j;  // Declares an integer member 'j' of the structure
};  
// This defines a user-defined data type called 'struct vector' which groups
// together two integers 'i' and 'j'. This allows us to represent a vector (i, j).

int main(){  
    // Entry point of the program, execution starts here.

    struct vector v = {1, 2};  
    // Declare a variable 'v' of type 'struct vector'.
    // Initialize it with values {1, 2}.
    // So, v.i = 1 and v.j = 2.

    printf("The value of vector is %di + %d j", v.i, v.j);  
    // printf is used to print output to the screen.
    // The format string "The value of vector is %di + %d j" contains placeholders:
    //    %d → expects an integer value.
    //    v.i (1) will replace the first %d.
    //    v.j (2) will replace the second %d.
    // Output will be: "The value of vector is 1i + 2 j"

    return 0;  
    // Returns 0 to the operating system, indicating successful execution of the program.
}
