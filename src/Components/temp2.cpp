#include <bits/stdc++.h>
using namespace std;
string getCodeAtTime(string initialCode, long long minutesElapsed) {
    int n = initialCode.length();
    string result(n, '0');  // Final result starts with all '0's
    int zeros = 0;

    for (int i = 0; i < n; ++i) {
        if (initialCode[i] == '0') {
            zeros++;
        } else {
            // Push this '1' as far left as allowed
            long long move = min((long long)zeros, minutesElapsed);
            result[i - move] = '1';
            minutesElapsed -= move;
        }
    }
    return result;
}
int main() {
    string initialCode;
    long long minutesElapsed;
    
    cin >> initialCode;
    cin >> minutesElapsed;
    
    cout << getCodeAtTime(initialCode, minutesElapsed) << endl;
    return 0;
}