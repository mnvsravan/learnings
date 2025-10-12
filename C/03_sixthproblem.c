#include <stdio.h>

int* sum(int a, int b){ // we use int* to return address of integer
    int s = a+b;
    int* ptr3= &s;             // we are using pointer to hold address of s
    printf("The sum is %d\n", s);
    return ptr3;                 // we use return &s; also it will work the same way
}

float* average(int a, int b){
    float avg = (a+b)/2.0;
    float * ptr4=&avg;
    printf("The average is %f\n", avg);
    return ptr4;
}

int main(){
    int x = 4;
    int y = 6;
    int* ptr3;
    float* ptr4;

    ptr3 = sum(x,y); // we can also write just sum(x,y) and keep sum(int a, int b) as sum(int* a, int* b) and it will work the same way
    ptr4 = average(x,y);

    printf("The address of sum is %u and of average is %u", ptr3, ptr4 );
}
