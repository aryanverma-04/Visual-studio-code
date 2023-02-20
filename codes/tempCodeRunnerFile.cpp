#include <bits/stdc++.h>
using namespace std;
// using bubble sort to sort an array
void bubbleSort(int arr[], int n)
{
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++)
    {
        swapped = false;
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        // IF no two elements were swapped
        // by inner loop, then break
        if (swapped == false)
            break;
    }
}
// Function to print an array
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << " " << arr[i];
}
// Function to get multiplication
int findmult(int ksmall, int klarge)
{
    return ksmall * klarge;
}
int main()
{
    int k;
    int arr[] = {5, 3, 1, 9, 8, 2, 4, 7};
    int N = sizeof(arr) / sizeof(arr[0]);
    cout << "The array is :";
    printArray(arr, N);
    bubbleSort(arr, N);
    cout << "\nSorted array is :";
    printArray(arr, N);
    cout << "\n\nEnter the value of k: ";
    cin >> k;
    int ksmall = arr[k - 1];
    int klarge = arr[N - k];
    cout << "\n\nKth Smallest Element " << ksmall << endl;
    cout << "\nKth largest Element = " << klarge << endl;
    cout << "\nMultiplication is  = " << findmult(ksmall, klarge) << endl;
    return 0;
}