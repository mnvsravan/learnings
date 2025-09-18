#include <stdio.h>  // Include standard input-output header for printf

// Function to print elements of an array
void printArray(int a[], int n) {
    // Loop through each element of the array
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);  // Print the current element followed by a space
    }
    printf("\n");  // Print a newline after printing all elements
}

// Function to reverse the elements of the array in place
void reverse(int arr[], int n) {
    /*
     * Swap elements from start to end moving towards the middle:
     * For i from 0 to n/2, swap arr[i] and arr[n - i - 1]
     */
    int temp;  // Temporary variable for swapping

    // Loop from the start to the middle of the array
    for (int i = 0; i < n / 2; i++) {
        temp = arr[i];               // Store the current element in temp
        arr[i] = arr[n - i - 1];    // Replace current element with its opposite from end
        arr[n - i - 1] = temp;      // Replace the opposite element with the temp value (original current)
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};  // Declare and initialize the array
    int n = 6;                       // Store the size of the array

    printArray(arr, n);  // Print original array

    reverse(arr, n);     // Reverse the array in place

    printArray(arr, n);  // Print the reversed array

    return 0;            // Return 0 to indicate successful execution
}

// starting is arr 0 arr 1 ... arr 5
// arr[0] ↔ arr[5]  →  1 ↔ 6  
//arr[1] ↔ arr[4]  →  2 ↔ 5  
//arr[2] ↔ arr[3]  →  3 ↔ 4  
//At this point, the array is fully reversed.

//Notice that you only need 3 swaps for 6 elements.