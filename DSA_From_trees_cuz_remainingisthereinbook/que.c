// using arrays
#include <stdio.h>
int front = -1;
int rear = -1;
int queue[5];
int size = 5;
void insert(int x){
    if((rear + 1) % size == front){
        printf("Overflow\n");
    }
    else if(front == -1 && rear == -1){
        front = rear = 0;
        queue[rear] = x;
    }
    else{
        rear = (rear + 1) % size;
        queue[rear] = x;
       
    }
}
void delete(){
    if(front == -1 && rear == -1){
        printf("Underflow\n");
    }
    else if(front==rear){
        printf("The deleted element is %d\n", queue[front]);
        front = rear = -1;
    }
    else{
        printf("The deleted element is %d\n", queue[front]);
        front = (front + 1) % size;
    }

}
void peak(){
    if(front == -1 && rear == -1){
        printf("Queue is empty\n");
    }
    else{
        printf("The front element is %d\n", queue[front]);
    }
}
void display(){
    if(front == -1 && rear == -1){
        printf("Queue is empty\n");
    }
    else{
        int i = front;
        while(i != rear){
            printf("%d ", queue[i]);
            i = (i + 1) % size;
        }
        printf("%d\n", queue[rear]);
    }
}
int main() {
    printf("Array Queue:\n");
    insert(6);
    insert(4);
    insert(8);
    insert(10);
    insert(12);
    insert(14);
    insert(16); // This should cause overflow since size is 5
    delete();
    delete();
    peak();
    display();
}



