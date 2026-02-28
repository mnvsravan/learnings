#include <stdio.h>
#include <stdlib.h>

struct node{
    int coeff;
    int exp;
    struct node* next;
};

// Insert at end
struct node* insert(struct node* head, int c, int e){

    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->coeff = c;
    newnode->exp = e;
    newnode->next = NULL;

    if(head == NULL){
        head = newnode;
    }
    else{
        struct node* temp = head;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = newnode;
    }

    return head;
}

// Display polynomial
void display(struct node* head){

    while(head != NULL){

        printf("%dx^%d", head->coeff, head->exp);

        if(head->next != NULL){
            printf(" + ");
        }

        head = head->next;
    }

    printf("\n");
}
// ADDITION
struct node* add(struct node* p1, struct node* p2){

    struct node* result = NULL;
    struct node* temp = NULL;
    struct node* newnode;

    while(p1 != NULL && p2 != NULL){

        newnode = (struct node*)malloc(sizeof(struct node));
        newnode->coeff = p1->coeff + p2->coeff;
        newnode->exp = p1->exp;
        newnode->next = NULL;

        if(result == NULL){
            result = newnode;
            temp = newnode;
        }
        else{
            temp->next = newnode;
            temp = newnode;
        }

        p1 = p1->next;
        p2 = p2->next;
    }

    return result;
}
// MULTIPLICATION
struct node* multiply(struct node* p1, struct node* p2){

    struct node* result = NULL;
    struct node* temp = NULL;
    struct node* newnode;

    struct node* t1 = p1;
    struct node* t2;

    while(t1 != NULL){

        t2 = p2;

        while(t2 != NULL){

            newnode = (struct node*)malloc(sizeof(struct node));
            newnode->coeff = t1->coeff * t2->coeff;
            newnode->exp = t1->exp + t2->exp;
            newnode->next = NULL;

            if(result == NULL){
                result = newnode;
                temp = newnode;
            }
            else{
                temp->next = newnode;
                temp = newnode;
            }

            t2 = t2->next;
        }

        t1 = t1->next;
    }

    return result;
}

int main(){
    printf("The polynomial 1 is :");
    struct node* poly1=NULL;
    poly1 = insert(poly1, 3, 2);
    poly1 = insert(poly1, 2, 1);
    display(poly1);
    printf("The polynomial 2 is :");
    struct node* poly2=NULL;
    poly2 = insert(poly2, 4, 2);
    poly2 = insert(poly2, 5, 1);
    display(poly2);
    printf("The sum is :");
    struct node* sum;
    sum=add(poly1,poly2);
    display(sum);
     struct node* mul=NULL;
     printf("The Multiplication is :");
     mul=multiply(poly1,poly2);
     display(mul);
}