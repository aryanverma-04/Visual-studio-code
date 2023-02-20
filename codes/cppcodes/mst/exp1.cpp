#include <iostream>
using namespace std;
void deletion(int arr[], int n)
{

    cout << "\nEnter element to be delete :: ";
    int del; int count = 0;
    cin >> del;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == del)
        {
            for (int j = i; j < (n - 1); j++)
            {
                arr[j] = arr[j + 1];
            }
            count++;
            break;
        }
    }
    if (count == 0)
    {
        cout << "\nElement not found..!!\n";
    }
    else
    {
        cout << "\nElement deleted successfully..!!\n";
        cout << "\nNow the new array is ::\n";
        for (int i = 0; i < (n - 1); i++)
        {
            cout << arr[i] << " ";
        }
    }
    cout << "\n";
}

int main()
{
    int n, c;
    cout << "Enter the number of elements : ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements : ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    do
    {

        cout << "\n\nType 1 for insertion \n ";
        cout << "Type 2 for deletion \n ";
        cout << "Type 3 for searching \n ";
        cout << "Type 4 for Exit \n  ";

        cout << "Enter your choice : ";
        cin >> c;

        switch (c)
        {
        case 1:
        //    insertion(arr, n);

            break;
        case 2:
            deletion(arr, n);
            break;

        case 3:
            //    searching(arr, n);
            break;
        case 4:
            cout << "You are quiting  ";
            break;

        default:
            cout << "Wrong choice";
        }

    } while (c != 4);

    return 0;
}