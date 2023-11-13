#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>


int main() {
    std::string filename;
    filename = "inputs/01.txt";


    std::ifstream inputFile(filename);


    if (!inputFile.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    std::string line;
    int solA = 0;
    int currentB = 0;
    std::vector< int > moves;
    std::set< int > seen;

    int c;
    while (std::getline(inputFile, line)) {
        c = std::stoi( line );
        moves.push_back(c);
        solA += c;
    }
    std::cout << "a: " << solA << std::endl;

    int i = 0;
    int size = moves.size();
    while (true) {
        currentB += moves[i]; 

        if (seen.count(currentB)) {
            std::cout << "b: " << currentB << std::endl;
            break;
        }
        seen.insert(currentB);
        i += 1;
        if (i == size) {
            i = 0;
        }


    }


    inputFile.close();

    return 0;
}