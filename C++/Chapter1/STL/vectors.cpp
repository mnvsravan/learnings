#include<iostream>
#include<vector>
using namespace std;
int main(){
// ways to initialize vectors
vector<int> vec;
vector<int> vec1={1,2,3,4}; // we define size
vector<int> vec2(3,10);// we create size 3 with 10 as values
vector<int> vec3(vec1);// we initialize vector with vec1

//Operations like size,capacity,push_back,pop_back,emplace_back,at,front and back
// when we pushback it just dosent add one element at end , like if 1 is present it becomes 1,_ now 2 goes
// similarly 1,2 and we pushback then it becomes 1,2,_,_ now we insert 3 , 1,2,3,_ so it dooubles its capacity
vec.push_back(1);
vec.push_back(2);
vec.push_back(3);
// cout<<vec<<"\n"; we cant do like  this 
for(int val:vec){
    cout<<val<<",";
}
cout<<"\n";
cout<<"size is "<<vec.size()<<"\n";
cout<<vec.capacity();
vec.pop_back();
cout<<"\n";
cout<<vec.at(1); // print element at index 1
cout<<"\n";
cout<<vec.front()<<" "<<vec.back();
cout<<"\n";
// cout << vec.emplace_back(5); this like adds 5 at end same like push_back

//erase,insert,clear,empty
vec.push_back(3);
vec.push_back(4);
vec.push_back(5);
for(int val:vec){
    cout<<val<<" ";
}
vec.erase(vec.begin()+3,vec.end()); // [start.end)
vec.insert(vec.begin()+1,9); // [start,val]
cout<<"\n";
for(int val:vec){
    cout<<val<<" ";
}
cout<<"\n";
vec.clear(); // clears vector
cout<<vec.empty();//returns 0 or 1
cout<<"\n";

// ITERATORS, like the v.begin(), v.end()
vec.push_back(1);
vec.push_back(2);
vec.push_back(3);

vector<int>:: iterator it;
for(it=vec.begin();it!=vec.end();it++){
cout<<*(it)<<" ";
}
cout<<"\n";
vector<int>:: reverse_iterator itr;
for(itr=vec.rbegin();itr!=vec.rend();itr++){
cout<<*(itr)<<" ";
}
// OR WE CAN AUTO,it will understand what to do
cout<<"\n";
for(auto it=vec.begin();it!=vec.end();it++){
cout<<*(it)<<" ";
}
cout<<"\n";
for(auto itr=vec.rbegin();itr!=vec.rend();itr++){
cout<<*(itr)<<" ";
}



}