#include <iostream>
using namespace std;
int n;
int chenhlech = 0;
// diem bat dau
int x = 1, y = 1;
// diem ket thuc
int endX = 3, endY = 3;

int main()
{
    cout << "nhap ma tran: ";
    cin >> n;
    int map[n][n];
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> map[i][j];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cout << "ma tran da nhap la:  " << endl;
            cout << map[i][j] << " ";
        }
        cout << "\n";
    }

    while (x != endX && y != endY)
    {
        int left = 1, right = n;
        int chenhlech1, chenhlech2;
        int mid;
        while (left <= right)
        {
            mid = (left + right) / 2;
            int docao = map[mid][mid];
            if (docao < map[x][y])
            {
                left = mid + 1;
            }
            if (docao > map[x][y])
            {
                right = mid - 1;
            }
            if (docao == map[x][y])
            {
                cout << "\n toa do " << "x: " << x << ", y: " << y << "\t do cao: " << docao << endl;
                break;
            }
        }
        chenhlech1 = abs(map[x + 1][y] - map[x][y]);
        chenhlech2 = abs(map[x][y + 1] - map[x][y]);

        cout << "chenh lech do cao o truc x: " << chenhlech1 << endl;
        cout << "chenh lech do cao o truc y: " << chenhlech2 << endl;
        if (chenhlech1 < chenhlech2 || chenhlech1 == chenhlech2)
        {
            x++;
        }
        else
        {
            y++;
        }
        cout << "\n toa do " << "x: " << x << ", y: " << y << "\t do cao: " << map[x][y] << endl;
    }

    return 0;
}
