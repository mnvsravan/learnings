#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
// You are given N stalls and C cows. 
// Your task is to assign the cows to the stalls such that the minimum distance between any two cows is as large as possible.
bool isValid(vector<int>& stalls, int n, int c, int mid){
    sort(stalls.begin(),stalls.end());
    int cowCount=1;
    int lastPos=stalls[0];
    for(int i=1;i<n;i++){
        if(stalls[i]-lastPos>=mid){
            cowCount++;
             lastPos=stalls[i];
        }
        if(cowCount>=c){
            return true;
        }
    }
    return false;
}
void AggressionCows(vector<int>& stalls, int n, int c){
    sort(stalls.begin(),stalls.end());
    int start=0;
    int end=stalls[n-1]-stalls[0];
    int ans=-1;
    while(start<=end){
        int mid=(start+end)/2;
        if(isValid(stalls,n,c,mid)){
            ans=mid;
            start=mid+1;
        }
        else{
            end=mid-1;
        }
    }
    cout<<"The largest minimum distance between any two cows is: "<<ans<<endl;
}
int main(){
    vector<int> stalls={1,2,4,8,9};
    int n=stalls.size();
    int c=3;
    AggressionCows(stalls,n,c);
    return 0;
}
// it works like
// 1,2,4,8,9
// cows are 3 
// cows can be placed among 1 2 4 8 9
// now lets say after sorting cow1 is placed at index 0 i.e 1 and say mid is 3
// now cow2 can be placed at index 2 i.e 4 and cow3 can be placed at index 3 i.e 8
// cuz 1+3 is 4 i.e it can be placed at index 2
// now 4+3 is 7 i.e it can be placed at index 3 
// now lets say after sorting cow1 is placed at index 0 i.e 1 and say mid is 4
// now c ow 2 , 1+4 is 5 i.e it can be placed at index 3 i.e 8
// now 8+4 is 12 i.e it can not be placed at index 4 i.e 9

