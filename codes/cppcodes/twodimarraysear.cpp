#include<iostream>
using namespace std;
int main(){
    cout<<"Enter the number of rows and columns :";
    int rows, columns ;
    cin>>rows>>columns;
    int arr[rows][columns];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            cin>>arr[i][j];
        }
        
    }
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;    
    }
    cout<<"Enter the number to search : ";
    int x; cin>>x;
    bool check;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (arr[i][j]==x)
            {
                check =true;
                cout<<"index of searched element is :"<<i<<" "<<j;
            }          
        
        }
    }

    if (check != true)
    {
        cout<<"ELement not found";
    }
    
    return 0;
    
}