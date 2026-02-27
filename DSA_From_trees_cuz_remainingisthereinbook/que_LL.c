#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node* next;
};
struct node* front=NULL;
struct node* rear=NULL;
void insert(int x){
    struct node* newnode;
    newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=x;
    newnode->next=0;
    if(front==NULL){
        front=rear=newnode;
        front->next=front;
    }
    else{
        rear->next=newnode;
        rear=newnode;
        rear->next=front;
    }
}
void delete(){
    if(front == NULL){
        printf("Underflow\n");
        return;
    }

    struct node* temp = front;

    if(front == rear){   // only one node
        printf("the deleted element is %d\n", front->data);
        front = rear = NULL;
    }
    else{
        printf("the deleted element is %d\n", front->data);
        front = front->next;
        rear->next = front;   // maintain circular link
    }

    free(temp);
}
void peak(){
    if(front==NULL){
        printf("Underflow");
    }
    else{
        printf("the first element is %d \n",front->data);
    }
}
void display(){
    if(front == NULL){
    printf("Queue is empty\n");
    return;
}
else{
    struct node* temp=front;
    while(temp != rear){
        printf("the elemnt is %d \n",temp->data);
        temp=temp->next;
    }
    printf("the elemnt is %d",temp->data);
}
}

int main(){
    insert(50);
     insert(40);
      insert(30);
       insert(20);
        insert(10);
        delete();
        peak();
        display();
}