#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

struct node* front = NULL;
struct node* rear = NULL;

void insert(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;

    if(front == NULL){
        front = rear = newnode;
    }
    else{
        rear->next = newnode;
        rear = newnode;
    }
}

void enqueue_front(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;

    if(front == NULL){
        newnode->next = NULL;
        front = rear = newnode;
    }
    else{
        newnode->next = front;   
        front = newnode;
    }
}

void enqueue_rear(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;

    if(front == NULL){
        front = rear = newnode;
    }
    else{
        rear->next = newnode;
        rear = newnode;
    }
}
void dequeue_front(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }

    struct node* temp = front;
    front = front->next;
    free(temp);
}
void dequeue_rear(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }

    if(front == rear){
        free(front);
        front = rear = NULL;
        return;
    }
  else{
    struct node* temp = front;
    struct node* newrear = rear;
    while(temp->next != rear){
        temp = temp->next;
    }
temp->next = NULL;
rear = temp;
free(newrear);
    
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

    insert(10);
    insert(20);
    insert(30);
    insert(40);

    printf("Queue after inserting 10, 20, 30, 40:\n");
    display();

    peek();
    peek_rear();

    dequeue_front();
    printf("Queue after dequeuing from front:\n");
    display();

    dequeue_rear();
    printf("Queue after dequeuing from rear:\n");
    display();

    enqueue_front(5);
    printf("Queue after enqueuing 5 at front:\n");
    display();

    enqueue_rear(50);
    printf("Queue after enqueuing 50 at rear:\n");
    display();

    length();

    return 0;
}





















