#include <stdio.h>

int main() {
    int arr[3][2];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            printf("Enter the value of arr[%d][%d]\n", i, j);
            scanf("%d", &arr[i][j]);
        }
    }

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            printf("The value of arr[%d][%d] is %d\n", i, j, arr[i][j]);
        }
    }

    return 0; 
}
//#include <stdio.h>

//int main() {
    // Declare and initialize a 2D array with fixed values
  //  int arr[3][2] = {
    //    {1, 2},   // row 0
      //  {3, 4},   // row 1
        //{5, 6}    // row 2
   // };

    // Print all values of the array
   // for (int i = 0; i < 3; i++) {       // loop for rows
     //   for (int j = 0; j < 2; j++) {   // loop for columns
       //     printf("The value of arr[%d][%d] is %d\n", i, j, arr[i][j]);
        //}
   // }

//    return 0;
//}
