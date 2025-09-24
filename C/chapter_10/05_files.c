#include <stdio.h>  
// Includes the standard input-output library, necessary for using functions like printf, fopen, fgetc, etc.

int main()  
// Entry point of the C program. Execution starts from here.
{
    char ch;  
    // Declares a variable 'ch' of type char to store each character read from the file.

    FILE *ptr;  
    // Declares a pointer 'ptr' to a FILE object, used to refer to the file.

    ptr = fopen("harry.txt", "r");  
    // Opens the file "harry.txt" in read mode ("r").
    // 'fopen' returns a pointer to the file, which is assigned to 'ptr'.
    // If the file does not exist or cannot be opened, 'ptr' will be NULL.

    while (1)  
    // Starts an infinite loop that will keep reading characters until broken manually.
    {
        ch = fgetc(ptr);  
        // Reads a single character from the file pointed to by 'ptr' and stores it in 'ch'.
        // fgetc returns an int, but here it's stored in a char (this works unless EOF is misinterpreted).

        printf("%c", ch);  
        // Prints the character stored in 'ch' to the standard output.

        // Check if the end of file (EOF) has been reached
        if (ch == EOF)  
        {
            break;  
            // If EOF is encountered, exit the loop.
        }
    }

    return 0;  
    // Returns 0 from the main function, indicating successful execution.
} // for using FOR LOOP
 //#include <stdio.h>  
// Includes the standard input-output library, necessary for functions like printf, fopen, fgetc, etc.

//int main()  
// Entry point of the C program. Execution starts from here.
//{
  //  int ch;  
    // Use int instead of char, because fgetc() returns int to properly handle EOF (-1).
//
 //  FILE *ptr;  
  //  // Declares a pointer 'ptr' to a FILE object, used to refer to the file.

    //ptr = fopen("harry.txt", "r");  
    // Opens the file "harry.txt" in read mode ("r").
    // If the file cannot be opened, 'ptr' will be NULL.

    //if (ptr == NULL) {
       // printf("File could not be opened.\n");
       // return 1;  
        // Exit with an error code if file opening fails.
   // }

    // Use a for loop to read until EOF
   // for (ch = fgetc(ptr); ch != EOF; ch = fgetc(ptr))  
    //{
      //  printf("%c", ch);  
        // Prints the character read from the file.
    //}

    //fclose(ptr);  
    // Close the file after reading to free system resources.

    //return 0;  
    // Return 0 to indicate successful execution.
///}
//he first fgetc(ptr) → initializes ch before the loop begins.

//The second fgetc(ptr) → fetches the next character at the end of each iteration
