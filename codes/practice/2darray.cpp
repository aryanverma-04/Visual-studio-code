#include <iostream>
using namespace std;
int main()
{
    int m, n;
    int arr[m][n];
    cin >> m
;    cin >> n;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; i < n; j++)
        {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; i < n; j++)
        {
            cout << arr[i][j];
        }
        cout << endl;
    }
}
