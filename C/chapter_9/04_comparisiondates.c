#include <stdio.h>  // Include standard input/output library for printf and scanf

// Define a struct to store a date
typedef struct {
    int day;    // Integer to store the day of the month (1-31)
    int month;  // Integer to store the month (1-12)
    int year;   // Integer to store the year (e.g., 2025)
} Date;

// Function to compare two dates
// Returns:
// -1 if date1 < date2
//  0 if date1 == date2
//  1 if date1 > date2
int compareDates(Date date1, Date date2) {
    // First, compare years
    if(date1.year < date2.year) {
        return -1;  // date1 is earlier
    } else if(date1.year > date2.year) {
        return 1;   // date1 is later
    } else {
        // Years are equal, compare months
        if(date1.month < date2.month) {
            return -1;  // date1 is earlier
        } else if(date1.month > date2.month) {
            return 1;   // date1 is later
        } else {
            // Months are also equal, compare days
            if(date1.day < date2.day) {
                return -1;  // date1 is earlier
            } else if(date1.day > date2.day) {
                return 1;   // date1 is later
            } else {
                return 0;   // Both dates are exactly the same
            }
        }
    }
}

int main() {
    Date d1, d2;  // Declare two Date variables to store input dates

    // Input first date
    printf("Enter first date (day month year): ");
    scanf("%d %d %d", &d1.day, &d1.month, &d1.year);

    // Input second date
    printf("Enter second date (day month year): ");
    scanf("%d %d %d", &d2.day, &d2.month, &d2.year);

    // Compare the two dates using the compareDates function
    int result = compareDates(d1, d2);

    // Display the result based on the comparison
    if(result == -1) {
        printf("The first date is earlier than the second date.\n");
    } else if(result == 1) {
        printf("The first date is later than the second date.\n");
    } else {
        printf("Both dates are the same.\n");
    }

    return 0;  // End of program
}
