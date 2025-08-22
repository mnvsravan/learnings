#include <stdio.h>

int main() {
    int grade=67;
    char a;
    char b;
    char c;
    char d;
    char e;
    char f;
if(grade>90){
    printf("You got an A.\n");
} else if(grade>80) {
    printf("You got a B.\n");
} else if(grade>70) {
    printf("You got a C.\n");  
} else if(grade>60) {
    printf("You got a D.\n"); 
} else if(grade>=0) { 
    printf("You got an F.\n");
} else {
    printf("Invalid grade.\n"); 
}
return 0;
}
// or use && also like this:grade>=90 && grade <100
    
