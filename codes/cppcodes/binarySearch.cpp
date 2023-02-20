#include<iostream>
using namespace std;
int binarySearch(int arr[],int n,int key){
    int s = 0;
    int e = n;
    while(s<=e)
    {
        int mid = (s+e)/2;
        if (arr[mid]==key)
        {
          return mid;
        }
        else if (arr[mid]>key)
        {
            e= mid-1;
            
        }
        else{
            s = mid+1;
        }
        
        


    }
    return -1;

}
int main(){
    cout<<"\nAryan verma, UID: 20BCS3651"<<endl;
    cout<<"Enter the number of elements: ";
    int n;
    cin>>n;
    int arr[n];
    for (int i=0; i<n; i++){
        cin>>arr[i];
    }
    cout<<"Enter element to search"<<endl;
    int key;
    cin>>key;
    int ans = binarySearch(arr,n,key);
    if (ans == -1)
    {
        cout<<"Element not found !!"<<endl;
    }
    else{
        cout<<"The element is found at index :"<<ans;
    }
}