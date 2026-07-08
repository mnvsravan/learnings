#include<iostream>
using namespace std;
int sum(int &a, int &b, int &c){
   return c=a+b;
}
void swap(int &a, int &b){
    int temp=a;
    a=b;
    b=temp;
}
void multiply(int &a, int &b, int &c){
    c=a*b;
}
int main(){
    int x=5, y=10, z;
    cout<<"The sum of "<<x<<" and "<<y<<" is: "<<sum(x,y,z)<<endl;
    cout<<"The value of z is: "<<z<<endl; // z is passed by reference so its value is changed in the function

    swap(x,y);
    cout<<"After swapping: x="<<x<<", y="<<y<<endl;
    multiply(x,y,z);
    cout<<"The product of "<<x<<" and "<<y<<" is: "<<z<<endl;
    return 0;
}