#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    int min_sum = INT_MAX;
    ifstream f("27989_B.txt");
    f >> n;
    vector <int> a(n);
    for (int i = 0; i < n; i++) {
        f >> a[i];
    }
    for (int i = 0; i < n; i++)
    {
        cout << i << endl;
        int sum = 0;
        for (int j = 0; j < n; j++)
        {
            int s = min(abs(i - j), n - abs(i - j));
            sum += s * a[j] * 3;
        }
        if (sum < min_sum) min_sum = sum;
    }
    cout <<min_sum << endl;
    return 0;
}
