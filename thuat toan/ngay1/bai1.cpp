#include <iostream>
using namespace std;
// tính tính các phần tử trong mảng
int n, s=1;

int main()
{
    cin >> n; // nhập vào n
    int a[n]; // 0-n
    for (int i = 0; i <= n - 1; i++)
    {
        cin >> a[i]; // nhập số i vào mảng a //vd: n=3 ta nhập i lần lượt là 3 4 5
        cout << "\nso vua nhap la " << a[i] << endl;
    }

    s = 1;
    for (int i = 0; i <= n - 1; i++)
    {
        cout << a[i] << "*" << s;
        s = s * a[i];
        cout << "=" << s << endl;
    }
    // Minh họa tuần tự:
    //  Giả sử bạn nhập n = 3 và các giá trị 2, 3, 4.

    // Vòng lặp đầu tiên (Nhập dữ liệu):

    // Lần 1: Nhập a[0] = 2.
    // Lần 2: Nhập a[1] = 3.
    // Lần 3: Nhập a[2] = 4.
    // Kết quả: Mảng a lưu trữ [2, 3, 4].
    // Vòng lặp thứ hai (Tính toán):

    // Lần 1: Lấy a[0] = 2, tính s = 1 * 2 = 2.
    // Lần 2: Lấy a[1] = 3, tính s = 2 * 3 = 6.
    // Lần 3: Lấy a[2] = 4, tính s = 6 * 4 = 24.
}
