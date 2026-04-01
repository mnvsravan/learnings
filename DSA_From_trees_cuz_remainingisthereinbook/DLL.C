#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
    struct node* prev;
};

struct node* head = NULL;
struct node* tail = NULL;
int len = 0;   

void create(int x){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = x;
    newnode->next = NULL;
    newnode->prev = NULL;

    if(head == NULL){
        head = tail = newnode;
    }
    else{
        newnode->prev = tail;
        tail->next = newnode;
        tail = newnode;
    }
}

void display(){
    struct node* temp = head;
    while(temp != NULL){
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void length(){
    len = 0;
    struct node* temp = head;

    while(temp != NULL){
        len++;
        temp = temp->next;
    }

    printf("length is %d\n", len);
}
void insert( int x, int index){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = x;
    newnode->next = NULL;
    newnode->prev = NULL;
    if(index < 0 || index >=len){
    printf("Invalid index\n");
    return;
}
else if(index==0){
    if(head != NULL){
    newnode->next=head;
    head->prev=newnode;
    head=newnode;
    }
    else{
        head=tail=newnode;
    }
}
else if(index==len-1){
    if(tail != NULL){
    newnode->prev=tail;
    tail->next=newnode;
    tail=newnode;
    }
    else{
         head=tail=newnode;
    }
}
else if (index>0 && index<len-1){
    int i=0;
    struct node* temp=head;
    while(i<index-1){
        temp=temp->next;
        i++;
        
    }
    newnode->prev=temp;
    newnode->next=temp->next;
    temp->next->prev = newnode;   
temp->next = newnode;         
}
len++;
}
void delete(int index){
   if(index < 0 || index >=len){
    printf("Invalid index\n");
    return;
}
else if(index==0){
    if(head==NULL){
        printf("error");
    }
    else{
        struct node*temp=head;
        head->next->prev=NULL;
        head=head->next;
        free(temp);
    }
}
else if(index==len-1){
    if(tail==NULL){
        printf("error");
    }
    else{
        struct node* temp=tail;
        tail->prev->next=NULL;
        tail=tail->prev;
        free(temp);
    }
}
else if(index > 0 && index < len-1){
    int i = 0;
    struct node* temp = head;

    while(i < index){
        temp = temp->next;
        i++;
    }

    temp->prev->next = temp->next;   
    temp->next->prev = temp->prev;   
    free(temp);
}

len--;
}


int main(){

    create(1);
    create(2);
    create(3);
    create(4);
    create(5);

    display();
    length();
    insert(6,0);
    insert(7,5);
    insert(8,4);
    display();
    delete(2);
    display();

    return 0;
}