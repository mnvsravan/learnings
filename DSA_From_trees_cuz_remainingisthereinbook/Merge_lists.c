#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

// Create node easily using temp pointer
struct node* createList(int arr[], int n) {
    struct node *head = NULL, *temp = NULL;

    for (int i = 0; i < n; i++) {
        struct node* newnode = (struct node*)malloc(sizeof(struct node));
        newnode->data = arr[i];
        newnode->next = NULL;

        if (head == NULL) {
            head = newnode;
            temp = newnode;
        } else {
            temp->next = newnode;
            temp = temp->next;   // ⭐ your style
        }
    }
    return head;
}

// Count nodes
int countNodes(struct node* head) {
    int count = 0;
    struct node* temp = head;

    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}

// Copy LL to array
void listToArray(struct node* head, int arr[]) {
    int i = 0;
    struct node* temp = head;

    while (temp != NULL) {
        arr[i++] = temp->data;
        temp = temp->next;   // ⭐ your style
    }
}

// Bubble Sort (array)
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int t = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = t;
            }
        }
    }
}

// Print array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d -> ", arr[i]);
    printf("NULL\n");
}

// Main
int main() {
    int a[] = {3, 1, 5};
    int b[] = {2, 4, 6};

    struct node* l1 = createList(a, 3);
    struct node* l2 = createList(b, 3);

    // Merge (just connect)
    struct node* temp = l1;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = l2;

    // Count total nodes
    int n = countNodes(l1);

    int arr[100];  // enough size

    // Copy to array
    listToArray(l1, arr);

    // Sort
    bubbleSort(arr, n);

    // Output
    printArray(arr, n);

    return 0;
}