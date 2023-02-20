#include <iostream>
using namespace std;
int binarysearch (int arr[], int n , int x){
    int s = 0, e = n;
    while (s<=e)
    {
    int mid = (s+e)/2;
        if (arr[mid]==x)
        {
            return mid;
        }else if (arr[mid]>x)
        {
             e = mid - 1;
        }
        else{
            s = mid +1;
        }
        
        
    }
        return -1;
    
    

}
int main(){
    int n;
    cout << "Enter the number of elements : ";
    cin >> n ;
    cout<<"Enter the elements : ";
    int arr[n];
    for (int i = 0 ; i< n ; i ++ ){
        cin>>arr[i];
    }
    cout<<"Elements entered by you is : ";
    for (int i = 0 ; i< n ; i++){
        cout <<arr[i]<<" "; 
    }
    cout<<"\nEnter the number you want to search ? ";
    int x; cin >> x;
    cout<<binarysearch(arr, n, x);





}