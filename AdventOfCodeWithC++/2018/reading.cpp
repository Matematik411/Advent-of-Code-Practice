#include <iostream>
#include <fstream>
#include <string>


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
    while (getline(inputFile, line)) {
        cout << line << endl;
    }

    inputFile.close();

    return 0;
}