#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using Graph = vector<vector<int>>;

// Input: Graph G,Initial node s
// Output: Array of shortest path like s to each node

vector<int> BFS(const Graph &G,int s){
    int N = (int)G.size(); // sum of node
    vector<int> dist(N,-1); // initialize All nodes to non-visited
    queue<int> que;

    dist[0] = 0;
    que.push(0);

    while (!que.empty()){
        if(dist[x] != -1){
            dist[x] = dist[v]+1;
            que.push(x);
        }
    }
    return dist;
}

int main(){
    // sum of top node and edge
    int N,M;
    cin >> N >> M;

    Graph G(N);
    for(int i=0;i<M;i++){
        int a,b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    vector<int> dist = BDS (G,0);

    for(int v=0;v<N;v++) cout << v << ":" << dist[v] << endl;
}