#include<iostream>
#include <vector>
#include <list>
#include <deque>
using namespace std;
int main(){
list<int>lt;
lt.push_back(2);
lt.push_front(4);
lt.emplace_back(3);
lt.emplace_front(5);
lt.pop_back();
lt.pop_front();
cout<<"\n";
// the size,erase,clar,iteration begin end and all are same like vector
for(auto it=lt.begin();it!=lt.end();it++){
    cout<<*(it)<<" ";
}
cout<<"\n";

//DEQUE IS ALSO SAME AS LIST JUST THAT RANDOM ACCESING IS POSSIBLE 
deque<int>d;
d.push_back(2);
d.push_front(4);
d.emplace_back(3);
d.emplace_front(5);

cout<<d[3]; // in list lt[3] not possible
cout<<"\n";
//PAIR

pair<int,string>one={69,"sus"}; // like u can do int,float and combo of datatypes
cout<<one.first<<" "<< one.second;
cout<<"\n";

pair<string, pair<int, string>> two = {"Sravan", {56, "fhggh"}};
cout<<two.first<<" "<< two.second.first;

cout<<"\n";


vector<pair<int,int>>goat={{1,2},{3,4},{5,6}};
for(auto gt:goat){
    cout<<gt.second<<" ";
}

goat.push_back({7,9});
goat.emplace_back(10,11); // this is diff between emplace and push back and its faster (int-place objectrs create)
cout<<"\n";
for(auto gt:goat){
    cout<<gt.first<<" ";
}












}