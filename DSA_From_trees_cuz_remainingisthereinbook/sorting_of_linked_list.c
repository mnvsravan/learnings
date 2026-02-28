#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

// Insert at end
struct node* insert(struct node* head, int value){

    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;

    if(head == NULL){
        return newnode;
    }

    struct node* temp = head;
    while(temp->next != NULL){
        temp = temp->next;
    }

    temp->next = newnode;
    return head;
}

// Display
void display(struct node* head){
    while(head != NULL){
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

// Arrange (Simple Bubble Sort)
void arrange(int arr[], int n){

    int i, j, temp;

    for(i = 0; i < n-1; i++){
        for(j = 0; j < n-i-1; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main(){

    struct node* list1 = NULL;
    struct node* list2 = NULL;
    struct node* merged = NULL;

    // First linked list
    list1 = insert(list1, 3);
    list1 = insert(list1, 1);
    list1 = insert(list1, 5);

    // Second linked list
    list2 = insert(list2, 4);
    list2 = insert(list2, 2);
    list2 = insert(list2, 6);

    int arr[50];
    int count = 0;
    struct node* temp;

    // Copy list1 elements to array
    temp = list1;
    while(temp != NULL){
        arr[count] = temp->data;
        count++;
        temp = temp->next;
    }

    // Copy list2 elements to array
    temp = list2;
    while(temp != NULL){
        arr[count] = temp->data;
        count++;
        temp = temp->next;
    }

    // Sort all elements
    arrange(arr, count);

    // Create new sorted merged list
    int i;
    for(i = 0; i < count; i++){
        merged = insert(merged, arr[i]);
    }

    printf("Merged Sorted List: ");
    display(merged);

    return 0;
}