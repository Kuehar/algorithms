#include <iostream>
#include <vector>
using namespace std;
const int INF = 2000000; //大きな値を代入

int main(){
    // input value
    int N,K;
    cin >> N >> K;
    vector<int> a(N),b(N);
    for(int i=0;i<N;++i) cin >> a[i];
    for(int i=0;i<N;++i) cin >> b[i];

    // linear search
    int min_value = INF;
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            // 和がK未満の場合は捨てる
            if (a[i]+b[j] < K) continue;

            // 最小値を更新
            if(a[i]+b[j] < min_value){
                min_value = a[i] + b[j];
            }
        }
    }
    cout << min_value << endl;
}