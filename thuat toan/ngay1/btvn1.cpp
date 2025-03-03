#include <iostream>
using namespace std;

int main()
{
    int n, m, remain = 0;
   
    cout << "Nhap so ve ca nhac: ";
    cin >> n;
    cout << "Nhap so nguoi: ";
    cin >> m;

    int a[n]; // Gia ve
    int b[m]; // Gia mua cua tung nguoi cho tung ve

    for (int i = 0; i < n; ++i)
    {
        cout << "Nhap gia ve thu " << i + 1 << ": ";
        cin >> a[i];

        int max_cost = a[i]; // Khoi tao gia cao nhat ban dau la gia ve
        int winner = -1;     // Luu nguoi mua duoc ve

        for (int j = 0; j < m; ++j)
        {
            cout << "Nguoi " << j + 1 << " ra gia cho ve " << i + 1 << ": ";
            cin >> b[j];

            if (b[j] > max_cost)
            {
                max_cost = b[j];
                winner = j; // Cap nhat nguoi mua duoc ve
            }
        }
        if (winner != -1)
        {
            cout << "Nguoi mua duoc ve " << i + 1 << " la nguoi " << winner + 1 << " voi gia " << max_cost << "$" << endl;
        }
        else
        {
            cout << winner << endl;
            remain++;
        }
    }
    cout << "ket thuc" << endl;
    cout << "ton kho: " << remain;

    return 0;
}