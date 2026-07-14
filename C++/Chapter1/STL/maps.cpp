#include<iostream>
#include<map>
#include <unordered_map>
using namespace std;
int main(){
map<string,int>mp;
// insert,find,count,erase,size,empty

mp["TV"]=500000;
mp["WATCH"]=100000;
mp["LAPTOP"]=700000;
mp["PC"]=900000;
mp.emplace("Camera",5000); // idk insert isnt working use mannual array or emplace
for(auto val:mp){
cout<<val.first<<"->"<<val.second<<" "; // we notice that all these tv and all come in aplha order
}
cout<<"\n";
cout<<mp.count("TV");
cout<<"\n";
cout<<mp["TV"];
cout<<"\n";
if (mp.find("TV") != mp.end()) { // FOR CHECKING WE MUST DO LIKE THIS
    cout << "Found";
} else {
    cout << "Not Found";
}
cout<<"\n";
mp.erase("TV");
cout<<"\n";
for(auto val:mp){
cout<<val.first<<"->"<<val.second<<" "; // we notice that all these tv and all come in aplha order
}
cout<<"\n";
cout<<mp.empty();
cout<<"\n";

//Multimap is like it can store same strings many times
multimap<string,int>Mp;
Mp.emplace("TV",10000);
Mp.emplace("TV",10000);
Mp.emplace("TV",10000);
Mp.emplace("TV",10000);

for(auto val:Mp){
cout<<val.first<<"->"<<val.second<<" "; 
}
Mp.erase(Mp.find("TV")); // for here we need to use find to erase
cout<<"\n";
for(auto val:Mp){
cout<<val.first<<"->"<<val.second<<" "; 
}


//Unordered map
unordered_map<string,int>UP;
// unlike normal map this is unordered

UP.emplace("TV",10000);
UP.emplace("hthfth",20000);
UP.emplace("neray",30000);
UP.emplace("wrtyntyrteh",40000);
UP.emplace("jdtgm",50000);
cout<<"\n";
for(auto val:UP){
cout<<val.first<<"->"<<val.second<<" "; // we notice that all these are in random alpha order
}






}