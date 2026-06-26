// its same like C only
#include <iostream>
using namespace std;
double sum(double starting, double ending)
{
    double sum=0;
    for(double i=starting; i<=ending; i++)
    {
        sum+=i;
    }
    return sum;
}
int factorial(int n)
{
    int fact=1;
    for(int i=1; i<=n; i++)
    {
        fact*=i;
    }
    return fact;
}
int sumDigits(int n){
    int sum=0;
    while(n>0){
 sum=sum+n%10;
 n=n/10;
    }
    return sum;
}
int ncr(int n, int r){
    int fact_n=factorial(n);
    int fact_r=factorial(r);
    int fact_n_r=factorial(n-r);
    return fact_n/(fact_r*fact_n_r);
}

int main(){

    double result = sum(18.5, 108.67);
    cout<<"Sum is: "<<result<<endl;
    int fact_result = factorial(5);
    cout<<"Factorial is: "<<fact_result<<endl;
    int digit_sum = sumDigits(12345);
    cout<<"Sum of digits is: "<<digit_sum<<endl;
    int combination = ncr(5, 2);
    cout<<"Combination is: "<<combination<<endl;
    return 0;
}