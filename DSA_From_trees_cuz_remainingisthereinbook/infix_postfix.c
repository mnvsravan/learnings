
#include <stdio.h>

char stack[100];
int size = -1;

void push(char c){
    size++;
    stack[size] = c;
}

char pop(){
    char c;
    c = stack[size];
    size--;
    return c;
}

int priority(char c){
    if(c=='+' || c=='-'){
        return 1;
    }
    else if(c=='*' || c=='/'){
        return 2;
    }
    return 0;
}

int main() {

char infix[100];
char postfix[100];
int size1;
int size2 = 0;
int i = 0;

printf("size of infix ? ");
scanf("%d",&size1);

for(i=0; i<size1; i++){
    scanf(" %c",&infix[i]);
}

i = 0;

while(i < size1){

     if((infix[i]>='A' && infix[i]<='Z') || (infix[i]>='a' && infix[i]<='z') || (infix[i]>='0' && infix[i]<='9')){
            postfix[size2] = infix[i];
            size2++;
        }

    else if(infix[i]=='('){
        push(infix[i]);
    }

    else if(infix[i]==')'){
        while(stack[size] != '('){
            postfix[size2] = pop();
            size2++;
        }
        pop();
    }

    else{
         while(size!=-1 && priority(stack[size]) >= priority(infix[i])){
                postfix[size2] = pop();
                size2++;
            }
            push(infix[i]);
        }

    i++;
}

/* AFTER the loop ends */
while(size != -1){
    postfix[size2] = pop();
    size2++;
}

    printf("Displaying postfix\n");
    for(i=0; i<size2; i++){
        printf("%c",postfix[i]);
    }

    return 0;
}