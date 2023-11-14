#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <regex>
#include <set>


using namespace std;

int main() {
    string filename;
    filename = "inputs/03.txt";

    ifstream inputFile(filename);
    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return 1;
    }

    map<pair<int, int>, pair<int, int>> grid;
    map<int, int> sizes;
    string line;
    int i, j, repeat, k = 1;
    int solB = -1;
    while (getline(inputFile, line)) {

        std::regex regex(".+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)");
        std::smatch m;
        std::regex_match(line, m, regex);

        repeat = 0;
        
        for (i = 0; i < (stoi (m[3])); i++) {
            for (j = 0; j < (stoi (m[4])); j++) {

                grid[{(stoi (m[1])) + i, (stoi (m[2])) + j}].first = k; 
                grid[{(stoi (m[1])) + i, (stoi (m[2])) + j}].second += 1; 
                sizes[k] += 1;

            }
        }
        k += 1;
    }

    inputFile.close();


    int solA = 0;
    for (auto const& [key, val] : grid) {
        if (val.second > 1) {
            solA += 1;
        }
        else {
            sizes[val.first] -= 1;
        }
    }
    cout << "a: " << solA << endl;
    for (int a = 1; a < k; a++) {
        if (sizes[a] == 0) 
            cout << "b: " << a << endl;
    }

    return 0;
}