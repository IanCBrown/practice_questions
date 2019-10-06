#include <stdio.h>
#include <iostream>
#include <unordered_set>

using namespace std;


int main()
{
    while (true) {
        int n, m; 
        cin >> n >> m;  
        if (n == 0 && m == 0) {
            break; 
        }

        unordered_set<int> info_set; 
        int val;
        int diff; 
        
        for (int i = 0; i < n + m; i++)
        {
            cin >> val;
            info_set.insert(val);
        }

        diff = (n + m) - info_set.size();
        cout << diff; 
    }
    return 0; 
}

