#include<iostream>
#include <vector>
#include<algorithm>
using namespace std;

bool custom(pair<int,int> p, pair<int,int> p1) {

    if (p.second < p1.second) {
        return true;
    }
     if (p.second > p1.second) {
        return false;
    }
    if (p.first > p1.first) {
        return false;
    }
    if (p.first < p1.first) {
        return true;
    }
}

int main(){
// sorting
vector<int>vec={1,2,3,4,64,25,2663,34,2265,43};
sort(vec.begin(),vec.end());
for(int val: vec){
    cout<<val<<" ";
}

// if u want any customiation of sorting like see below
vector<pair<int,int>> vec1 = {{3,2}, {1,7}, {6,3}};

sort(vec1.begin(), vec1.end(), custom);
cout<<"\n";
for (auto val : vec1) {
    cout << val.first << " " << val.second << endl;
}

// Reverse

vector<int>vec2={1,2,3,4,64,25,2663,34,2265,43};
reverse(vec2.begin(),vec2.end());
// reverse(vec2.begin()+3,vec2.end()+5); we can do like this also
for (int val : vec2) {
    cout << val<<" ";
}



cout<<"\n";
// next permuation and prev
vector<int>vec3={1,2,3};
next_permutation(vec3.begin(),vec3.end()); // same we can do for prev_permuatation
for (int val : vec3) {
    cout << val<<" ";
}


//U ALREADY KNOW SWAP AND MIN AND MAX
// we cam use binary search like this binary_search(v.begin,v.end,target)



// __builtin_popcount() is a GCC/Clang built-in function that counts the number of 1's (set bits) in the binary representation of an integer.
 int x = 13;
cout<<"\n";
    cout << __builtin_popcount(x); // if we use long int then __builtin_popcountl
                                   // if we use long long int then __builtin_popcountll
}