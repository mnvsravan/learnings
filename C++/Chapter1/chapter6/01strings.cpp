#include<iostream>
#include<string>
using namespace std;
int main(){
char str[]={'a','f','g','l','\0'};
cout<<str;
cout<<"\n";
cout<<str[3];

//Better is string class, this is most used
// for input we do getline(cin,name,delim) delim is like where to stop
string str1;
getline(cin,str1,'.'); // for input

string str2="Hello mate";
cout<< str1+str2;
cout << (str1 > str2);
cout << (str1 == str2);

// we cannot change char arrays stuff but we can change string
str2="Yoyo";
cout<<str2;
cout<<str2.length();

// reverse a string
// use inlucde algo do like vector only 
// or do start =0 , end= length-1 and start<=end swap both and end-- start++;












}