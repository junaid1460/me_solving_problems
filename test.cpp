#include<iostream>
#include<algorithm>
#include<vector>

int main(){
    int n;
    std::cin >> n;
    std::vector<int> buildings;
    buildings.reserve(n);
    for(int i = 0;i< n;i++){
        std::cin >> buildings[i];
    }
    

}