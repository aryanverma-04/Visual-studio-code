#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter no of elements:  ";
    cin>>n;

    int arr[n];
    for (int i = 0; i < n; i++)
    {
       cout<<"Enter element no :"<<arr[i];
       cin>>arr[i];
    }
    for (int i = 0; i < n ; i++)
    {
        cout<<arr[i]<<endl;
    }
    
return 0;
}