#include <stdio.h>  // Standard input/output library

// Define a struct to represent a 2D vector
struct vector {
    int i;  // x-component
    int j;  // y-component
};

// Function to add two vectors and return the result in **one line**
struct vector sumvector(struct vector v1, struct vector v2) {
    // Directly return a struct with summed components
    return (struct vector){v1.i + v2.i, v1.j + v2.j};
}

int main() {
    // Declare and initialize two vectors
    struct vector v1 = {1, 2};
    struct vector v2 = {3, 4};

    // Call the function and store result
    struct vector result = sumvector(v1, v2);

    // Print the sum of vectors
    printf("The sum of vectors is %di + %d j\n", result.i, result.j);

    return 0;  // End of program
}
// #include <stdio.h>  // Standard input/output library

// Define a struct to represent a 2D vector
//struct vector {
  //  int i;  // x-component of vector
    //int j;  // y-component of vector
//};

// Function to add two vectors and return the result
//struct vector sumvector(struct vector v1, struct vector v2) {
    // Create a struct variable to store the sum
  //  struct vector sum;

    // Add corresponding components of v1 and v2
    //sum.i = v1.i + v2.i;  // sum of x-components
    //sum.j = v1.j + v2.j;  // sum of y-components

    // Return the resulting vector
    //return sum;
//}

//int main() {
  //  // Declare and initialize two vectors
    //struct vector v1 = {1, 2};  // First vector
    //struct vector v2 = {3, 4};  // Second vector

    // Call the function sumvector to add v1 and v2
    //struct vector result = sumvector(v1, v2);

    // Print the sum of vectors in i and j components
//    printf("The sum of vectors is %di + %d j\n", result.i, result.j);

  //  return 0;  // End of program
//}


