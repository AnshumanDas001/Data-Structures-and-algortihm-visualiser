#include <bits/stdc++.h>
using namespace std;

/**
 * Given a permutation packageSequence of 1..n, returns the number of full
 * scans (operations) the manager needs to collect all packages in order.
 */
int getNumberOperations(const vector<int>& packageSequence) {
    int n = packageSequence.size();
    vector<int> position(n+1);
    for(int i = 0; i < n; i++) {
        position[ packageSequence[i] ] = i;
    }
    int operations = 1;
    int currindex = -1;
    for(int v = 1; v <= n; v++){
        if(position[v] > currindex) {
            currindex = position[v];
        } else {
            operations++;
            currindex = position[v];
        }
    }
    return operations;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    cout << getNumberOperations(a) << "\n";
    return 0;
}