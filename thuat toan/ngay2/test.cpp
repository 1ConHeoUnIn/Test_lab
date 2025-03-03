#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cout << "nhap kich thuoc ma tran: ";
    cin >> n;

    int map[n + 1][n + 1]; // Khai báo mảng tĩnh
    cout << "nhap cac phan tu ma tran:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> map[i][j];
        }
    }

    cout << "ma tran da nhap:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << map[i][j] << " ";
        }
        cout << "\n";
    }

    // Điểm bắt đầu
    int x = 1, y = 1;
    // Điểm kết thúc
    int endX = 3, endY = 3;

    while (endX != x || endY != y) {
        int left = 1, right = n;
        int mid;
        bool found = false;

        while (left <= right) {
            mid = (left + right) / 2;
            int height = map[mid][mid];

            cout << "\nToa do x: " << x << ", y: " << y << "\tdo cao: " << height;

            if (height < map[x][y]) {
                left = mid + 1;
            } else if (height > map[x][y]) {
                right = mid - 1;
            } else {
                found = true;
                break;
            }
        }

        if (!found) {
            int chenhlech1 = abs(map[mid + 1][mid] - map[mid][mid]);
            int chenhlech2 = abs(map[mid][mid + 1] - map[mid][mid]);

            cout << "chenh lech do cao o truc x: " << chenhlech1 << endl;
            cout << "chenh lech do cao o truc y: " << chenhlech2 << endl;

            // Cập nhật điểm (x, y)
            if (chenhlech1 < chenhlech2) {
                x = mid + 1; // Di chuyển xuống
            } else {
                y = mid + 1; // Di chuyển sang phải
            }
        } else {
            break; // Nếu đã tìm thấy thì thoát
        }
    }

    return 0;
}