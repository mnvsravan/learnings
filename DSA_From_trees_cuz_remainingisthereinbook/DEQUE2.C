#include<stdio.h> 
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
    struct node* prev; 
};
struct node* front = NULL;
struct node* rear = NULL;
void insert(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;
    newnode->prev = NULL;

    if(front == NULL){
        front = rear = newnode;
    }
    else{
        rear->next = newnode;
        newnode->prev = rear; 
        rear = newnode;
    }
}
void enqueue_front(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;
    newnode->prev = NULL;

    if(front == NULL){
        front = rear = newnode;
    }
    else{
        newnode->next = front;   
        front->prev = newnode; 
        front = newnode;
    }
}
void enqueue_rear(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;
    newnode->prev = NULL;

    if(front == NULL){
        front = rear = newnode;
    }
    else{
        rear->next = newnode;
        newnode->prev = rear; 
        rear = newnode;
    }
}
void dequeue_front(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }
else if(front == rear){
    free(front);
    front = rear = NULL;
}
else{
    struct node* temp = front;
    front = front->next;
        front->prev = NULL; 
    free(temp);
}
}
void dequeue_rear(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }
else if(front == rear){
    free(front);
    front = rear = NULL;
}
else{
    struct node* temp = rear;
    rear = rear->prev;
    rear->next = NULL;
    free(temp);
}
}
void peek(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }

    printf("Front element is %d\n", front->data);
}
void peek_rear(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }

    printf("Rear element is %d\n", rear->data);
}
void display(){
    struct node* temp = front;
    while(temp != NULL){
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
void length(){
    struct node* temp = front;
    int count = 0;

    while(temp != NULL){
        count++;
        temp = temp->next;
    }

    printf("Length of the linked list is %d\n", count);
}
int main(){
     enqueue_front(7);
      enqueue_front(2);
    enqueue_rear(10);
    enqueue_rear(20);
    

    printf("Queue after enqueuing elements: ");
    display();

    peek();
    peek_rear();

    dequeue_front();
    printf("Queue after dequeuing from front: ");
    display();

    dequeue_rear();
    printf("Queue after dequeuing from rear: ");
    display();

    length();

    return 0;
}   