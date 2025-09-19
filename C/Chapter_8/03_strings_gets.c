#include <stdio.h>

int main() {
    char st[30];
    gets(st);
    
    printf("%s",st);

    return 0;
} // this gets is unsafe in projects usually so use fgets 
 // #include <stdio.h>

//int main() {
  //  char st[30];

    /////// fgets(string, size, stdin) - safe input this is comment
    //fgets(st, sizeof(st), stdin);

    //printf("%s", st);

    //return 0;
//}
