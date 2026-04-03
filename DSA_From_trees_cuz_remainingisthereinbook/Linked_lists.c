// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node* next;
};
struct node*head=NULL;
struct node*tail=NULL;
int len=0;
void create(int x){
    struct node* newnode=(struct node*)malloc(sizeof(struct node));
    newnode->next=NULL;
    newnode->data=x;
    if(head==NULL){
        head=tail=newnode;
    }
    else{
        tail->next=newnode;
        tail=newnode;
    }
    
}
void display(){
    struct node* temp = head;
    while(temp != NULL){
        printf("%d \t ", temp->data);
        temp = temp->next;
    }
    printf("\n");   // fixed formatting
}
void length(){
    len=0;
     struct node* temp=head;
    while(temp!=NULL){
        len++;
        temp=temp->next;
}
printf("\n");
printf("length is %d ",len);
}
void insert(int x, int index){

    if(index < 0 || index > len){   // 🔴 FIX
        printf("Invalid index");
        return;
    }

    struct node* newnode=(struct node*)malloc(sizeof(struct node));
    newnode->next=NULL;
    newnode->data=x;

    if(index==0){
        newnode->next=head;
        head=newnode;
        if(tail == NULL) tail = newnode;   // 🔴 FIX
    }
    else if(index==len){
        tail->next=newnode;
        tail=newnode;
    }
    else{
        int i=0;
        struct node* temp=head;
        while(i<index-1){
            temp=temp->next;
            i++;
        }
        newnode->next=temp->next;
        temp->next=newnode;
    }

    len++;
}
void delete(int index){

    if(index < 0 || index >= len){
        printf("Invalid index");
        return;
    }

    if(index == 0){
        struct node* temp = head;
        head = head->next;
        if(head == NULL) tail = NULL;
        free(temp);
    }
    else if(index == len - 1){
        struct node* temp = head;
        struct node* parent = NULL;

        while(temp->next != NULL){
            parent = temp;
            temp = temp->next;
        }

        if(parent == NULL){
            head = tail = NULL;
        }
        else{
            parent->next = NULL;
            tail = parent;
        }

        free(temp);
    }
    else{
        int i = 0;
        struct node* temp = head;

        while(i < index - 1){
            temp = temp->next;
            i++;
        }

        struct node* nextnode = temp->next;
        temp->next = nextnode->next;
        free(nextnode);
    }

    len--;
}
struct node* deleteRepeating(struct node* head){
    struct node* temp1 = head;

    while(temp1 != NULL){
        struct node* temp2 = temp1->next;
        int flag = 0;

        // check if duplicate exists
        while(temp2 != NULL){
            if(temp1->data == temp2->data){
                flag = 1;
                break;
            }
            temp2 = temp2->next;
        }

        if(flag == 1){
            int val = temp1->data;

            // delete all occurrences of val
            struct node* curr = head;
            struct node* prev = NULL;

            while(curr != NULL){
                if(curr->data == val){
                    if(prev == NULL){
                        head = curr->next;
                        free(curr);
                        curr = head;
                    }
                    else{
                        prev->next = curr->next;
                        free(curr);
                        curr = prev->next;
                    }
                }
                else{
                    prev = curr;
                    curr = curr->next;
                }
            }

            // restart from head
            temp1 = head;
        }
        else{
            temp1 = temp1->next;
        }
    }

    return head;
}



int main() {
   create(5);
     create(7);
       create(6);
         create(9);
           create(3);
           display();
           length();
           insert(11, 0 );
           insert(12, 5 );
           insert(13, 3);
    display();
    delete(3);
 display();
    return 0;
}



