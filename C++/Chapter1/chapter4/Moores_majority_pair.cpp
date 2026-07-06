#include <iostream>
#include <vector>
using namespace std;
vector<int> pairSum(vector<int> arr, int target) {
    vector<int> result;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[i] + arr[j] == target) {
                result.push_back(arr[i]);
                result.push_back(arr[j]);
                return result; // Return the first pair found
            }
        }
    }
    return result; // Return empty if no pair found
}
vector<int> pairSumTwoPointer(vector<int> arr, int target) {
    vector<int> result;
    int left = 0;
    int right = arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            result.push_back(arr[left]);
            result.push_back(arr[right]);
            return result; // Return the first pair found
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return result; // Return empty if no pair found
}
void majorityBruteForces(vector<int> arr) {
    for(int i:arr){
        int count=0;
        for(int j:arr){
            if(i==j){
                count++;
            }
        }
        if(count>arr.size()/2){
            cout<<"Majority element is: "<<i<<endl;
            return;
        }
    }
    cout << "No majority element found." << endl;
}
// void majorityOptimal(vector<int> arr) {
//     sort vector arr in ascending order
// int frq=1;
// int ans=arr[0];
// for(int i=1;i<arr.size();i++){
//     if(arr[i]==arr[i-1]){
//         frq++;
//     }else{
//         frq=1;
//         ans=arr[i];
//     }
//     if(frq>arr.size()/2){
//         ans=arr[i];
//         break;
//     }
// }
// }
void majorityMoore(vector<int> arr) {
    int frq = 0;
    int ans = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (frq == 0) {
            ans = arr[i];
        } else if (arr[i] == ans) {
            frq++;
        } else {
            frq--;
        }
    }
    // Verify if the candidate is indeed the majority element
    // count = 0;
    // for (int num : arr) {
    //     if (num == candidate) {
    //         count++;
    //     }
    // }
    // if (count > arr.size() / 2) {
    //     cout << "Majority element is: " << candidate << endl;
    // } else {
    //     cout << "No majority element found." << endl;
    // }
    cout << "Majority element is: " << ans << endl;
}