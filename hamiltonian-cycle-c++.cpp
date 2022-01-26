// Hamiltonian cycle in c++

#include <iostream>
#include <vector>

using namespace std;

void tryNextStep(int curpos,vector<int>& path, bool* visited,const int** graph) {
    bool allVisited=true;
    int i;
    for(int i=0;i<5;i++) {
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
            path.pop_back();
        }
    }
}

int main() {
    const int graph[][]={
        {0,1,0,1,0},
        {1,0,1,1,1},
        {0,1,0,0,1},
        {1,1,0,0,1},
        {0,1,1,1,0}};
    const int nodes=5;
    bool visited[]={true,false,false,false,false};
    vector<int> path;
    

    tryNextStep(0,path,visited,graph);

}