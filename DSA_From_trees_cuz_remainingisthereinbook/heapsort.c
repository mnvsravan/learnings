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
void swap(int arr[], int i, int j){
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}
void heapify(int arr[],int n, int i){
    int largest=i;
    int left= 2*i;
    int right=2*i+1;
    
        if(left <= n && arr[left] > arr[largest])
            largest = left;

        if(right <= n && arr[right] > arr[largest])
            largest = right;

        if(largest != i){
           swap(arr,i,largest);
           heapify(arr,n,largest);
}
}
void heapsort(int arr[],int n){
    for(int i=n/2; i>=1;i--){
        heapify(arr,n,i);
    }
    for(int i=n;i>=1;i--){
        swap(arr,i,1);
        heapify(arr,i-1,1);
    }
}

int main() {
   insert(34);
    insert(54);
     insert(24);
      insert(87);
       insert(42);
        insert(65);
        display(heap,size);
        heapsort(heap,size);
        display(heap,size);

    return 0;
}