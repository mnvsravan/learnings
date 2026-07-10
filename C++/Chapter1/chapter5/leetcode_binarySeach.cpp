// There are N books, where the i-th book contains A[i] pages.

// You have to allocate these books to M students such that the maximum number of pages assigned to any student is minimized.

// The following conditions must be satisfied:

// Each book must be allocated to exactly one student.
// Every student must receive at least one book.
// Books must be allocated in contiguous order (i.e., consecutive books only).

// Calculate and return the minimum possible value of the maximum number of pages assigned to a student.
#include<iostream>
#include<vector>
using namespace std;
bool Valid(vector<int>& arr, int n, int m, int mid){
    int studentCount=1;
    int pageSum=0;
    for(int i=0;i<n;i++){
        if(arr[i]>mid){
            return false;
        }
        if(pageSum+arr[i]>mid){
            studentCount++;
            pageSum=arr[i];
           
        }
         else{
            pageSum+=arr[i];
        }
        if(studentCount>m){
                return false;
            }
       
    }
    return true;
}
int AllocateBooks(vector<int>& arr, int n, int m){
    int start=0;
    int end=0;
    for(int i=0;i<n;i++){
        end+=arr[i];
    }
    int ans=INT32_MAX;
    while(start<=end){
        int mid=(start+end)/2;
        if(Valid(arr,n,m,mid)){
            ans=mid;
            end=mid-1;
        }
        else{
            start=mid+1;
        }
    }
    return ans;
}
int main(){
    vector<int> arr={12,34,67,90};
    int n=arr.size();
    int m=2;
    cout<<"Minimum possible value of the maximum number of pages assigned to a student: "<<AllocateBooks(arr,n,m)<<endl;
    return 0;
}
//  its works like lets say m=2 ie 2 students 
//  now cases are s1->12,s2->34,67,90 max pages=191
//  s1->12,34,s2->67,90 max pages=157
//  s1->12,34,67,s2->90 max pages=113
//  the answer is 113 which is the minimum possible value of the maximum number of pages assigned to a student.

// SAME QUESTION DIFFERENT CONTEXT

// Given are N boards of length of each given in the form of array, and M painters, such that each painter takes 1 unit of time to paint 1 unit of the board.

// The task is to find the minimum time to paint all boards under the constraints that any painter will only paint continuous sections of boards.

bool isValid(vector<int>& arr, int n, int m, int mid){
    int painterCount=1;
    int boardSum=0;
    for(int i=0;i<n;i++){
        if(arr[i]>mid){
            return false;
        }
        if(boardSum+arr[i]>mid){
            painterCount++;
            boardSum=arr[i];
        }
        else{
            boardSum+=arr[i];
        }
        if(painterCount>m){
            return false;
        }
    }
    return true;
}
void minTimeToPaintBoards(vector<int>& arr, int n, int m){
    int start=0;
    int end=0;
    for(int i=0;i<n;i++){
        end+=arr[i];
    }
    int ans=INT32_MAX;
    while(start<=end){
        int mid=(start+end)/2;
        if(isValid(arr,n,m,mid)){
            ans=mid;
            end=mid-1;
        }
        else{
            start=mid+1;
        }
    }
    cout<<"Minimum time to paint all boards: "<<ans<<endl;
}
int main(){
    vector<int> arr={10,20,30,40};
    int n=arr.size();
    int m=2;
    minTimeToPaintBoards(arr,n,m);
    return 0;
}

