#include <iostream>
using namespace std;

int func(int N){
    // 再帰関数の呼び出しを宣言
    cout << "func(" << N << ")を呼び出しました" << endl;
    if(N == 0) return 0;

    // 再帰処理
    int result = N + func(N-1);
    cout << N << " までの和 = " << result << endl;

    return result;
}

int main(){
    func(5);
}