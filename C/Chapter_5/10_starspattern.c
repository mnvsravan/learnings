#include <stdio.h>
int main() {
    int n;
    for(n=0;n<3;n++){
        for(int j=0;j<2*n+1;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

