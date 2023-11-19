#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;


int main() {
    string filename;
    filename = "inputs/06.txt";


    ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return 1;
    }

    string line;
    vector< pair<int,int> > points;
    
    string fst, snd;
    while (getline(inputFile, line)) {
        fst = line.substr(0, line.find(","));
        snd = line.substr(line.find(",") + 1);
        points.push_back({ stoi(fst) , stoi(snd) });

    }
    inputFile.close();

    int xMin = 1000, xMax = 0, yMin = 1000, yMax = 0;
    for (auto p : points) {
        if (p.first < xMin)
            xMin = p.first;
        if (p.first > xMax)
            xMax = p.first;
        if (p.second < yMin)
            yMin = p.second;
        if (p.second > yMax)
            yMax = p.second;
    }

    // grid [xMin - 1, xMax + 1]x[yMin - 1, yMax + 1]
    vector< pair<int,int> > moved;
    for (auto p : points) {
        moved.push_back({p.first - (xMin - 1) , p.second - (yMin - 1)});
    }
    map<pair<int,int>, pair<int,int> > grid;
    for (int i = 0; i < (xMax - xMin + 3); i++) {
        for (int j = 0; j < (yMax - yMin + 3); j++) {
            grid[{i,j}] = {1000, -1};
        }
    }

    int c = 0, d;
    for (auto p : moved) {
        for (auto [key, value] : grid) {
            d = abs(p.first - key.first) + abs(p.second - key.second);
            if (d < value.first) {
                grid[key].first = d;
                grid[key].second = c;
            }
            else if (d == value.first)
            {
                grid[key].second = -1;
            }
        }
        c++;
    }

    // for (int i = 0; i < (xMax - xMin + 3); i++) {
    //     for (int j = 0; j < (yMax - yMin + 3); j++) {
    //         cout << grid[{i,j}].second << " ";
    //     }
    //     cout << endl;
    // }

    set<int> border;
    for (int i = 0; i < (xMax - xMin + 3); i++) {
        border.insert(grid[{i,0}].second);
        border.insert(grid[{i,(yMax-yMin+2)}].second);
    }
    for (int j = 0; j < (yMax - yMin + 3); j++) {
        border.insert(grid[{0,j}].second);
        border.insert(grid[{(xMax-xMin+2),j}].second);
    }
    
    int current, maxSize = 0;
    for (int id = 0; id < points.size(); id++) {
        if (border.count(id)) {
            continue;
        }
        current = 0;
        for (auto [key, value] : grid) {
            if (value.second == id) {
                current += 1;
            }
        }
        if (current > maxSize) {
            maxSize = current;
        }
    }
    cout << "a: " << maxSize << endl;


    // -----------------------------------
    int distMax = 10000;

    map<pair<int,int>, int> gridB;
    for (int i = 0; i < (xMax - xMin + 3); i++) {
        for (int j = 0; j < (yMax - yMin + 3); j++) {
            gridB[{i,j}] = 0;
        }
    }

    c = 0;
    for (auto p : moved) {
        for (auto [key, value] : grid) {
            d = abs(p.first - key.first) + abs(p.second - key.second);
            gridB[key] += d;
        }
        c++;
    }

    // for (int i = 0; i < (xMax - xMin + 3); i++) {
    //     for (int j = 0; j < (yMax - yMin + 3); j++) {
    //         cout << gridB[{i,j}] << " ";
    //     }
    //     cout << endl;
    // }
    int solB = 0;
    for (auto [key, value] : gridB) {
        if (value < distMax) {
            solB += 1;
        }
    }


    

    cout << "b: " << solB << endl;


    return 0;
}