#include <iostream>
using namespace std;

void quickSort(int a[], int left, int right)
{
    if (left < right)
    {
        int pivot = a[(left + right) / 2]; // sử dụng mid làm pivot
        int i = left, j = right;

        while (i <= j)
        {
            // dò các phần tử nằm bên trái pivot
            while (a[i] < pivot)
            {
                i++;
            }
            // dò các phần tử nằm bên phải pivot
            while (a[j] > pivot)
            {
                j--;
            }

            //chỉ khi i>j thì mới không swap
            if (i <= j)
            {
                swap(a[i], a[j]); // Swap
                i++;
                j--;
            }
        }// kết thúc quá trình swap

        if (left < j)
        {
            quickSort(a, left, j); // đệ quy 
        }
        if (i < right)
        {
            quickSort(a, i, right); // đệ quy
        }
    }
}

int main()
{
    // tạo mảng a
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    int a[n];
    cout << "Nhap cac phan tu: ";
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

// call quicksoft
    quickSort(a, 0, n - 1); // quicksoft (mảng a, phần tử left, phần tử right)

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;

    return 0;
}
