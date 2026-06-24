#include <iostream>
using namespace std;
int main()
{
    //1
    int num;
    cout << "Enter The Number: ";
    cin >> num;

    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num; j++){
            cout << j << " ";
        }
        cout << endl;
    }

    //2
     int num1;
    cout << "Enter The Number: ";
    cin >> num1;

    for(int i = 1; i <= num1; i++){
        char ch='A';
        for(int j = 1; j <= num1; j++){
            cout << ch << " ";
            ch++;
        }
        cout << endl;
    }
 //3
  int num3;
    cout << "Enter number of rows: ";
    cin >> num3;

    int k = 1;

    for(int i = 1; i <= num3; i++)
    {
        for(int j = 1; j <= 3; j++)
        {
            cout << k;
            k++;
        }
        cout << endl;
    }
    //4

     int n;
    cout << "Enter number: ";
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
       for(int k=1;k<=n+i-n;k++){
           cout<<"*"<<" ";
       }
       cout<<"\n";
    }
    //5
     int n;
    cout << "Enter number: ";
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        int o=1;
       for(int k=1;k<=n+i-n;k++){
           cout<<o<<" ";
           o++;
       }
       cout<<"\n";
    }
    //6

       int n;
    cout << "Enter number: ";
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        for(int k = 1; k <= n+i-n; k++)
        {
            cout << i-k+1;
        }
        cout << "\n";
    }
    //7
      int n;
    cout << "Enter number: ";
    cin >> n;

   for(int i=n; i>=1; i--)
{
    for(int s=0; s<n-i; s++)
    {
        cout<<" ";
    }

    for(int k=1; k<=n+i-n; k++)
    {
        cout<<n-i+1; // if we add << " " then it will print space between numbers like pyramid
    }

    cout<<"\n";

    //8
       int n;
    cout << "Enter number: ";
    cin >> n;

    for(int i=n; i>0; i--)
    {
        int j;

        for(int s=1; s<i; s++)
        {
            cout << "  ";
        }

        for(j=1; j<=n+1-i; j++)
        {
            cout << j << " ";
        }

        for(int l=j-2; l>=1; l--)
        {
            cout << l << " ";
        }

        cout << "\n";
    }

    //9
      int n;
    cin >> n;

    // Upper half
    for(int i=n; i>0; i--)
    {
        int j;

        for(int s=1; s<i; s++)
        {
            cout << "  ";
        }

        for(j=1; j<=n+1-i; j++)
        {
            if(j==1)
                cout << "* ";
            else
                cout << "  ";
        }

        for(int k=j-2; k>=1; k--)
        {
            if(k==1)
                cout << "*";
            else
                cout << "  ";
        }

        cout << "\n";
    }

    // Lower half (same syntax)
    for(int i=2; i<=n; i++)
    {
        int j;

        for(int s=1; s<i; s++)
        {
            cout << "  ";
        }

        for(j=1; j<=n+1-i; j++)
        {
            if(j==1)
                cout << "* ";
            else
                cout << "  ";
        }

        for(int k=j-2; k>=1; k--)
        {
            if(k==1)
                cout << "*";
            else
                cout << "  ";
        }

        cout << "\n";
    }
}


//10


int n;
    cin >> n;

    // Upper half
    for(int i=n;i>=1;i--)
    {
        for(int k=1;k<=n-i+1;k++)
        {
            cout<<"* ";
        }

        for(int s=1;s<=2*(i-1);s++)
        {
            cout<<"  ";
        }

        for(int k=1;k<=n-i+1;k++)
        {
            cout<<"* ";
        }

        cout<<"\n";
    }

    // Lower half
    for(int i=n;i>=1;i--)
    {
        for(int k=n-i+1;k<=n;k++)
        {
            cout<<"* ";
        }

        for(int s=1;s<=2*(n-i);s++)
        {
            cout<<"  ";
        }

        for(int k=n-i+1;k<=n;k++)
        {
            cout<<"* ";
        }

        cout<<"\n";
    }
























































    return 0;
    
}