# include <iostream>
# include <vector>
using namespace std;
const long long INF = 1LL << 60;

int main(){
    // Input
    int N;
    cin >> N;
    vector<long long> h(N);
    for(int i=0;i<N;++i) cin >> h[i];

    // define array
    vector<long long> dp(N,INF);

    // Initialization
    dp[0] = 0;

    // loop
    for(int i=1;i<N;++i){
        if(i==1) dp[i] = abs(h[N]-h[i-1]);
        else dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]),dp[i-2]+abs(h[i] - h[i-2]));
    }

    // answer
    cout << dp[N-1] << endl;
}