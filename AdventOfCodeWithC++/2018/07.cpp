#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <regex>


using namespace std;

vector<char> addCorrect(vector<char> v, char s) {

  int i = 0;
  for (int j = 0; j < v.size(); j++) {
    if (s > v[j]) {
      i = j + 1;
    }
  }
  v.insert(v.begin() + i, s);

  return v;
}


int main() {
  string filename;
  filename = "07.txt";


  ifstream inputFile(filename);

  if (!inputFile.is_open()) {
      cerr << "Error opening file." << endl;
      return 1;
  }



  map<char, vector<char>> graph;
  map<char, set<char>> req;
  set<char> vertices;

  string line;

  regex regex("Step (.) must be finished before step (.) can begin.");

  int c;
  while (getline(inputFile, line)) {
    smatch m;
    regex_search(line, m, regex);

    graph[m.str(1)[0]].push_back(m.str(2)[0]);
    req[m.str(2)[0]].insert(m.str(1)[0]);
    vertices.insert(m.str(1)[0]);

  }

  vector<char> clear = {'{'};
  for (auto v : vertices) {
    if (req[v].size() == 0) {
      clear = addCorrect(clear, v);
    }
  }


  char node;
  string solA = "";
  while (clear.size() > 1) {

    node = clear[0];
    clear.erase(clear.begin());

    solA += node;

    for (auto neigh : graph[node]) {
      req[neigh].erase(node);

      if (req[neigh].size() == 0) {
        clear = addCorrect(clear, neigh);
      }
    }

  }

  cout << "a: " << solA << endl;

  inputFile.close();

  return 0;
}
