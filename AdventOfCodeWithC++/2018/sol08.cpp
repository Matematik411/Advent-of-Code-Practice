#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <regex>
#include <sstream>


using namespace std;

pair<int, int> sumMeta(vector<int> tree, int loc) {

  int metaSum = 0;
  int children = tree[loc];
  int metaData = tree[loc+1];
  loc +=2;

  for (int child = 0; child < children; child++) {
    pair<int, int> inner = sumMeta(tree, loc);
    metaSum += inner.first;
    loc = inner.second;
  }
  for (int m = 0; m < metaData; m++) {
    metaSum += tree[loc];
    loc += 1;
  }

  return {metaSum, loc};
}

pair<int, int> sumMetaPointers(vector<int> tree, int loc) {

  int metaSum = 0;
  int children = tree[loc];
  int metaData = tree[loc+1];
  loc +=2;

  vector<int> childrenValues;
  for (int child = 0; child < children; child++) {
    pair<int, int> inner = sumMetaPointers(tree, loc);
    childrenValues.push_back(inner.first);
    loc = inner.second;
  }

  for (int m = 0; m < metaData; m++) {
    if (children == 0) {
      metaSum += tree[loc];
    }
    else {
      if (tree[loc] <= children) {
        metaSum += childrenValues[tree[loc] - 1];
      }
    }
    loc += 1;
  }

  return {metaSum, loc};
}

int main() {
  string filename;
  filename = "inputs/08.txt";


  ifstream inputFile(filename);

  if (!inputFile.is_open()) {
      cerr << "Error opening file." << endl;
      return 1;
  }

  string line;
  getline(inputFile, line);

  stringstream iss( line );
  int number;
  vector<int> treeFull;
  while ( iss >> number ) {
    treeFull.push_back(number);
  }


  pair<int, int> resA = sumMeta(treeFull, 0);
  cout << "a: " << resA.first << endl;


  pair<int, int> resB = sumMetaPointers(treeFull, 0);
  cout << "b: " << resB.first << endl;

  inputFile.close();

  return 0;
}
