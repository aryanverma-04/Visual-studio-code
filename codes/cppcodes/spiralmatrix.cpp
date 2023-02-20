#include<iostream>
using namespace std;
int main(){
    int row , col ;
    cout<<"Enter the number of rows :";
    cin>>row;
    cout<<"enter the number of columns : ";
    cin>>col;
    int arr[row][col];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin>>arr[i][j];
        }
        
    }
    cout<<"Matrix entred by you is : "<<endl;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }

    // Implementing spiral order matrix 

    int row_start = 0; 
    int row_end = row-1;
    int col_start = 0;
    int col_end = col-1;
    while (row_start <= row_end && col_start <= col_end)
    {
        // for row start
        for (int col = col_start; col <= col_end; col++)
        {
            cout<<arr[row_start][col]<<" ";
            row_start++;
        }

        //for column end
        for (int row = row_start; row < row_end; row++)
        {
            cout<<arr[row][col_end]<<" ";
            col_end--;
        }

        //for row end
        /*for (int col = col_end; col<=col_start; col--)
        {
            cout<<arr[row_end][col]<<" ";
            row_end--;
        }*/
        
        // for column start 

        /*for (int row = row_end; row >=row_start; row--)
        {
            cout<<arr[row][col_start]<<" ";
            col_start++;
        }*/
        
        
        
    }
    
    

}