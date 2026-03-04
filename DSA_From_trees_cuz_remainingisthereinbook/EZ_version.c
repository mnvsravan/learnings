#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* root = NULL;

// Insert function
void insert(int x){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = x;
    newnode->left = NULL;
    newnode->right = NULL;

    // If tree is empty
    if(root == NULL){
        root = newnode;
        return;
    }

    struct node* temp = root;
    struct node* parent = NULL;

    // Traverse the tree
    while(temp != NULL){
        parent = temp;

        if(x < temp->data){
            temp = temp->left;
        }
        else{
            temp = temp->right;
        }
    }

    // Insert at correct position
    if(x < parent->data){
        parent->left = newnode;
    }
    else{
        parent->right = newnode;
    }
}

void find(int x){
    struct node* temp = root;
    struct node* parent = NULL;

    while(temp != NULL){

        if(x == temp->data){
            if(parent == NULL)
                printf("%d is root node\n", x);
            else
                printf("Parent of %d is %d\n", x, parent->data);
            return;
        }

        parent = temp;

        if(x < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }

    printf("Element not found\n");
}

void delete(int x)
{
    struct node* temp = root;
    struct node* parent = NULL;

    // Find node
    while (temp != NULL && temp->data != x)
    {
        parent = temp;

        if (x > temp->data)
        {
            temp = temp->right;
        }
        else
        {
            temp = temp->left;
        }
    }

    if (temp == NULL)
    {
        printf("DATA NOT FOUND\n");
        return;
    }

    // ✅ Case 1: No child
    if (temp->left == NULL && temp->right == NULL)
    {
        if (parent == NULL)
        {
            root = NULL;
        }
        else if (parent->left == temp)
        {
            parent->left = NULL;
        }
        else
        {
            parent->right = NULL;
        }

        free(temp);
    }

    // ✅ Case 2: One child
    else if (temp->right == NULL || temp->left == NULL)
    {
        struct node* child;

        if (temp->right != NULL)
        {
            child = temp->right;
        }
        else
        {
            child = temp->left;
        }

        if (parent == NULL)
        {
            root = child;
        }
        else if (parent->left == temp)
        {
            parent->left = child;
        }
        else
        {
            parent->right = child;
        }

        free(temp);
    }

    // ✅ Case 3: Two children
    else
    {
        struct node* lefttree = temp->left;
        struct node* righttree = temp->right;

        struct node* s1 = lefttree;

        // find rightmost of left subtree
        while (s1->right != NULL)
        {
            s1 = s1->right;
        }

        // attach right subtree
        s1->right = righttree;

        if (parent == NULL)
        {
            root = lefttree;
        }
        else if (parent->left == temp)
        {
            parent->left = lefttree;
        }
        else
        {
            parent->right = lefttree;
        }

        free(temp);
    }
}






// Inorder Traversal (Display)
void display(struct node* root){
    if(root != NULL){
        display(root->left);
        printf("%d ", root->data);
        display(root->right);
    }
}



int main() {

    insert(50);
    insert(30);
    insert(70);
    insert(20);
    insert(40);
    insert(60);
    insert(80);
    find(80);
    delete(50);
    delete(40);

    printf("Inorder Traversal: ");
    display(root);

    return 0;
}