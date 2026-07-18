#include<iostream>
#include<vector>
using namespace std;
int main()
{
vector<vector<int>>vec;
vec.push_back({1,2,3});
vec.push_back({3,545,35,});
vec.push_back({4,34,434,43});
vec.push_back({35,53,3,5});
// unlike array we dont have to maintain any fixed ssize
for(auto val:vec){
    for(auto val1:val){
        cout<<val1<<
        " ";
    }
    cout<<"\n";
}
return 0;
}