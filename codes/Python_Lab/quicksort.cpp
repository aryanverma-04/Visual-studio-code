#include<iostream>
using namespace std;
void quicksort(int arr[],int first,int last)
{
    int i,j,pivot,temp;
    if(first<last)
    {
        pivot=first;
        i=first;
        j=last;

        while(i<j)
        {
            while(arr[i]<=arr[pivot]&&i<last)
            {
               i++;
            }
               while (arr[j]>arr[pivot])
               {
                   j--;
               }
               if(i<j)
               {
                   temp=arr[i];
                   arr[i]=arr[j];
                   arr[j]=temp;
               }
    
            
        }
        temp=arr[pivot];
        arr[pivot]=arr[j];
        arr[j]=temp;
        quicksort(arr,first,j-1);
        quicksort(arr,j+1,last);
    }
}
int main()
{
    cout<<"\nName: Aryan verma, UID: 20Bcs3651 "<<endl;
    cout<<"This is an program to implement quick sort"<<endl;
    int i, n;
    cout<<"\nEnter size of array: ";
    cin>>n;
    int arr[n];
    cout<<"Enter elements of array: "; 
    for(i=0;i<n;i++)
    {
        cin>>arr[i];

    }
    
    quicksort(arr,0,n-1);
    cout<<"After Sorting: ";
    for(i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}