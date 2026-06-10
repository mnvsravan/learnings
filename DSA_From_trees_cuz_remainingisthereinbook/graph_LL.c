#include <stdio.h>
#include <stdlib.h>
#define N 100
struct node{
    int data;
    struct node* next;
};
struct node*adj[N];
int visited[N];
int stack[N];
int top=-1;
int n;
void push(int x){
    top++;
    stack[top]=x;
}
int pop(){
    int t=stack[top];
    top--;
    return t;
}
struct node* create(int x){
    struct node*newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=x;
    newnode->next=NULL;
    return newnode;
}

void addEdge(int u, int v){
    if(adj[u]==NULL){
        adj[u]=create(v);
    }
    else{
        struct node*temp=adj[u];
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=create(v);
    }
}
void dfs(int start){
    push(start);
    while(top!=-1){
        int v=pop();
        if(visited[v]==0){
            printf("%d",v);
            visited[v]=1;
        
        struct node* temp=adj[v];
        while(temp!=NULL){
            if(visited[temp->data]==0){
                push(temp->data);
            }
            temp=temp->next;
        }
    }
  }
}

int Q[10];
int front = -1;
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

// Dequeue
int deQ() {

    int x = Q[front];

    if(front == rear) {

        front = -1;
        rear = -1;
    }
    else {
        front++;
    }

    return x;
}

// BFS Traversal
void bfs(int start) {

    enQ(start);

    while(front != -1) {

        int v = deQ();

        if(visited[v] == 0) {

            printf("%d ", v);

            visited[v] = 1;

            struct node* temp = adj[v];

            while(temp != NULL) {

                if(visited[temp->data] == 0) {
                    enQ(temp->data);
                }

                temp = temp->next;
            }
        }
    }
}

int main() {

    int edges;
    int start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    // Initialize adjacency list
    for(int i = 0; i < n; i++) {
        adj[i] = NULL;
    }

    // Initialize visited array
    for(int i = 0; i < n; i++) {
        visited[i] = 0;
    }

    printf("Enter number of edges: ");
    scanf("%d", &edges);

    // Input edges
    for(int i = 0; i < edges; i++) {

        int u, v;

        printf("Enter edge (u v): ");
        scanf("%d %d", &u, &v);

        // Undirected graph
        addEdge(u, v);
        addEdge(v, u);
    }

    printf("Enter starting vertex: ");
    scanf("%d", &start);

    printf("DFS Traversal: ");

    dfs(start);

    return 0;
}