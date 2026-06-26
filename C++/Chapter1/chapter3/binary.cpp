#include<iostream>
using namespace std;
int convertBinaryToDecimal(int n){
    int decimal=0, pow=1, remainder;
    while(n!=0){
        remainder=n%10;
        n/=10;
        decimal+=remainder*pow;
        pow*=2;
    }
    return decimal;
}
int convertDecimalToBinary(int n){
    int binary=0, pow=1, remainder;
    while(n!=0){
        remainder=n%2;
        n/=2;
        binary+=remainder*pow;
        pow*=10;
    }
    return binary;
}
int twosComplement(int n){
    int onesComplement=0, pow=1, remainder;
    while(n!=0){
        remainder=n%10;
        n/=10;
        if(remainder==0)
            remainder=1;
        else
            remainder=0;
        onesComplement+=remainder*pow;
        pow*=10;
    }
    return onesComplement+1;
}




int main(){
    int binary, decimal;
    cout<<"Enter a binary number: ";
    cin>>binary;
    decimal=convertBinaryToDecimal(binary);
    cout<<"Decimal equivalent: "<<decimal<<endl;

    cout<<"Enter a decimal number: ";
    cin>>decimal;
    binary=convertDecimalToBinary(decimal);
    cout<<"Binary equivalent: "<<binary<<endl;
    cout<<"Two's complement: "<<twosComplement(binary)<<endl;

    return 0;
}