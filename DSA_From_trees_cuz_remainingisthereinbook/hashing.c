// Online C compiler to run C program online
#include <stdio.h>

#define size 10

int hash[size];

// Division Method
int divi(int key){
    return key % size;
}

// Folding Method
int fold(int key){

    int sum = 0;

    while(key != 0){

        sum = sum + (key % 100);

        key = key / 100;
    }

    return sum % size;
}

// Mid Square Method
int mid(int key){

    int square = key * key;

    return (square / 10) % size;
}

// Multiplication Method
int multi(int key){

    float A = 0.618;

    return (int)(size * ((key * A) - (int)(key * A)));
}

// Second Hash Function for Double Hashing
int hash2(int key){

    return 7 - (key % 7);
}

// Function to get hash value
int getHash(int key, int method){

    switch(method){

        case 1:
            return divi(key);

        case 2:
            return fold(key);

        case 3:
            return mid(key);

        case 4:
            return multi(key);

        default:
            return -1;
    }
}

// Insert Function
void insert(int key, int method, int choice){

    int u = getHash(key, method);

    if(u == -1){

        printf("Invalid Hash Function\n");
        return;
    }

    int index;

    for(int i = 0; i < size; i++){

        // Linear Probing
        if(choice == 1){

            index = (u + i) % size;
        }

        // Quadratic Probing
        else if(choice == 2){

            index = (u + i * i) % size;
        }

        // Double Hashing
        else if(choice == 3){

            int step = hash2(key);

            index = (u + i * step) % size;
        }

        else{

            printf("Invalid Collision Method\n");
            return;
        }

        if(hash[index] == -1){

            hash[index] = key;

            printf("Key inserted at index %d\n", index);

            printf("Total Probes = %d\n", i + 1);

            return;
        }
    }

    printf("%d could not be inserted\n", key);
}

// Search Function
void search(int key, int method, int choice){

    int u = getHash(key, method);

    int index;

    for(int i = 0; i < size; i++){

        // Linear Probing
        if(choice == 1){

            index = (u + i) % size;
        }

        // Quadratic Probing
        else if(choice == 2){

            index = (u + i * i) % size;
        }

        // Double Hashing
        else if(choice == 3){

            int step = hash2(key);

            index = (u + i * step) % size;
        }

        if(hash[index] == key){

            printf("Key found at index %d\n", index);

            printf("Total Probes = %d\n", i + 1);

            return;
        }

        if(hash[index] == -1){

            break;
        }
    }

    printf("Key not found\n");
}

// Delete Function
void deleteKey(int key, int method, int choice){

    int u = getHash(key, method);

    int index;

    for(int i = 0; i < size; i++){

        // Linear Probing
        if(choice == 1){

            index = (u + i) % size;
        }

        // Quadratic Probing
        else if(choice == 2){

            index = (u + i * i) % size;
        }

        // Double Hashing
        else if(choice == 3){

            int step = hash2(key);

            index = (u + i * step) % size;
        }

        if(hash[index] == key){

            hash[index] = -1;

            printf("Key deleted from index %d\n", index);

            printf("Total Probes = %d\n", i + 1);

            return;
        }

        if(hash[index] == -1){

            break;
        }
    }

    printf("Key not found\n");
}

// Display Hash Table
void display(){

    printf("\nHash Table:\n");

    for(int i = 0; i < size; i++){

        printf("%d -> %d\n", i, hash[i]);
    }
}

int main(){

    int n, key;
    int method, choice;
    int op;

    // Initialize Hash Table
    for(int i = 0; i < size; i++){

        hash[i] = -1;
    }

    // Choose Hash Function
    printf("Choose Hash Function:\n");

    printf("1. Division Method\n");
    printf("2. Folding Method\n");
    printf("3. Mid Square Method\n");
    printf("4. Multiplication Method\n");

    printf("Enter choice: ");
    scanf("%d", &method);

    // Choose Collision Method
    printf("\nChoose Collision Method:\n");

    printf("1. Linear Probing\n");
    printf("2. Quadratic Probing\n");
    printf("3. Double Hashing\n");

    printf("Enter choice: ");
    scanf("%d", &choice);

    while(1){

        printf("\n--- MENU ---\n");

        printf("1. Insert\n");
        printf("2. Search\n");
        printf("3. Delete\n");
        printf("4. Display\n");
        printf("5. Exit\n");

        printf("Enter choice: ");
        scanf("%d", &op);

        switch(op){

            case 1:

                printf("Enter key to insert: ");
                scanf("%d", &key);

                insert(key, method, choice);

                break;

            case 2:

                printf("Enter key to search: ");
                scanf("%d", &key);

                search(key, method, choice);

                break;

            case 3:

                printf("Enter key to delete: ");
                scanf("%d", &key);

                deleteKey(key, method, choice);

                break;

            case 4:

                display();

                break;

            case 5:

                return 0;

            default:

                printf("Invalid Choice\n");
        }
    }

    return 0;
}