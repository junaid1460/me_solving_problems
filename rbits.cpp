#include<bits/stdc++.h>
using namespace std;
int main(){
    priority_queue<tuple<int, int>> pq;
    pq.push(make_tuple(2,3));
    pq.push(make_tuple(1,3));
    for(auto it = begin(pq); it != end(pq); ++it){
        std :: cout << *it;

    }
    return 0;
    
}