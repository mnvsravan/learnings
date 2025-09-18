#include <stdio.h>  // include the standard input-output library

int main() {
    int arr[2][3][4];  
    // declare a 3D array of integers with dimensions [2][3][4]
    // total elements = 2 * 3 * 4 = 24

    // ---- Input values ----
    for (int i = 0; i < 2; i++) {          // loop for the first dimension (size 2)
        for (int j = 0; j < 3; j++) {      // loop for the second dimension (size 3)
            for (int k = 0; k < 4; k++) {  // loop for the third dimension (size 4)
                
                // prompt user to enter value for specific indices
                printf("Enter the value of arr[%d][%d][%d]: ", i, j, k);
                
                // take input and store it in arr[i][j][k]
                scanf("%d", &arr[i][j][k]);
            }
        }
    }

    // ---- Output values ----
    for (int i = 0; i < 2; i++) {          // loop again for first dimension
        for (int j = 0; j < 3; j++) {      // loop for second dimension
            for (int k = 0; k < 4; k++) {  // loop for third dimension
                
                // print the stored value at arr[i][j][k]
                printf("The value of arr[%d][%d][%d] is %d\n", i, j, k, arr[i][j][k]);
            }
        }
    }

    return 0; // end of program
}
//#include <stdio.h>

//int main() {
    // Declare and initialize a 3D array with fixed values
  //  int arr[2][3][4] = {
    //    {   // first "block" (i = 0)
      //      {1, 2, 3, 4},     // j = 0
        //    {5, 6, 7, 8},     // j = 1
          //  {9, 10, 11, 12}   // j = 2
        //},
        //{  / // second "block" (i = 1)
            //{13, 14, 15, 16}, // j = 0
    //        {17, 18, 19, 20}, // j = 1
      //      {21, 22, 23, 24}  // j = 2
        //}
  //  };

    // Print all elements of the 3D array
    //for (int i = 0; i < 2; i++) {          // loop for first dimension
      //  for (int j = 0; j < 3; j++) {      // loop for second dimension
        //    for (int k = 0; k < 4; k++) {  // loop for third dimension
          //      printf("arr[%d][%d][%d] = %d\n", i, j, k, arr[i][j][k]);
   //         }
   ///     }
    //}/

    //return 0;
//}


