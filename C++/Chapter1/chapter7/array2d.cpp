#include<iostream>
using namespace std;
#include <utility>

pair<int,int> linearSearch(int arr[][3], int rows, int cols, int key) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (arr[i][j] == key) {
                return {i, j};
            }
        }
    }

    return {-1, -1};
}
int maxRow(int arr[][3], int rows, int cols) {
    int ans = INT32_MIN;

    for (int i = 0; i < rows; i++) {
        int ans1 = 0;

        for (int j = 0; j < cols; j++) {
            ans1 += arr[i][j];
        }

        ans = max(ans, ans1);
    }

    return ans;
}
int diagonal(int arr[][3],int n){ // assume square matrices
    // we can use two for loops or..
    int sum=0;
    for(int i=0;i<n;i++){
         sum+=arr[i][i];
         if(i!=n-1-i){
            sum+=arr[i][n-1-i];
         }
        

    }
    return sum;
}
int main(){
int arr[2][3]={{1,2,3},{4,5,6}};
int brr[100][100];
int rows; int cols;
cout<<"Enter number of Rows";
cin>>rows;
cout<<"Enter number of Cols";
cin>>cols;
for(int i=0;i<rows;i++){
    for(int j=0;j<cols;j++){
        cin>>brr[i][j];
    }
}
cout<<"Printg...";
for(int i=0;i<rows;i++){
    for(int j=0;j<cols;j++){
cout<<arr[i][j];
    }
}
    
    return 0;
}