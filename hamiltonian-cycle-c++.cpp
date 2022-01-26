// Hamiltonian cycle in c++
// https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/?ref=lbp

#include <iostream>
#include <vector>

using namespace std;

void tryNextStep(int curpos,vector<int>& path, bool* visited,const int graph[5][5]) {
    bool allVisited=true;
    int i;
    for(i=0;i<5;i++) {
        if(!visited[i]) {
            allVisited=false;
        }
    }
    if(allVisited) {
        if(graph[curpos][0]==1) {
            path.push_back(0);
            int size=path.size();
            for(i=0;i<size;i++) {
                cout << path[i] << " ";
            }
            cout << endl;
            path.pop_back();
        }
    }
    for(i=0;i<5;i++) {
        if(!visited[i] && graph[curpos][i]==1) {
            visited[i]=true;
            path.push_back(i);
            tryNextStep(i,path,visited,graph);
            path.pop_back();
            visited[i]=false;
        }
    }
}

int main() {
    const int graph[5][5]={
        {0,1,0,1,0},
        {1,0,1,1,1},
        {0,1,0,0,1},
        {1,1,0,0,1},
        {0,1,1,1,0}};
    const int nodes=5;
    bool visited[]={true,false,false,false,false};
    vector<int> path;
    path.push_back(0);
    tryNextStep(0,path,visited,graph);
}