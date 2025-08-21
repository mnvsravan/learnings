#include <stdio.h>

int main(){
   // int legnth = 10; // Example length
    //int width = 5; // Example width
    int legnth, width; // Declare variables for length and width
    printf("Enter length rectangle\n");
    scanf("%d", &legnth); // Read length and width from user input
    printf("Enter width of rectangle\n");
    scanf("%d", &width); // Read width from user input
    // Calculate area of rectangle
    // printf("Area of rectangle: %d\n", legnth * width);   
    printf("Area of rectangle: %d\n", legnth * width); // Calculate and print area
    return 0;
}
