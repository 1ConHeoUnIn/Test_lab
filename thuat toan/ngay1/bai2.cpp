#include <iostream>
using namespace std;
// tìm số lớn nhất trong mảng
int n, s=0;

int main()
{
    cin >> n; // nhập vào n
    int a[n]; // 0-n
    for (int i = 0; i <= n - 1; i++)
    {
        cin >> a[i]; // nhập số i vào mảng a //vd: n=3 ta nhập i lần lượt là 3 4 5
        cout << "\nso vua nhap la " << a[i] << endl;
    }

    for (int i = 0; i <= n-1; i++)
    {
        if (a[i] > s)
        {
            s = a[i];
            cout << "\n so lon nhat : " << s;
        }
        //    else
        //    {
        //        s = s + 0;
        //        cout << "\nso lon nhat : " << s;
        //    }
    }
    cout << "\nso lon nhat : " << s;
}