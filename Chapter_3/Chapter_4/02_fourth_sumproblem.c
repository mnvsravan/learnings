#include <stdio.h>

int main() {
    int i=0;
    int sum=0;
    while(i<10){

    sum=sum+i;
    printf("The sum is %d\n",sum,i);
    i++;
    }
    

    return 0;  // should be after the loop
}
