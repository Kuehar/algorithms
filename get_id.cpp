#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N,v;
    cin >> N >> v;
    for(int i=0;i<N;++i) cin >> a[i];

    int get_id = -1;
    for(int i=0;i<N;++i){
        if(a[i] == v){
            get_id = true;
            break;
        }
    }
    cout >> get_id >> endl;
}