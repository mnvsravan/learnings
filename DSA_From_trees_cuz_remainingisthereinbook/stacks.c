// using arrays
#include <stdio.h>

int top = -1;
int stack[5];
int size = 5;

void insert(int x){
    if(top == size - 1){
        printf("Overflow\n");
    }
    else{
        top++;
        stack[top] = x;
    }
}

void delete(){
    if(top == -1){
        printf("Underflow\n");
    }
    else{
        printf("The deleted element is %d\n", stack[top]);
        top--;
    }
}

void peak(){
    if(top == -1){
        printf("Stack is empty\n");
    }
    else{
        printf("The top element is %d\n", stack[top]);
    }
}

void display(){
    if(top == -1){
        printf("Stack is empty\n");
    }
    else{
        for(int i = top; i >= 0; i--){
            printf("Index %d -> %d\n", i, stack[i]);
        }
    }
}


// # using linked list
#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

struct node* top_1 = NULL;

void create_1(int x){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = x;
    newnode->next = NULL;
    if(top_1 == NULL){
        top_1 = newnode;
    }
    else{
        newnode->next = top_1;
        top_1 = newnode;
    }
}

void delete_1(){
    struct node* temp = top_1;
    if(top_1 == NULL){
        printf("Underflow\n");
    }
    else if(top_1->next == NULL){
        printf("The deleted element is %d\n", top_1->data);
        free(temp);
        top_1 = NULL;
    }
    else{
        printf("The deleted element is %d\n", temp->data);
        top_1 = top_1->next;
        free(temp);
    }
}

void peak_1(){
    if(top_1 == NULL){
        printf("Stack is empty\n");
    }
    else{
        printf("The top element is %d\n", top_1->data);
    }
}

void display_1(){
    struct node* temp = top_1;
    if(top_1 == NULL){
        printf("Stack is empty\n");
    }
    else{
        while(temp != NULL){
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {

    printf("Array Stack:\n");
    insert(6);
    insert(4);
    delete();
    peak();
    display();

    printf("\nLinked List Stack:\n");
    create_1(6);
    create_1(4);
    delete_1();
    peak_1();
    display_1();

    return 0;
}