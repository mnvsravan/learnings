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


void preorder(struct node* root){
    if(root != NULL){
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void inorder(struct node* root){
    if(root != NULL){
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

void postorder(struct node* root){
    if(root != NULL){
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}


int countLeaves(struct node* root){
    if(root == NULL)
        return 0;

    if(root->left == NULL && root->right == NULL)
        return 1;

    return countLeaves(root->left) + countLeaves(root->right);
}
int main(){

    insert(50);
    insert(30);
    insert(70);
    insert(20);
    insert(40);
    insert(60);
    insert(80);

    printf("Preorder: ");
    preorder(root);

    printf("\nInorder: ");
    inorder(root);

    printf("\nPostorder: ");
    postorder(root);

    printf("\nNumber of leaf nodes: %d", countLeaves(root));

    return 0;
}