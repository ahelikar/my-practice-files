#include<stdio.h>
int binsearch(int low,int high,int b[],int x);
int main()
{
    int b[]={3,6,9,10,11,12};
    int n=sizeof(b)/sizeof(b[0]);
    int x=10;
    int result=binsearch(0,n-1,b,x);
    if(result==-1)
    {
        printf("Element is not present in array:");
    }
    else{
printf("Element is present in array");
    }
    return 0;
    }
    int binsearch(int low,int high,int b[],int x)
    {
while(low<=high)
{
    int mid=low+(high-low)/2;
    if(b[mid]==x)
    {
        return mid;

    }
    else if(b[mid]<x)
    {
        low=mid+1;
    }
    else{
        high=mid-1;
    }
    return -1;
}
    }
