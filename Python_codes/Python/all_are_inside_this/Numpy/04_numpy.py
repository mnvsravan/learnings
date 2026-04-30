# agreegate functions in numpy are functions that operate on an array and return a single value. These functions are used to perform various operations such as summing, finding the mean, finding the maximum or minimum value, etc. Some common aggregate functions in numpy include:
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(np.sum(a))  # Output: 15, this function returns the sum of all the elements in the array a.
print(np.mean(a))  # Output: 3.0, this function returns the mean (average) of all the elements in the array a.
print(np.max(a))  # Output: 5, this function returns the maximum value in the array a.
print(np.min(a))  # Output: 1, this function returns the minimum value in the array a.
print(np.prod(a))  # Output: 120, this function returns the product of all      the elements in the array a.
print(np.std(a))  # Output: 1.4142135623730951, this function returns the standard deviation of all the elements in the array a.
print(np.var(a))  # Output: 2.0, this function returns the variance of all the elements in the array a.     
print(np.median(a))  # Output: 3.0, this function returns the median value of all the elements in the array a. The median is the middle value when the elements are sorted in order. If there is an even number of elements, the median is the average of the two middle values. In this case, since there are 5 elements in the array a, the median is the value at index 2 (0-based index), which is 3.0.
print(np.argmax(a))  # Output: 4, this function returns the index of the maximum value in the array a. In this case, the maximum value is 5, which is located at index 4 (0-based index).
print(np.argmin(a))  # Output: 0, this function returns the index of the minimum value in the array a. In this case, the minimum value is 1, which is located at index 0 (0-based index).   
print(np.cumsum(a))  # Output: [ 1  3  6 10 15], this function returns the cumulative sum of the elements in the array a. The cumulative sum is calculated by adding each element to the sum of all previous elements. In this case, the cumulative sum is calculated as follows:
print(np.cumprod(a))  # Output: [  1   2   6  24 120], this function returns the cumulative product of the elements in the array a. The cumulative product is calculated by multiplying each element with the product of all previous elements. In this case, the cumulative product is calculated as follows:



# AXIS
my_array= np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
print(np.sum(my_array, axis=0))  # Output: [12 15 18], this function returns the sum of the elements along the specified axis. In this case, axis=0 means that the sum is calculated along the columns of the array my_array. The resulting array contains the sum of each column: [1+4+7, 2+5+8, 3+6+9] = [12, 15, 18].
print(np.sum(my_array, axis=1))  # Output: [ 6 15 24], this function returns the sum of the elements along the specified axis. In this case, axis=1 means that the sum is calculated along the rows of the array my_array. The resulting array contains the sum of each row: [1+2+3, 4+5+6, 7+8+9] = [6, 15, 24].

#Filtering

List_of_ages= np.array([[10, 13, 17],
                        [21, 50, 60],
                        [70, 80, 90]])

teenagers = List_of_ages[List_of_ages < 20]
print(teenagers)  # Output: [10 13 17], this code creates a new array called teenagers that contains only the elements from the List_of_ages array that are less than 20. The resulting array teenagers will contain the values [10, 13, 17], which are the ages of the teenagers in the original List_of_ages array.
adults= List_of_ages[(List_of_ages >= 20) & (List_of_ages < 60)] # We cannot use "and" , we must use & 
print(adults)  # Output: [21 50], this code creates a new array called adults that contains only the elements from the List_of_ages array that are greater than or equal to 20 and less than 60. The resulting array adults will contain the values [21, 50], which are the ages of the adults in the original List_of_ages array. Note that the age 60 is not included in the adults array because it does not satisfy the condition of being less than 60.

odds= List_of_ages[List_of_ages % 2 != 0]
print(odds)  # Output: [13 17 21 50 70 80], this code creates a new array called odds that contains only the elements from the List_of_ages array that are odd numbers. The resulting array odds will contain the values [13, 17, 21, 50, 70, 80], which are the odd ages in the original List_of_ages array. Note that the age 10 is not included in the odds array because it is an even number.

#If we want the keep same dimensions of the original array we can use np.where() function. For example:

#SYNTAX: np.where(condition, x, y) x is the value to be returned if the condition is true, and y is the value to be returned if the condition is false. The resulting array will have the same shape as the original array, with values determined by the condition.

filtered_array_below_20 = np.where(List_of_ages < 20, List_of_ages, 0)
print(filtered_array_below_20)  # Output: [[10 13 17] [ 0  0  0] [ 0  0  0]], this code creates a new array called filtered_array_below_20 that contains the same shape as the original List_of_ages array. The np.where() function is used to check each element of the List_of_ages array against the condition List_of_ages < 20. If the condition is true for an element, it is included in the filtered_array_below_20; otherwise, it is replaced with 0. As a result, the filtered_array_below_20 will contain the values [10, 13, 17] in the first row (where the condition is true) and 0s in the second and third rows (where the condition is false).

filtered_array_adults = np.where((List_of_ages >= 20) & (List_of_ages < 60), List_of_ages, 0)
print(filtered_array_adults)  # Output: [[ 0  0  0] [21 50  0] [ 0  0  0]], this code creates a new array called filtered_array_adults that contains the same shape as the original List_of_ages array. The np.where() function is used to check each element of the List_of_ages array against the condition (List_of_ages >= 20) & (List_of_ages < 60). If the condition is true for an element, it is included in the filtered_array_adults; otherwise, it is replaced with 0. As a result, the filtered_array_adults will contain the values [21, 50] in the second row (where the condition is true) and 0s in the first and third rows (where the condition is false).
filtered_array_odds = np.where(List_of_ages % 2 != 0, List_of_ages, 0)
print(filtered_array_odds)  # Output: [[ 0 13 17] [21  0  0] [ 0  0  0]], this code creates a new array called filtered_array_odds that contains the same shape as the original List_of_ages array. The np.where() function is used to check each element of the List_of_ages array against the condition List_of_ages % 2 != 0. If the condition is true for an element (i.e., if the element is an odd number), it is included in the filtered_array_odds; otherwise, it is replaced with 0. As a result, the filtered_array_odds will contain the values [13, 17] in the first row, [21] in the second row, and 0s in the third row (where the condition is false).
