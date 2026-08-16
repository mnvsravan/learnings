#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// ===============================
// MERGE SORTED ARRAYS - LEETCODE 88
// ===============================

void merge_arrays(vector<int>& arr1, vector<int>& arr2) {

    int i = arr1.size() - 1;
    int j = arr2.size() - 1;
    int idx = arr1.size() - 1;

    while (i >= 0 && j >= 0) {

        if (arr1[i] > arr2[j]) {
            arr1[idx] = arr1[i];
            i--;
        }
        else {
            arr1[idx] = arr2[j];
            j--;
        }

        idx--;
    }

    while (j >= 0) {
        arr1[idx] = arr2[j];
        j--;
        idx--;
    }
}


// ===============================
// NEXT PERMUTATION
// 3 STEPS:
// 1. Pivot
// 2. Swap with > pivot
// 3. Reverse after pivot
// ===============================

void nextPermutation(vector<int>& nums) {

    // STEP 1: Find pivot
    int pivot = -1;

    for (int i = nums.size() - 2; i >= 0; i--) {

        if (nums[i] < nums[i + 1]) {
            pivot = i;
            break;
        }
    }

    // No pivot means array is in descending order
    if (pivot == -1) {
        reverse(nums.begin(), nums.end());
        return;
    }

    // STEP 2: Find element greater than pivot
    for (int i = nums.size() - 1; i > pivot; i--) {

        if (nums[i] > nums[pivot]) {
            swap(nums[i], nums[pivot]);
            break;
        }
    }

    // STEP 3: Reverse after pivot
    reverse(nums.begin() + pivot + 1, nums.end());
}


// ===============================
// PRINT ARRAY
// ===============================

void printArray(vector<int> arr) {

    for (int x : arr) {
        cout << x << " ";
    }

    cout << endl;
}


// ===============================
// MAIN
// ===============================

int main() {

    // --------------------------------
    // Example 1: Merge Arrays
    // --------------------------------

    vector<int> arr1 = {1, 2, 3, 0, 0, 0};
    vector<int> arr2 = {2, 5, 6};

    // For this simple version, resize is already present in arr1
    // so we need only use the first 3 actual elements.
    
    // Instead, demonstrate with separate vectors:
    vector<int> a = {1, 2, 3};
    vector<int> b = {2, 5, 6};

    // Our merge function expects arr1 to have space.
    a.resize(a.size() + b.size());

    // Move original elements to the front is not needed here
    // because resize added zeros at the end.
    
    merge_arrays(a, b);

    cout << "Merged array: ";
    printArray(a);


    // --------------------------------
    // Example 2: Next Permutation
    // --------------------------------

    vector<int> nums = {1, 2, 5, 4, 3};

    cout << "Before permutation: ";
    printArray(nums);

    nextPermutation(nums);

    cout << "After permutation: ";
    printArray(nums);


    return 0;
}