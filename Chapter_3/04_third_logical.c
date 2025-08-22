#include <stdio.h>

int main()
{
    int a = 1;
    int b = 1;
    printf("The vale of a and b is %d\n", a && b);
    printf("The vale of a or b is %d\n", a || b);
    printf("The value of not(a) is %d\n", !a);
    if (a && b)
    printf("Both a and b are true.\n");
    return 0;
}
    

