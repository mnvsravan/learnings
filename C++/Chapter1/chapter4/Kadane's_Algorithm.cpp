//FINDING THE THE MAXIMUM SUM OF A CONTIGUOUS SUBARRAY USING KADANE'S ALGORITHM
// like from an array a subarray in which sum is max among rest
#include <iostream>
using namespace std;
void displaySubarrays(int arr[], int size) {  
    int count = 0;
    for (int start = 0; start < size; start++) {
        for (int end = start; end < size; end++) {
            for (int k = start; k <= end; k++) {
                cout << arr[k] << " ";
            }
            cout << endl;
            count++;  // number of subarrays is n(n+1)/2
        }
        
    }
    cout << "Total number of subarrays: " << count << endl;
}
void BruteForceMaxSubarraySum(int arr[], int size) { // we use only 2 for loops instead of 3 for loops to find the max sum of subarray cuz we don't need to print the subarray we just need the sum of subarray so we can use 2 for loops to find the max sum of subarray like initial point same we can use the previous sum and add the next element to it to find the sum of subarray instead of using 3 for loops to find the sum of subarray
    int maxSum = INT32_MIN;
    for (int start = 0; start < size; start++) {
        int currentSum = 0;            // cuz initial is same we just add the upcoming element to the previous sum
        for (int end = start; end < size; end++) {
                currentSum += arr[end];
                maxSum = max(maxSum, currentSum);  // update maxSum if currentSum is greater
        }
    }
    cout << "Maximum subarray sum (Brute Force): " << maxSum << endl;
}
void KadaneMaxSubarraySum(int arr[], int size) {
    int maxSum = INT32_MIN;
    int currentSum = 0;
    for (int i = 0; i < size; i++) {
        currentSum += arr[i];
        maxSum = max(maxSum, currentSum);
        if (currentSum < 0) {
            currentSum = 0;  // reset current sum if it becomes negative
        }
    }
    cout << "Maximum subarray sum (Kadane's Algorithm): " << maxSum << endl;
}
int main() {
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int size = sizeof(arr) / sizeof(arr[0]);
    displaySubarrays(arr, size);  
    BruteForceMaxSubarraySum(arr, size);
    KadaneMaxSubarraySum(arr, size);
    return 0;
}