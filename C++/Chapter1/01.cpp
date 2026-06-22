#include<iostream>
using namespace std;
int main()
{
    cout << "Hello World!" << endl;
    // or
    cout<< "This is my first C++ program.\n";
    // or
    cout<< "I am learning C++ programming language.\n"<< "I will become a good C++ programmer.\n";
    //or
    cout<< "I am learning C++ programming language."<< "I will become a good C++ programmer.\n";

// Variables and Constants
int a=10;
const float pi=3.14;
float radius=5.0;
float area=pi*radius*radius;
bool nameIsValid=true;
char grade='A';
double largeNumber=1.23456789;
cout << "Area of the circle: " << area << endl;
cout << "Large number: " << largeNumber << endl;
cout<<"The ascii value of grade "<<grade<<" is "<<int(grade)<<endl;
cout<<"division is"<< float(a)/3<<endl; // type casting



// INPUT
int num1, num2;
cout << "Enter two numbers: "<<endl;
cin >> num1 >> num2;
cout << "You entered: " << num1 << " and " << num2 << endl;
float multi;
multi=num1*num2;
cout<<"The multiplication of "<<num1<<" and "<<num2<<" is "<<multi<<endl;

//OPERATORS
int sum=num1+num2;
int diff=num1-num2;
int product=num1*num2;
float quotient=float(num1)/num2; // type casting
cout<<"The sum of "<<num1<<" and "<<num2<<" is "<<sum<<endl;
cout<<"The difference of "<<num1<<" and "<<num2<<" is "<<diff<<endl;
cout<< "The product of "<<num1<<" and "<<num2<<" is "<<product<<endl;
cout<<"The quotient of "<<num1<<" and "<<num2<<" is "<<quotient<<endl;

//COMPARISON OR RELATIONSAL OPERATORS
cout<<"Is num1 greater than or equal to num2? "<<(num1>=num2)<<endl;
cout<<"Is num1 less than or equal to num2? "<<(num1<=num2)<<endl;
cout<<"Is num1 equal to num2? "<<(num1==num2)<<endl;
cout<<"Is num1 not equal to num2? "<<(num1!=num2)<<endl;

//LOGICAl OPERATORS
cout<<"Is num1 greater than 0 AND num2 greater than 0? "<<((num1>0) && (num2>0))<<endl;
cout<<"Is num1 greater than 0 OR num2 greater than 0? "<<((num1>0) || (num2>0))<<endl;
cout<<"Is num1 NOT greater than 0? "<<!(num1>0)<<endl;


//UNARY OPERATORS
cout<<"The value of num1 is "<<num1<<endl;
cout<<"The value of num1 after increment is "<<++num1<<endl; // pre-increment
cout<<"The value of num1 after decrement is "<<--num1<<endl; // pre-decrement like it decreases but dosent print
cout<<"The value of num1 after post-increment is "<<num1++<<endl;  // post-increment
cout<<"The value of num1 after post-decrement is "<<num1--<<endl;// post-decrement

    return 0;
}

