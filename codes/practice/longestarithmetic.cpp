#include <iostream>
using namespace std;
int main()
{
    int n, arr[n];
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int ans = 2;
    int pd = arr[1] - arr[0];
    int curr = 2;
    int j = 2;
    while (j < n)
    {
        if (arr[j] - arr[j - 1] == pd)
        {
            curr++;
        }
        else
        {
            pd = arr[j] - arr[j - 1];
            curr = 2;
        }
        ans = max(ans, curr);
        j++;
    }
    cout<<"The longest srithmetic subarray is : ";
    cout<<ans;

}