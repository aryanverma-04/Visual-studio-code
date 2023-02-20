#include <iostream>
using namespace std;
int main()
{
    int n, m;
    int arr[n][m];
    cout << "Enter the number of rows : ";
    cin >> n;
    cout<<"Enter the number of columns : ";
    cin>>m;
    cout<<n<<"  "<<m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
cout<<arr[0][0]<<endl;
cout<<arr[0][1]<<endl;
cout<<arr[1][0]<<endl;
cout<<arr[1][1]<<endl;
   /* cout << "Matrix entered by you is -> \n";

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }*/
}