#include<iostream>
#include<set>
#include<unordered_set>
using namespace std;

int main() {

    set<int> S;

    // insert()
    S.insert(30);
    S.insert(10);
    S.insert(20);
    S.insert(40);
    S.insert(20);   // Duplicate (Ignored)

    // Traversing using range-based loop
    cout << "Elements: ";
    for (auto i : S) {
        cout << i << " ";
    }
    cout << endl;

    // Traversing using iterator
    cout << "Using Iterator: ";
    for (auto it = S.begin(); it != S.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    // begin()
    cout << "First Element: " << *S.begin() << endl;

    // rbegin()
    cout << "Last Element: " << *S.rbegin() << endl;

    // size()
    cout << "Size: " << S.size() << endl;

    // empty()
    cout << "Empty: " << S.empty() << endl;

    // count()
    cout << "Count of 20: " << S.count(20) << endl;
    cout << "Count of 100: " << S.count(100) << endl;

    // find()
    auto it = S.find(30);

    if (it != S.end())
        cout << "30 Found" << endl;
    else
        cout << "30 Not Found" << endl;

    // lower_bound()
    auto lb = S.lower_bound(25); // gives the value or nearest above it

    if (lb != S.end())
        cout << "Lower Bound of 25: " << *lb << endl;

    // upper_bound()
    auto ub = S.upper_bound(20); // gives the value nearest above it       // like a a b b b c c d , 1st b is lowerB,1st c is upperB if we do upperB(b) or lower

    if (ub != S.end())
        cout << "Upper Bound of 20: " << *ub << endl;

    // erase()
    S.erase(20);

    cout << "After Erase: ";
    for (auto i : S) {
        cout << i << " ";
    }
    cout << endl;

    // swap()
    set<int> S1 = {1, 2, 3};

    S.swap(S1);

    cout << "After Swap (S): ";
    for (auto i : S) {
        cout << i << " ";
    }
    cout << endl;

    cout << "After Swap (S1): ";
    for (auto i : S1) {
        cout << i << " ";
    }
    cout << endl;

    // clear()
    S.clear();

    cout << "After Clear, Size: " << S.size() << endl;

    // empty()
    cout << "Is Empty: " << S.empty() << endl;



// MULTISET
multiset<int> MS;
MS.insert(10);
MS.insert(20);
MS.insert(20);
MS.insert(30);

for(auto i : MS){
    cout << i << " ";
}



/// Unordered

unordered_set<int> US;
US.insert(10);
US.insert(20);
US.insert(30);

for(auto i : US){
    cout << i << " ";
}























    return 0;
}