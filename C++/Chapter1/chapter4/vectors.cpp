#include<iostream>
#include<vector> // vectors are dynamic arrays in C++ STL, STL is a library in C++ which provides many useful data structures and algorithms
using namespace std; // dynamic system to store data in a contiguous memory location, it can grow and shrink in size as needed, it provides random access to elements, it is implemented as a template class in C++ STL

int main(){

    vector<int> v; // create an empty vector of integers we can also do like vector<int>vec={1,2,3,4,5}; to create a vector with initial values

    v.push_back(10); // add an element to the vector
    v.push_back(20); // add another element to the vector at the end of the vector
    v.push_back(30); // add another element to the vector
    v.pop_back(); // remove the last element of the vector

    for(int i=0; i<v.size(); i++){
        cout<<v[i]<<" "; // print all elements of the vector
    }

    // we can use for loop like this also
    cout<<"\n";

    for(int i:v){ // range based for loop, it is introduced in C++11, it is used to iterate over the elements of a container
        cout<<i<<" "; // print all elements of the vector
    }

    cout<<"\n";

    vector<char> chars(5, 'a'); // create a vector of characters with size 5 and initial value 'a'

    for(char c:chars){ // range based for loop to print all elements of the vector
        cout<<c<<" "; // print all elements of the vector
    }

    cout<<"\n";

    // we can use functions like front back , at,capacity,size etc
    cout<<"Front element: "<<v.front()<<endl; // print the first element of the vector
    cout<<"Back element: "<<v.back()<<endl; // print the last element of the vector
    cout<<"Element at index 1: "<<v.at(1)<<endl; // print the element at index 1 of the vector
    cout<<"Size of vector: "<<v.size()<<endl; // print the size of the vector
    cout<<"Capacity of vector: "<<v.capacity()<<endl; // print the capacity of the vector, capacity is the total number of elements that can be stored in the vector without reallocating memory

    // see leetcode 136 problem for an excersie problem on bitwise operator with vectors

    // Linear search using vectors
    bool found = false;

    for(int i=0; i<v.size(); i++){
        if(v[i] == 20){
            found = true;
            break;
        }
    }

    if(found){
        cout<<"Element found in the vector"<<endl;
    }
    else{
        cout<<"Element not found in the vector"<<endl;
    }

    // reverse a vector using STL reverse function
    // reverse(v.begin(), v.end()); // reverse the vector using STL reverse function

    cout<<"Original vector: ";
    for(int i=0; i<v.size(); i++){
        cout<<v[i]<<" "; // print all elements of the vector
    }

    cout<<endl;

    vector<int> tempp = v; // create a temporary vector to store the original vector

    for(int i=0; i<v.size(); i++){
        v[i] = tempp[v.size()-1-i]; // reverse the vector using for loop
    }

    cout<<"Reversed vector: ";
    for(int i=0; i<v.size(); i++){
        cout<<v[i]<<" "; // print all elements of the vector
    }

    cout<<endl;

    return 0;
}