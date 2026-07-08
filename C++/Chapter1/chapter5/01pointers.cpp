#include<iostream>
using namespace std;
// Just like C only
void swapUsingPointers(int* x, int* y){
    int temp=*x;
    *x=*y;
    *y=temp;
}
void swapUsingAliases(int& x, int& y){
    int temp=x;
    x=y;
    y=temp;
}
int main(){
int a=10;
int* ptr=&a; // pointer variable ptr is storing the address of a
int** ptr2=&ptr; // pointer to pointer variable ptr2 is storing the address of ptr
cout<<"The value of a is: "<<a<<endl;
cout<<"The address of a is: "<<ptr<<endl;
cout<<"The value of a using pointer is: "<<*ptr<<endl;
cout<<"The address of pointer ptr is: "<<ptr2<<endl;
cout<<"The value of a using pointer to pointer is: "<<**ptr2<<endl;

// we can do pass by reference in two ways first is using pointers and second is aliases
int x=5, y=10;
int x1=5, y1=10;
cout<<"Before swapping: x="<<x<<", y="<<y<<endl;
swapUsingPointers(&x, &y);
cout<<"After swapping using pointers: x="<<x<<", y="<<y<<endl;
swapUsingAliases(x1, y1);
cout<<"After swapping using aliases: x="<<x1<<", y="<<y1<<endl;

//Array pointers are constant pointers because the address of the first element of the array is fixed and cannot be changed
int arr[5]={1,2,3,4,5};
int* ptr10=arr; // pointer variable ptr is storing the address of first element of arr
cout<<"The value of first element of arr is: "<<*ptr10<<endl;
// pointer arithmetic
cout<<"The value of second element of arr is: "<<*(ptr10+1)<<endl;// cuz +1 increases the address by sizeof(int) which is 4 bytes in most systems
ptr10++; // now ptr10 is pointing to the second element of arr
cout<<"The value of second element of arr is: "<<*ptr10<<endl;
ptr10--; // now ptr10 is pointing to the first element of arr
cout<<"The value of first element of arr is: "<<*ptr10<<endl;
//we cannot add ptrs but we can subtract them to get the number of elements between them
cout<<"The number of elements between ptr10 and arr is: "<<ptr10-arr<<endl; // like if the difference is 4 it means 1 element is between them because the difference is in bytes and sizeof(int) is 4 bytes in most systems
ptr10+=2; // now ptr10 is pointing to the third element of arr

//we can compare pointers using relational operators
if(ptr10>arr){
    cout<<"ptr10 is pointing to an element after arr"<<endl;
    cout<<"The value of third element of arr is: "<<*ptr10<<endl;
}
else{
    cout<<"ptr10 is pointing to an element before arr"<<endl;
}










































return 0;
}


