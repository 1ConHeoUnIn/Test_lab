#include <iostream>
using namespace std;
// 1 3 5 9 11 13 14 15 20 23 tim index (vị trí) của só 5 //đáp án là 2
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

    int left=0, right=n-1;
    
    int x=5; //
while(left<=right)
{
    int mid=(left+right)/2;
if(a[mid]<x)
{
    left=mid+1;
    cout<<"\n mid la: "<<mid<<"\t so: "<<a[mid];
}
if(a[mid]>x)
{
    right=mid-1;
    cout<<"\n mid la: "<<mid<<"\t so: "<<a[mid];
}
if(a[mid]==x)
{
    cout<<"\n mid la: "<<mid<<"\t so: "<<a[mid];
    break;
}
}
}
