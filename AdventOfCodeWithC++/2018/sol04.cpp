#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <map>
#include <regex>
#include <numeric>


using namespace std;

template <typename T, typename A>
int arg_max(std::vector<T, A> const& vec) {
  return static_cast<int>(std::distance(vec.begin(), max_element(vec.begin(), vec.end())));
}



int main() {
    string filename;
    filename = "inputs/04.txt";


    ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return 1;
    }


    vector<string> lines;
    string line;
    while (getline(inputFile, line)) {
        lines.push_back(line);
    }
    sort(lines.begin(), lines.end());

    map<int, vector<int>> guards;
    
    int start, end, id;
    for (string s : lines) {


        regex regex(".+ [0-9][0-9]:([0-9]+)] ([a-zA-Z]+) ([a-zA-Z#0-9]+).*");
        smatch m;
        regex_search(s, m, regex);

        if (m.str(2) == "falls") {
            start = stoi(m.str(1));
        }
        else if (m.str(2) == "wakes")
        {
            end = stoi(m.str(1));
            if (not guards.count(id)) {
                vector<int> v(60);
                guards[id] = v;
            }
            for (int t = start; t < end; t++) {
                guards[id][t] += 1;
            }
        }
        else {
            id = stoi( m.str(3).substr(1) );
        }
        
    }
    inputFile.close();

    // a)
    int most_sleepy, minutes_slept = 0, current;
    for (auto [key, val] : guards) {
        current = reduce(val.begin(), val.end());
        if (current > minutes_slept) {
            minutes_slept = current;
            most_sleepy = key;
        }
    }
    int most_common_minute = arg_max(guards[most_sleepy]);

    cout << "a: " << most_sleepy * most_common_minute << endl;

    // b)
    int highest_number = 0;
    for (auto [key, val] : guards) {
        current = *( max_element(val.begin(), val.end()) );
        if (current > highest_number) {
            highest_number = current;
            most_sleepy = key;
            most_common_minute = arg_max(val);
        }
    }

    cout << "b: " << most_sleepy * most_common_minute << endl;
    return 0;
}