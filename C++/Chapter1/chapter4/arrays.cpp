#include<iostream>
using namespace std;
void display(int arr[], int size){
    for(int i=0; i<size; i++){
        cout<<arr[i]<<" ";
    }
}
void reverse(int arr[], int size){ // this is two pointer approach to reverse an array
    int start=0, end=size-1;
    while(start<end){
        swap(arr[start], arr[end]); // swap is a built-in function in C++ to swap two values
        start++;
        end--;
    }
}
void findMaxMin(int arr[], int size, int &max, int &min){
    max=INT16_MIN;
    min=INT16_MAX;
    for(int i=0; i<size; i++){
        if(arr[i]>max)
            max=arr[i];
        if(arr[i]<min)
            min=arr[i];
    }
    cout<<"Max: "<<max<<endl;
    cout<<"Min: "<<min<<endl;
}
void findunique(int arr[], int size){
    for(int i=0; i<size; i++){
        bool isUnique=true;
        for(int j=0; j<size; j++){
            if(i!=j && arr[i]==arr[j]){
                isUnique=false;
                
            }
        }
        if(isUnique)
            cout<<arr[i]<<" ";
    }
}       

int main(){
    
    int arr[12]={1,2,2,24,54,3,5,1,3,67,4,5};
    display(arr, 12);
    reverse(arr, 12);
    cout<<"\nReversed array: ";
    display(arr, 12);
    int max, min;
    findMaxMin(arr, 12, max, min);
    cout<<"Unique elements: ";
    findunique(arr, 12);

    
    return 0;
}
