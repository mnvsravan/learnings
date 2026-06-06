// Online C compiler to run C program online
#include <stdio.h>

#define N 100

int graph[N][N];
int visited[N];
int stack[N];
int top = -1;
int n;

void push(int x) {
    top++;
    stack[top] = x;
}

int pop() {
    int k = stack[top];
    top--;
    return k;
}

void dfs(int start) {

    push(start);

    while(top != -1) {

        int v = pop();

        if(visited[v] != 1) {

            printf("%d ", v);
            visited[v] = 1;

            for(int i = 0; i < n; i++) {

                // Fixed: visited[v] changed to visited[i]
                if(graph[v][i] == 1 && visited[i] != 1) {
                    push(i);
                }
            }
        }
    }
}
int Q[N];
int front =-1;
int rear = -1;
void enQ(int x) {

    if(front == -1 && rear == -1) {
        front = 0;
        rear = 0;
        Q[rear] = x;
    }
    else {

        rear++;

        Q[rear] = x;
    }
}

int deQ() {

    int k = Q[front];

    if(front == rear) {
        front = -1;
        rear = -1;
    }
    else {
        front++;
    }
    return k;
}

void bfs(int start) {

    enQ(start);

    while(front != -1) {

        int v = deQ();

        if(visited[v] != 1) {

            printf("%d ", v);
            visited[v] = 1;

            for(int i = 0; i < n; i++) {

                // Fixed: visited[v] changed to visited[i]
                if(graph[v][i] == 1 && visited[i] != 1) {
                    enQ(i);
                }
            }
        }
    }
}

int main() {

    int start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    // Initialize visited array
    for(int i = 0; i < n; i++) {
        visited[i] = 0;
    }

    printf("Enter starting vertex: ");
    scanf("%d", &start);

    printf("DFS Traversal: ");
    dfs(start);

    return 0;
}