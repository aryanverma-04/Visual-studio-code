#include<iostream>
using namespace std;

int linearSearch(int arr[], int n, int key ){
        for (int  i = 0; i < n; i++)
    {
        if (arr[i]==key)
        {
            return i;
        }
        
    }
    return -1;

}
int main(){
    cout<<"Enter the no of elements ";
    int n ;
    cin>>n;
    int arr[n];
    for (int i = 0; i<n; i++){
        cin>>arr[i];
    }
    cout<<"Elements enter by you is ";
    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    cout<<"Enter the element you want to find the index ";
    int key;
    cin>>key;
    cout<<endl;
    cout<<linearSearch(arr, n, key);

    
}