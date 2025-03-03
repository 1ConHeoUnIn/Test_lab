#include <iostream>
using namespace std;

void quickSort(int a[], int left, int right) { // Changed arr to a
    if (left < right) {
        int pivot = a[(left + right) / 2];  // Use mid as pivot, accessing a
        int i = left, j = right;

        while (i <= j) {
            while (a[i] < pivot) { // Accessing a
                i++;
            }
            while (a[j] > pivot) { // Accessing a
                j--;
            }
            if (i <= j) {
                swap(a[i], a[j]); // Swapping elements of a
                i++;
                j--;
            }
        }

        if (left < j) {
            quickSort(a, left, j); // Recursive call with a
        }
        if (i < right) {
            quickSort(a, i, right); // Recursive call with a
        }
    }
}

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    int a[n]; //  Changed arr to a here
    cout << "Nhap cac phan tu: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i]; // Reading into a
    }

    quickSort(a, 0, n - 1); // Calling quicksort with a

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " "; // Printing elements of a
    }
    cout << endl;

    return 0;
}
