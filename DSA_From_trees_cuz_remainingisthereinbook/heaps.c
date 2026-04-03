// Online C compiler to run C program online
#include <stdio.h>
#define N 100
int heap[N];
int size=0;
void insert(int x){
    size++;
    int i=size;
    heap[i]=x;
    while(i>1 && heap[i]>heap[i/2]){
        int temp=heap[i];;
        heap[i]=heap[i/2];
        heap[i/2]=temp;
        i=i/2;
    }
}
void display(int arr[], int size){
    for (int i=1;i<=size;i++){
        printf("%d \t",arr[i]);
    }
}
void deleteRoot(){
    if(size == 0){
        printf("Heap is empty\n");
        return;
    }

    int max = heap[1];   // store root (optional)

    heap[1] = heap[size];
    size--;

    int i = 1;
    while(2*i <= size){
        int left = 2*i;
        int right = 2*i + 1;
        int largest = i;

        if(left <= size && heap[left] > heap[largest])
            largest = left;

        if(right <= size && heap[right] > heap[largest])
            largest = right;

        if(largest != i){
            int temp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = temp;
            i = largest;
        }
        else{
            break;
        }
    }

    printf("Deleted element: %d\n", max);
}
int main() {
   insert(34);
    insert(54);
     insert(24);
      insert(87);
       insert(42);
        insert(65);
        display(heap,size);
        deleteRoot();
        deleteRoot();
        display(heap,size);

    return 0;
}