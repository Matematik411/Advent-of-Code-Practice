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

int timeNeeded(char s) {

  return int(s) - int('A') + 1 + 60;
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


  vector< pair<int, char> > workers = {{-1, '*'},{-1, '*'},{-1, '*'},{-1, '*'},{-1, '*'}};
  set<char> visited;
  char node;
  string solB = "";
  int timeSpent = 0;
  while (solB.size() < (vertices.size()+1)) {

    for (int w = 0; w < 5; w++) {
      if (workers[w].second == '*') {
        if (clear.size() > 1) {
          workers[w] = {timeNeeded(clear[0]), clear[0]};
          clear.erase(clear.begin());
        }
      }
    }


    timeSpent += 1;

    for (int w = 0; w < 5; w++) {
      if (workers[w].second != '*') {
        workers[w].first -= 1;
        if (workers[w].first == 0) {
          node = workers[w].second;
          for (auto neigh : graph[node]) {
            req[neigh].erase(node);

            if (req[neigh].size() == 0) {
              clear = addCorrect(clear, neigh);
            }
          }
          solB += node;
          workers[w] = {-1, '*'};
        }
      }
    }
  }

  cout << "b: word is " << solB << ", time needed " << timeSpent << endl;

  inputFile.close();

  return 0;
}
