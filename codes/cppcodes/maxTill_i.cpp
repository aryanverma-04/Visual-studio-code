#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int mx = -99999999;
    for (int i = 0; i < n; i++)
    {
        mx = max(arr[i], mx);
        cout << mx << " ";
    }
}

#include <iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter the size of array : ";
    cin>>n;
    int arr[n];
    for (int i = 0 ; i < n ; i ++ ){
        cin>>arr[i];
    }
    for (int i = 0 ; i < n ; i++){
        int mx = -100000;
        mx = max(arr[i], mx);
        cout << mx<< endl;
    }
    return 0;
}