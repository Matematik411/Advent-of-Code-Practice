#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <regex>
#include <sstream>


using namespace std;

pair<int, int*> sumMeta(int* tree) {
  cout << "start" << endl;
  int metaSum = 0;
  int children = *tree;
  cout << "start1" << endl;
  int metaData = tree[1];
  cout << children << "!!" << metaData << endl;

  pair<int, int*> inner;
  inner.first = 0;
  inner.second = tree+2;

  // cout << "QQQQQQQQQQQQQQQQQQQQQQ" << inner.first << "!!" << inner.second[0]  << endl;



  for (int child = 0; child < children; child++) {
    cout << children << "!!" << inner.second[0] << endl;
    pair<int, int*> inner = sumMeta(inner.second);
    cout << "AAAAAAA" <<children << "!!" << metaData << endl;
    metaSum += inner.first;

  }
  for (int m = 0; m < metaData; m++) {
    metaSum += inner.second[m];
  }
  inner.first += metaSum;
  inner.second += metaData;
  return inner;
}

int main() {
  string filename;
  filename = "test.txt";


  ifstream inputFile(filename);

  if (!inputFile.is_open()) {
      cerr << "Error opening file." << endl;
      return 1;
  }

  string line;
  getline(inputFile, line);

  stringstream iss( line );
  int N = 0;
  int number;
  while ( iss >> number ) {
    N++;
  }

  int* data = (int*) malloc(N * sizeof(int));
  stringstream iss2 ( line );
  int i = 0;
  while ( iss2 >> number ) {
    data[i] = number;
    i += 1;
  }

  for (int i = 0; i < N; i++){
    cout << data[i] << " ";
  }
  cout << endl;

  pair<int, int*> resA = sumMeta(data);

  cout << "a: " << resA.first << endl;

  inputFile.close();

  return 0;
}
