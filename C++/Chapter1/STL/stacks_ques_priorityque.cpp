#include<iostream>
#include<stack>
#include<queue>
using namespace std;
int main(){
stack<int> s;
s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);

stack<int> s1;

swap(s, s1);

cout << s.size() << endl;   // 0
cout << s1.size() << endl;  // 5

while (!s1.empty()) {
    cout << s1.top() << " ";
    s1.pop();
}

//QUEUE
// same like stack , uk stack and queue already
  queue<int> q; 

    // Insert elements
    q.push(10);
    q.push(20);
    q.push(30);

    // Front element
    cout << q.front() << endl;   // 10

    // Last element
    cout << q.back() << endl;    // 30

    // Remove front element
    q.pop();

    cout << q.front() << endl;   // 20

    // Size
    cout << q.size() << endl;    // 2

    // Empty
    cout << q.empty() << endl;   // 0 (false)

// 
//PRIOTITY QUEUE
priority_queue<int> pq; // IT IS LIKE MAX HEAP DEFAULT

    // Insert
    pq.push(10);
    pq.push(30);
    pq.push(20);
    pq.push(5);

    // Largest element
    cout << pq.top() << endl;      // 30

    // Remove largest element
    pq.pop();

    cout << pq.top() << endl;      // 20

    // Size
    cout << pq.size() << endl;     // 3

    // Empty
    cout << pq.empty() << endl;    // 0 (false)


     // FOR MIN HEAP PQ we can do
     priority_queue<int, vector<int>, greater<int>> PQ;

    // Insert elements
    PQ.push(30);
    PQ.push(10);
    PQ.push(50);
    PQ.push(20);

    // Smallest element
    cout << PQ.top() << endl;      // 10

    // Remove smallest element
    PQ.pop();

    cout << PQ.top() << endl;      // 20

    // Size
    cout << PQ.size() << endl;     // 3

    // Empty
    cout << PQ.empty() << endl;    // 0 (false)









}