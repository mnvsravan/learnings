#include <stdio.h>
#include <stdlib.h>

struct node{
    int degree;
    int coeff;
    struct node* next;
};

struct node* p1 = NULL;
struct node* tail1 = NULL;
struct node* ADD=NULL;
struct node* ADDT=NULL;
struct node* MUL=NULL;
struct node* MULT=NULL;
struct node* p2 = NULL;
struct node* tail2 = NULL;

struct node* create(int x,int y){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));

    newnode->coeff = x;
    newnode->degree = y;
    newnode->next = NULL;

    return newnode;
}

void insert1(int x,int y){

    struct node* newnode = create(x,y);

    if(p1 == NULL){
        p1 = newnode;
        tail1 = newnode;
    }
    else{
        tail1->next = newnode;
        tail1 = newnode;
    }
}

void insert2(int x,int y){

    struct node* newnode = create(x,y);

    if(p2 == NULL){
        p2 = newnode;
        tail2 = newnode;
    }
    else{
        tail2->next = newnode;
        tail2 = newnode;
    }
}

void add(struct node*p1,struct node*p2){

    struct node* temp1 = p1;
    struct node* temp2;

    while(temp1 != NULL){

        temp2 = p2;

        while(temp2 != NULL){

            if(temp1->degree == temp2->degree){

                struct node* newnode =
                    create(temp1->coeff + temp2->coeff,
                           temp1->degree);

                if(ADD == NULL){
                    ADD = ADDT = newnode;
                }
                else{
                    ADDT->next = newnode;
                    ADDT = newnode;
                }
            }

            temp2 = temp2->next;
        }

        temp1 = temp1->next;
    }
}

void multiply(struct node* p1, struct node* p2){

    struct node* temp1 = p1;
    struct node* temp2;

    while(temp1 != NULL){

        temp2 = p2;

        while(temp2 != NULL){

            struct node* newnode =
                create(temp1->coeff * temp2->coeff,
                       temp1->degree + temp2->degree);

            if(MUL == NULL){
                MUL = MULT = newnode;
            }
            else{
                MULT->next = newnode;
                MULT = newnode;
            }

            temp2 = temp2->next;
        }

        temp1 = temp1->next;
    }
}
void displayAdd(){

    struct node* temp = ADD;

    while(temp != NULL){

        printf("%dx^%d", temp->coeff, temp->degree);

        if(temp->next != NULL){
            printf(" + ");
        }

        temp = temp->next;
    }

    printf("\n");
}

void displayMul(){

    struct node* temp = MUL;

    while(temp != NULL){

        printf("%dx^%d", temp->coeff, temp->degree);

        if(temp->next != NULL){
            printf(" + ");
        }

        temp = temp->next;
    }

    printf("\n");
}

void display1(){

    struct node* temp = p1;

    while(temp != NULL){
        printf("%dx^%d", temp->coeff, temp->degree);

        if(temp->next != NULL){
            printf(" + ");
        }

        temp = temp->next;
    }

    printf("\n");
}

void display2(){

    struct node* temp = p2;

    while(temp != NULL){
        printf("%dx^%d", temp->coeff, temp->degree);

        if(temp->next != NULL){
            printf(" + ");
        }

        temp = temp->next;
    }

    printf("\n");
}

int main(){

    // P1 = 5x² + 3x + 2
    insert1(5,2);
    insert1(3,1);
    insert1(2,0);

    // P2 = 4x³ + 6x² + 1
    insert2(4,3);
    insert2(6,2);
    insert2(1,0);

    printf("Polynomial 1: ");
    display1();

    printf("Polynomial 2: ");
    display2();
    
    add(p1,p2);
multiply(p1,p2);

printf("Addition: ");
displayAdd();

printf("Multiplication: ");
displayMul();

    return 0;
}