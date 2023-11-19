#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;


int main() {
    string filename;
    filename = "inputs/text.txt";


    ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return 1;
    }

    string line;
    std::vector< int > data;

    int c;
    while (getline(inputFile, line)) {
        c = stoi( line );
        data.push_back(c);

    }


    inputFile.close();

    return 0;
}