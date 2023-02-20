#include<iostream>
using namespace std;
int main(){
    int count;
    cin>>count;
    int arr[count];
    for ( int i = 0; i < count; i++)
    {
        cin>>arr[i];
    }
    for (int i = 0; i < count; i++)
    {
        cout<<arr[i];
    }
    int x;
    cin>>x;
    for (int i = 0; i < count; i++)
    {
        if (arr[i]==x)
        {
            cout<<arr[i];
        }
        else{
            cout<<"Element not found !";
        }
        
    }
    
    
    
}