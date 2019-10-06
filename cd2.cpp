#include <stdio.h>
#include <iostream>
#include <unordered_set>

using namespace std;


int main()
{
    int n, m; 
    while (true) {
        cin >> n >> m;  
        if (n == 0 && m == 0) {
            break; 
        }

        unordered_set<int> jack_set; 
        int count = 0; 
        int val;
        
        for (int i = 0; i < n; i++) {
            cin >> val; 
            jack_set.insert(val);
        }

        for (int i = 0; i < m; i++) {
            cin >> val; 
            if (jack_set.count(val)) {
                count++; 
            }
        }
        cout << count << endl;
    }
    return 0; 
}

