#include <stdio.h>

#define N 100

int heap[N];
int size = 0;

void insert(int x) {
    size++;
    int i = size;
    heap[i] = x;

    while(i > 1 && heap[i] > heap[i/2]) {
        int temp = heap[i];
        heap[i] = heap[i/2];
        heap[i/2] = temp;

        i = i / 2;
    }
}

void display(int heap[], int size) {
    for(int i = 1; i <= size; i++) {
        printf("%d\t", heap[i]);
    }
}

void swap(int heap[], int i, int j) {
    int temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
}
void delete(){
    int max = heap[1];

    heap[1] = heap[size];
    size--;

    int i = 1;

    while(2*i <= size){

        int large = i;
        int left = 2*i;
        int right = 2*i + 1;

        if(left <= size && heap[left] > heap[large]){
            large = left;
        }

        if(right <= size && heap[right] > heap[large]){
            large = right;
        }

        if(large != i){
            int temp = heap[i];
            heap[i] = heap[large];
            heap[large] = temp;

            i = large;
        }
        else{
            break;
        }
    }
}

void heapify(int heap[], int size, int i) {

    int large = i;
    int left = 2 * i;
    int right = 2 * i + 1;

    if(left <= size && heap[left] > heap[large]) {
        large = left;
    }

    if(right <= size && heap[right] > heap[large]) {
        large = right;
    }

    if(large != i) {
        swap(heap, i, large);
        heapify(heap, size, large);
    }
}

void heapsort(int heap[], int size) {

    for(int i = size/2; i >= 1; i--) {
        heapify(heap, size, i);
    }

    for(int i = size; i > 1; i--) {
        swap(heap, 1, i);
        heapify(heap, i - 1, 1);
    }
}

int main() {

    insert(36);
    insert(65);
    insert(76);
    insert(86);
    insert(54);
    insert(87);

    heapsort(heap, size);

    display(heap, size);

    return 0;
}


#include <stdio.h>

#define N 100

int arr[N];

int max(int arr[], int size) {
    int x = arr[0];

    // Fixed: started loop from 1 instead of 0
    for(int i = 1; i < size; i++) {
        if(arr[i] > x) {
            x = arr[i];
        }
    }

    return x;
}

// Fixed: renamed function from count() to countDigits()
// because count[] array was also used later
int countDigits(int x) {

    int t = 0;

    while(x != 0) {
        t++;

        // Fixed: x = x % 10 was wrong
        // It should be x = x / 10
        x = x / 10;
    }

    return t;
}

void radixSort(int arr[], int size) {

    // Fixed: max(arr) needed size argument
    int m = max(arr, size);

    // Fixed: count(max) was wrong
    int passes = countDigits(m);

    int b[10][N];

    // Fixed: count variable name conflicted with function name
    int count[10];

    int ex = 1;

    for(int p = 0; p < passes; p++) {

        // Fixed: reset count array every pass
        for(int i = 0; i < 10; i++) {
            count[i] = 0;
        }

        // Fixed: for(int 1=0;i<n;i++) was invalid syntax
        // Also n was undefined, replaced with size
        for(int i = 0; i < size; i++) {

            int digit = (arr[i] / ex) % 10;

            b[digit][count[digit]] = arr[i];
            count[digit]++;
        }

        int k = 0;

        for(int i = 0; i < 10; i++) {

            for(int j = 0; j < count[i]; j++) {

                arr[k] = b[i][j];
                k++;
            }
        }

        // Fixed: ex = ex * 10 should be inside loop
        ex = ex * 10;
    }
}

void display(int arr[], int size) {

    // Fixed: for(int i=;,i<size,i++) invalid syntax
    for(int i = 0; i < size; i++) {
        printf("%d\t", arr[i]);
    }
}

int main() {

    int size;

    printf("Enter size: ");
    scanf("%d", &size);

    for(int i = 0; i < size; i++) {

        // Fixed: better display format
        printf("Enter element %d: ", i + 1);

        scanf("%d", &arr[i]);
    }

    // Fixed: radixSort function was not called
    radixSort(arr, size);

    printf("\nSorted Array:\n");

    // Fixed: display function was not called
    display(arr, size);

    return 0;
}



// Online C compiler to run C program online
#include <stdio.h>

#define N 100

void swap(int arr[], int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void shellSort(int arr[], int size) {

    // Fixed: gap-- changed to gap/=2
    for(int gap = size / 2; gap >= 1; gap /= 2) {

        for(int j = gap; j < size; j++) {

            // Fixed: i-gap changed to i-=gap
            for(int i = j - gap; i >= 0; i -= gap) {

                if(arr[i] > arr[i + gap]) {

                    // Fixed: wrong arguments in swap
                    // swap(arr,arr[i],arr[j]) -> swap(arr,i,i+gap)
                    swap(arr, i, i + gap);

                } else {
                    break;
                }
            }
        }
    }
}

void display(int arr[], int size) {

    for(int i = 0; i < size; i++) {
        printf("%d\t", arr[i]);
    }
}

int main() {

    int size;
    int arr[N];

    printf("Enter size: ");
    scanf("%d", &size);

    for(int i = 0; i < size; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    shellSort(arr, size);

    printf("Sorted array:\n");
    display(arr, size);

    return 0;
}