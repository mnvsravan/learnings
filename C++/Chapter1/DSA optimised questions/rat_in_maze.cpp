#include <bits/stdc++.h>
using namespace std;

// Explore all possible paths using backtracking
void helper(vector<vector<int>>& mat, int r, int c,
            string path, vector<string>& ans,
            vector<vector<bool>>& vis) {

    int n = mat.size();

    // Invalid cell
    if (r < 0 || c < 0 || r >= n || c >= n ||
        mat[r][c] == 0 || vis[r][c]) {
        return;
    }

    // Destination reached
    if (r == n - 1 && c == n - 1) {
        ans.push_back(path);
        return;
    }

    // Mark current cell
    vis[r][c] = true;

    // Down
    helper(mat, r + 1, c, path + "D", ans, vis);

    // Up
    helper(mat, r - 1, c, path + "U", ans, vis);

    // Left
    helper(mat, r, c - 1, path + "L", ans, vis);

    // Right
    helper(mat, r, c + 1, path + "R", ans, vis);

    // Backtrack
    vis[r][c] = false;
}

vector<string> findPath(vector<vector<int>>& mat) {

    int n = mat.size();
    vector<string> ans;

    if (n == 0 || mat[0][0] == 0)
        return ans;

    vector<vector<bool>> vis(n, vector<bool>(n, false));

    helper(mat, 0, 0, "", ans, vis);

    return ans;
}

int main() {

    vector<vector<int>> mat = {
        {1, 0, 0, 0},
        {1, 1, 0, 1},
        {1, 1, 0, 0},
        {0, 1, 1, 1}
    };

    vector<string> ans = findPath(mat);

    for (string path : ans) {
        cout << path << endl;
    }

    return 0;
}