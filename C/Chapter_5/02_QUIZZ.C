#include <stdio.h>

void goodMorning();
void goodEvening();         // Function prototypes
void goodAfternoon();

void goodMorning() {                            // Function definitions

    printf("Good Morning Bro\n");
}
void goodEvening() {                                    
    printf("Good Evening Bro\n");
}
void goodAfternoon() {
    printf("Good Afternoon Bro\n");
}
int main() {
goodMorning();
goodAfternoon();                  // gives the output in sequence
goodEvening();

    return 0;
}
