#include<iostream>
#include<vector>
using namespace std;

bool isSorted(vector<int>& arr, int size) {

    if(size == 0 || size == 1)
        return true;

    return arr[size-1] > arr[size-2] && isSorted(arr, size-1);
}

int binarySearch(vector<int>& arr, int start, int end, int key) {

    if(start > end)
        return -1;

    int mid = start + (end - start)/2;

    if(arr[mid] == key)
        return mid;

    if(key > arr[mid])
        return binarySearch(arr, mid+1, end, key);

    return binarySearch(arr, start, mid-1, key);
}

void recursion(vector<int>& arr, vector<int>& ans, int start) {

    if(start == arr.size()) {

        for(int val : ans)
            cout << val << " ";

        cout << endl;
        return;
    }

    ans.push_back(arr[start]);
    recursion(arr, ans, start+1);

    ans.pop_back();
    recursion(arr, ans, start+1);
}

int main() {

    vector<int> arr = {1,2,3,4};
    vector<int> ans;

    cout << isSorted(arr,4) << endl;

    cout << binarySearch(arr,0,3,4) << endl;

    recursion(arr,ans,0);

    return 0;
}