#include<stdio.h>
int main()
{
    int array[5];
    int i;
    for(i=0;i<5;i++)
    {
        printf("Enter the value of array[%d]:",i);
        scanf("%d",&array[i]);
    }
    for(i=0;i<5;i++)
    {
        printf("%d\n",array[i]);
    }
    return 0;
}