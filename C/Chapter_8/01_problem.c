#include <stdio.h>   // include standard input-output library for printf, scanf

int main() {         
    char str[6];     // declare a character array of size 6 (5 chars + 1 '\0')

    // scanf("%s", str); 
    // this is commented because we are reading character by character instead

    for (int i = 0; i < 5; i++) {   // loop runs 5 times (i = 0 to 4)
        scanf("%c", &str[i]);      // read a single character and store in str[i]
        // fflush(stdin);          // (commented) - not standard, should not be used
    }

    str[5] = '\0';   // manually add string terminator '\0' at the end of array
                     // this makes str a proper C-string

    printf("%s", str);   // print the string entered by the user

    return 0;       // end of program
}
 // arey it the string starts from 0 to goes till 5 so all strings are  used EG 
 //str[0] = 'H'

//str[1] = 'e'

//str[2] = 'l'

//str[3] = 'l'

//str[4] = 'o'

//str[5] = '\0'
// but for ez way we use ( after that char [] 6)
// scanf("%s",st)
// printf ( "%s",st) thats it

