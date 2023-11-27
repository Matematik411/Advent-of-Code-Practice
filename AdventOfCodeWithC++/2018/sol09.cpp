#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;


int main() {
    // int players = 9, last = 24;
    int players = 425, last = 7084800;

    // number: (prev, next)
    map<int, pair<int, int>> circle;
    // scores
    vector<long long> scores(players, 0);


    int n, nn, c, pl;
    circle[0] = {0, 0};
    c = 0;
    pl = 0;
    for (int m = 1; m <= last; m++) {


        if (m % 23 == 0) {
            scores[pl] += m;
            for (int i = 0; i < 7; i++) {
                c =circle[c].first;
            }
            scores[pl] += c;
            circle[circle[c].first].second = circle[c].second;
            circle[circle[c].second].first = circle[c].first;
            c = circle[c].second;
        }
        else {
            n = circle[c].second;
            nn = circle[n].second;
            circle[m] = {n, nn};
            circle[n].second = m;
            circle[nn].first = m;
            c = m;
        }

        pl = (pl + 1) % players;
        if (m == (last / 100)) {
            int solA = *(max_element(scores.begin(), scores.end()));
            cout << "a: " << solA << endl;
        }
    }


    long long solB = *(max_element(scores.begin(), scores.end()));

    cout << "b: " << solB << endl;





    return 0;
}