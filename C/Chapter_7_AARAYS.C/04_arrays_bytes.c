#include <stdio.h>

int main() {
 int a=5;
 int *ptr= &a;
 printf("The adress of a is %u", &a);
 printf("the adress of a is %u", ptr);
 ptr++;
 printf("the adress of a is %u",ptr);

    return 0;
} // here the value increases by 4 cuz this is arrays btyes sspace storage so it not inc by only 1 
 // like if we use char it increase by only 1 
