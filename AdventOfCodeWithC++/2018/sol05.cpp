#include <iostream>
#include <fstream>
#include <string>


using namespace std;

string reduce(string s) {

    char l, r;
    int changed = 0, i = 0;
    while (i < (s.size() - 1)) {
    // for (int i = 0; i < (s.size() - 1); i++) {
        l = s[i];
        r = s[i+1];
        if ((l != r) and (toupper(l) == toupper(r))) {
            // cout << s << "---" << s.substr(0, i) + s.substr(i+2) << endl;
            s = s.substr(0, i) + s.substr(i+2);
            changed = 1;
            i -= 1;
        }
        i += 1;
    }
    if (changed) {
        s = reduce(s);
    }
    return s;
}

string remove(string s, char c) {
    int i = 0;
    while (i < s.size()) {
        if (tolower(s[i]) == c) {
            s = s.substr(0, i) + s.substr(i+1);
            i -= 1;
        }
        i += 1;
    }
    return s;


}


int main() {
    string filename;
    filename = "inputs/05.txt";


    ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return 1;
    }

    string line;
    getline(inputFile, line);
    inputFile.close();

    int solA = reduce(line).size();
    cout << "a: " << solA << endl;

    string corrected;
    int solB = solA;
    int for_this; 
    for (int i = int('a'); i <= int('z'); i++) {
        corrected = remove(line, char(i));
        for_this = reduce(corrected).size(); 
        if (for_this < solB) {
            solB = for_this;
            cout << "improvement for " << char(i) << " .. now best is " << solB << endl;
        }

    }
    cout << "b: " << solB << endl;
    return 0;
}