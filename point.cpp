#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// 2点 (x1,y1)と(x2,y2)tono


double calc_dist(double x1,double y1,double x2,double y2){
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 -y2));
}

int main(){
    // 入力データを受け取る
    int N;
    cin >> N;
    vector<double> x(N),y(N);
    for(int i=0;i<N;++i) cin >> x[i] >> y[i];
    double minimum_dist = 1000000000.0;
    for(int i=0;i<N;++i){
        for(int j=i+1;j<N;++j){
            double dist_i_j = calc_dist(x[i],y[i],x[j],y[j]);
            if(dist_i_j < minimum_dist){
                minimum_dist = dist_i_j;
            }
        }
    }
    cout << minimum_dist << endl;
}