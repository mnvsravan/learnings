// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

// There is only one repeated number in nums, return this repeated number.

// You must solve the problem without modifying the array nums and using only constant extra space.

 

// Example 1:

// Input: nums = [1,3,4,2,2]
// Output: 2
#include<iostream>
using namespace std;

int slow_fast(int arr[], int size) {

    int slow = arr[0];
    int fast = arr[0];

    // Phase 1: Detect cycle
    do {
        slow = arr[slow];
        fast = arr[arr[fast]];
    } while (slow != fast);

    // Phase 2: Find entrance of cycle
    slow = arr[0];

    while (slow != fast) {
        slow = arr[slow];
        fast = arr[fast];
    }

    return slow;   // fast would also work
}

int main() {

    int arr[5] = {1, 3, 4, 2, 2};

    cout << slow_fast(arr, 5);

} // this is mathemetically proved , u get to know later