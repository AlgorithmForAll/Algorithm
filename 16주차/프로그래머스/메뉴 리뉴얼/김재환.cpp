#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

map<string, int> M;
vector<int> big(11, 0);

void combination(vector<char> arr, vector<char> comb, int r, int index, int depth)
{
    if (r == 0)
    { // 더이상 뽑을게 없다. 출력한다.
        string tmp;
        for (int i = 0; i < comb.size(); i++)
        {
            tmp += comb[i];
        }
        if (M.find(tmp) == M.end())
        {

            M.insert({tmp, 1});
        }
        else
        {
            M[tmp] += 1;
            if (M[tmp] > big[comb.size()])
            {
                big[comb.size()] = M[tmp];
            }
        }
    }
    else if (depth == arr.size()) // 개수를 채우지 못한경우 // 순회를 다 돌았지만 채우지 못한경우
        return;
    else
    {
        // arr[depth] 를 뽑은 경우
        comb[index] = arr[depth];
        // index는 선택할 자원의 인덱스, depth는 뽑은 자원의 개수
        combination(arr, comb, r - 1, index + 1, depth + 1);
        // 위에서 comb[index]에 arr[depth]에 대입했었지만 comb[index]에 다시 덮어쓰러 가듯,
        // comb[index] 대입하러 간다. (즉 arr[depth]를 뽑지 않은 것으로 간주)

        // r은 뽑을 수 있는 개수
        combination(arr, comb, r, index, depth + 1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course)
{
    vector<string> answer;

    for (int i = 0; i < orders.size(); i++)
    {
        vector<char> arr(orders[i].begin(), orders[i].end());
        sort(arr.begin(), arr.end());
        for (int m = 0; m < course.size(); m++)
        {
            if (orders[i].size() < course[m])
            {
                continue;
            }
            combination(arr, vector<char>(course[m]), course[m], 0, 0);
        }
    }

    for (auto m : M)
    {
        string key = m.first;
        int val = m.second;
        if (big[key.size()] == val && val >= 2)
        {
            answer.push_back(key);
        }
    }

    return answer;
}