#include <bits/stdc++.h>

using namespace std;

// Complete the commonChild function below.
int m[5002][5002];
string s1, s2;

int solve(int x, int y, int k) {
    if (m[x][y] >= 0) {
        return m[x][y];
    }
    if (x == s1.size() || y == s2.size()) {
        m[x][y] = k;
        return k;
    }
    if (s1[x] == s2[y]) {
        k = max(k, solve(x+1, y+1, k+1));
    } else {
        k = max(
            max(k, solve(x+1, y+1, k)),
            max(solve(x+1, y, k), solve(x, y+1, k))
        );
    }

    m[x][y] = k;
    return k;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    memset(m, -1, sizeof(m));

    
    getline(cin, s1);

    
    getline(cin, s2);

    int result = solve(0,0,0);

    fout << result << "\n";

    fout.close();

    return 0;
}
