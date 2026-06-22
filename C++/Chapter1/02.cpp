#include<iostream>
using namespace std;
int main()
{
    // CONDITIONAL STATEMENTS
    int a = 10;
    if(a > 5)
    {
        cout << "a is greater than 5" << endl;
    }
    else if(a == 5)
    {
        cout << "a is equal to 5" << endl;
    }
    else
    {
        cout << "a is less than 5" << endl;
    }



    char grade = 'B';
    if(grade>='A' && grade<='Z'){
        cout<<"UPPERCASE LETTER"<<endl;     // we can also use ascii number cuz charac is implicitly converted to int in comparison
    }
    else if(grade>='a' && grade<='z'){
        cout<<"LOWERCASE LETTER"<<endl;
    }
    else{
        cout<<"NOT A LETTER"<<endl;
    }

    // SWITCH STATEMENT
    int day = 4;
    switch(day)
    {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;
        default:
            cout << "Invalid day" << endl;
    }

    grade='C';
    switch(grade)
    {
        case 'A':
            cout << "Excellent" << endl;
            break;
        case 'B':
            cout << "Good" << endl;
            break;
        case 'C':
            cout << "Average" << endl;
            break;
        case 'D':
            cout << "Below Average" << endl;
            break;
        case 'F':
            cout << "Fail" << endl;
            break;
        default:
            cout << "Invalid grade" << endl;
    }


    //ternary operator
    int num1=10, num2=20;
    int max = (num1 > num2) ? num1 : num2;
    cout << "The maximum number is: " << max << endl;


//LOOP






//WHILE
    int count = 1;
    while(count <= 5)
    {
        cout << "Count: " << count << endl;
        count++;
    }
// FOR
    for(int i = 1; i <= 5; i++)
    {
        cout << "i: " << i << endl;
    }

    //SUM OF ODD NUMBER IN GIVEN RANGE
    int number;
    cout << "Enter a number: ";
    cin >> number;
    int sum = 0;
    for(int i = 1; i <= number; i++)
    {
        if(i % 2 != 0)
        {
            sum += i;
        }
    }
    cout << "The sum of odd numbers from 1 to " << number << " is: " << sum << endl;
    // using while loop
    int sum2 = 0;
    int j = 1;
    while(j <= number)
    {
        if(j % 2 != 0)
        {
            sum2 += j;
        }
        j++;
    }
    cout << "The sum of odd numbers from 1 to " << number << " is: " << sum2 << endl;






    // DO WHILE 
    int k = 1;
    do
    {
        cout << "k: " << k << " ";
        k++;
    } while(k <= 5);

    return 0;


// PRIME NUMBER WITH DO WHILE
int num;
    cin >> num;

    if(num <= 1){
        cout << num << " is not a prime number.";
        return 0;
    }

    bool isPrime = true;

    for(int i = 2; i < num; i++){
        if(num % i == 0){
            isPrime = false;
            break;
        }
    }

    if(isPrime)
        cout << num << " is a prime number.";
    else
        cout << num << " is not a prime number.";
        


    
// NESTED LOOPS
    for(int i = 1; i <= 3; i++)
    {
        for(int j = 1; j <= 3; j++)
        {
            cout << "i: " << i << ", j: " << j << endl;
        }
    }
return 0;
}
