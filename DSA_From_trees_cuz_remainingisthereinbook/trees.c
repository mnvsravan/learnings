#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* root = NULL;

struct node* create(int x){
    struct node* cre = (struct node*)malloc(sizeof(struct node));
    cre->data = x;
    cre->left = NULL;
    cre->right = NULL;
    return cre;
}

void insert(int x){

    struct node* newnode1 = create(x);

    if(root == NULL){
        root = newnode1;
        return;
    }

    struct node* temp = root;

    while(temp != NULL){

        if (x < temp->data){

            if (temp->left == NULL){
                temp->left = newnode1;
                break;
            }
            temp = temp->left;
        }
        else{

            if (temp->right == NULL){
                temp->right = newnode1;
                break;
            }
            temp = temp->right;
        }
    }
}

void inorder(struct node *root){
    if (root != NULL){
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

void deleteNode(int x)
{
    struct node *temp = root;
    struct node *parent = NULL;

    // 🔎 Find the node
    while (temp != NULL && temp->data != x)
    {
        parent = temp;

        if (x < temp->data)
            temp = temp->left;
        else
            temp = temp->right;
    }

    if (temp == NULL)
    {
        printf("Value not found\n");
        return;
    }

    // 🔥 Case 1: Leaf node
    if (temp->left == NULL && temp->right == NULL)
    {
        if (parent == NULL)  // deleting root
            root = NULL;
        else if (parent->left == temp)
            parent->left = NULL;
        else
            parent->right = NULL;

        free(temp);
    }

    // 🔥 Case 2: One child (left)
    else if (temp->left != NULL && temp->right == NULL)
    {
        if (parent == NULL)  // deleting root
            root = temp->left;
        else if (parent->left == temp)
            parent->left = temp->left;
        else
            parent->right = temp->left;

        free(temp);
    }

    // 🔥 Case 3: One child (right)
    else if (temp->left == NULL && temp->right != NULL)
    {
        if (parent == NULL)  // deleting root
            root = temp->right;
        else if (parent->left == temp)
            parent->left = temp->right;
        else
            parent->right = temp->right;

        free(temp);
    }

    // 🔥 Case 4: Two children
    else
    {
        struct node *succ = temp->right;
        struct node *succParent = temp;

        while (succ->left != NULL)
        {
            succParent = succ;
            succ = succ->left;
        }

        // Copy successor value
        temp->data = succ->data;

        // Delete successor
        if (succParent->left == succ)
            succParent->left = succ->right;
        else
            succParent->right = succ->right;

        free(succ);
    }
}

int main(){

    insert(50);
    insert(45);
    insert(35);
    insert(25);
    insert(75);
    insert(65);

    printf("Inorder before deletion: ");
    inorder(root);

    deleteNode(65);

    printf("\nInorder after deletion: ");
    inorder(root);

    return 0;
}