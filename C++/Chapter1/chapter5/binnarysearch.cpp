#include<iostream>
#include<vector>
using namespace std;
void BinarySearch(vector<int>& arr, int target){
    int left=0, right=arr.size()-1, mid;
    while(left<=right){
        mid=(left+right)/2;
        if(arr[mid]==target){
            cout<<"Element found at index: "<<mid<<endl;
            return;
        }
        else if(arr[mid]<target){
            left=mid+1;
        }
        else{
            right=mid-1;
        }
    }
    cout<<"Element not found"<<endl;
}
void recursionBinarySearch(vector<int>& arr, int left, int right, int target){
    if(left>right){
        cout<<"Element not found"<<endl;
        return;
    }
    int mid=(left+right)/2;
    if(arr[mid]==target){
        cout<<"Element found at index: "<<mid<<endl;
        return;
    }
    else if(arr[mid]<target){
        recursionBinarySearch(arr, mid+1, right, target);
    }
    else{
        recursionBinarySearch(arr, left, mid-1, target);
    }
}
int main(){
vector<int> arr={1,2,3,4,5,6,7,8,9,10};
int target;
cout<<"Enter the element to search: ";
cin>>target;
BinarySearch(arr, target);
recursionBinarySearch(arr, 0, arr.size()-1, target);
return 0;
}