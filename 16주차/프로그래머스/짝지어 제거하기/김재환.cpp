#include <iostream>
#include<string>
#include<stack>
using namespace std;
/*
연속으로 같은 것을 비교하기 때문에
스택구조를 활용하여 진행.
*/
int solution(string s){
    int answer = -1;

    stack<int> stack;

    for (int i = 0; i < s.size(); i++) {
        if (stack.size() >= 1) { // 1개부터는 비교 가능
            if (stack.top() == s[i]) { // 동일하다면 po하고 제거
                stack.pop();
                continue;
            }
        }
        stack.push(s[i]);
    }
    if (stack.empty()) {
        return 1;
    }
    else {
        return 0;
    }
}