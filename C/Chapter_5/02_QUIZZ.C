#include <stdio.h>

void goodMorning();
void goodEvening();         // Function prototypes
void goodAfternoon();


int main() {
goodMorning();
goodAfternoon();                  // gives the output in sequence
goodEvening();

    return 0;
}
void goodMorning() {                            // Function definitions

    printf("Good Morning Bro\n");
}
void goodEvening() {                                    
    printf("Good Evening Bro\n");
}
void goodAfternoon() {
    printf("Good Afternoon Bro\n");
}
