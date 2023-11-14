#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>


using namespace std;

string check(string left, string right, int d) {
    string common = "";
    int error = 0;
    for (int i = 0; i < d; i++) {
        if (left[i] != right[i]) {
            error += 1;
            if (error == 2) {
                return "";
            }
        }
        else {
            common += left[i];
        }
    }
    if (error) 
        return common;
    else
        return "";
}
 

int main() {
    string filename;
    filename = "inputs/02.txt";

    ifstream inputFile(filename);
    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return 1;
    }

    int two = 0;
    int three = 0;
    map<char, int> times;

    vector<string> words;

    string line;
    int addTwo, addThree;
    while (getline(inputFile, line)) {
        words.push_back(line);

        times.clear();
        addTwo = 0;
        addThree = 0;
        for (char c : line) {
            times[c] += 1;
        }
        for (auto const& [key, val] : times) {
            if (val == 2) {
                addTwo = 1;
            }
            if (val == 3) {
                addThree = 1;
            }
           
        }
        two += addTwo;
        three += addThree;
    }

    cout << "a: " << two * three << endl;

    string solB = "";
    int nr = words.size();
    int l = words[0].size();
    for (int i = 0; i < nr; i++) {
        for (int j = i+1; j < nr; j++) {
            solB = check(words[i], words[j], l);
            if (solB != "") {
                cout << "b: " << solB << endl;
                break;
            }
        }
        if (solB != "") {
            break;
        }
    }

    inputFile.close();

    return 0;
}