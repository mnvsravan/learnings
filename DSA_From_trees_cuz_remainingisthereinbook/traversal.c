#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* root = NULL;   // Global root

// Create and insert node (BST style)
void insert(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->left = NULL;
    newnode->right = NULL;

    if(root == NULL){
        root = newnode;
        return;
    }

    struct node* temp = root;
    struct node* parent = NULL;

    while(temp != NULL){
        parent = temp;

        if(value < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }

    if(value < parent->data)
        parent->left = newnode;
    else
        parent->right = newnode;
}
void inorder(){

    struct node* stack[100];
    int top = -1;
    struct node* temp = root;

    while(temp != NULL || top != -1){

        while(temp != NULL){
            top++;
            stack[top] = temp;
            temp = temp->left;
        }

        temp = stack[top];
        top--;

        printf("%d ", temp->data);
        temp = temp->right;
    }
}
void preorder(){

    if(root == NULL)
        return;

    struct node* stack[100];
    int top = -1;

    top++;
    stack[top] = root;

    while(top != -1){

        struct node* temp = stack[top];
        top--;

        printf("%d ", temp->data);

        if(temp->right != NULL){
            top++;
            stack[top] = temp->right;
        }

        if(temp->left != NULL){
            top++;
            stack[top] = temp->left;
        }
    }
}
void postorder(){

    if(root == NULL)
        return;

    struct node* stack1[100];
    struct node* stack2[100];
    int top1 = -1;
    int top2 = -1;

    top1++;
    stack1[top1] = root;

    while(top1 != -1){

        struct node* temp = stack1[top1];
        top1--;

        top2++;
        stack2[top2] = temp;

        if(temp->left != NULL){
            top1++;
            stack1[top1] = temp->left;
        }

        if(temp->right != NULL){
            top1++;
            stack1[top1] = temp->right;
        }
    }

    while(top2 != -1){
        printf("%d ", stack2[top2]->data);
        top2--;
    }
}
int main(){

    insert(50);
    insert(30);
    insert(70);
    insert(20);
    insert(40);
    insert(60);
    insert(80);

    printf("Inorder (Non-Recursive): ");
    inorder();

    printf("\nPreorder (Non-Recursive): ");
    preorder();

    printf("\nPostorder (Non-Recursive): ");
    postorder();

    return 0;
}