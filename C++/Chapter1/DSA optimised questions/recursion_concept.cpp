#include <iostream>
using namespace std;

// 1. Print name n times
void printName(int i, int n) {
    if (i > n) return;

    cout << "Raj" << endl;

    printName(i + 1, n);
}


// 2. Print 1 to n linearly
void print1ToN(int i, int n) {
    if (i > n) return;

    cout << i << endl;

    print1ToN(i + 1, n);
}


// 3. Print n to 1 linearly
void printNTo1(int i, int n) {
    if (i < 1) return;

    cout << i << endl;

    printNTo1(i - 1, n);
}


// 4. Print 1 to n using Backtracking
void print1ToNBacktrack(int i, int n) {
    if (i < 1) return;

    print1ToNBacktrack(i - 1, n);

    cout << i << endl;
}


// 5. Print n to 1 using Backtracking
void printNTo1Backtrack(int i, int n) {
    if (i > n) return;

    printNTo1Backtrack(i + 1, n);

    cout << i << endl;
}


int main() {

    int n = 5;

    // 1. Name n times
    cout << "1. Print name n times:" << endl;
    printName(1, n);

    cout << endl;


    // 2. 1 to n
    cout << "2. Print 1 to n linearly:" << endl;
    print1ToN(1, n);

    cout << endl;


    // 3. n to 1
    cout << "3. Print n to 1 linearly:" << endl;
    printNTo1(n, n);

    cout << endl;


    // 4. 1 to n using backtracking
    cout << "4. Print 1 to n using backtracking:" << endl;
    print1ToNBacktrack(n, n);

    cout << endl;


    // 5. n to 1 using backtracking
    cout << "5. Print n to 1 using backtracking:" << endl;
    printNTo1Backtrack(1, n);

    return 0;
}