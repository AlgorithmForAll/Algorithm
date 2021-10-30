#include <string>
#include <iostream>
#include <map>
#include <set>
#include <regex>

using namespace std;

int solution(string str1, string str2)
{
    int answer = 0;

    map<string, int> m1;
    map<string, int> m2;
    set<string> s;

    for (auto &c : str1)
        c = tolower(c);
    for (auto &c : str2)
        c = tolower(c);
    cout << str1 << endl;
    cout << str2 << endl;
    for (int i = 0; i < str1.size() - 1; i++)
    {
        if ((str1[i] >= 97 && str1[i] <= 122) && (str1[i + 1] >= 97 && str1[i + 1] <= 122))
        {
            string tmp = str1.substr(i, 2);
            s.insert(tmp);
            if (m1.find(tmp) == m1.end())
            {
                m1.insert({tmp, 1});
            }
            else
            {
                m1[tmp] += 1;
            }
        }
        else
        {
            continue;
        }
    }
    for (int i = 0; i < str2.size() - 1; i++)
    {
        if ((str2[i] >= 97 && str2[i] <= 122) && (str2[i + 1] >= 97 && str2[i + 1] <= 122))
        {
            string tmp = str2.substr(i, 2);
            s.insert(tmp);
            if (m2.find(tmp) == m2.end())
            {
                m2.insert({tmp, 1});
            }
            else
            {
                m2[tmp] += 1;
            }
        }
        else
        {
            continue;
        }
    }
    // 다중 교집합 구하기
    int in = 0;
    int out = 0;
    for (string c : s)
    {
        if (m1.find(c) != m1.end() && m2.find(c) != m2.end()) //교집합
        {
            in += min(m1[c], m2[c]);
        }
        if (m1.find(c) != m1.end() && m2.find(c) != m2.end()) //합집합(둘다 있음)
            out += max(m1[c], m2[c]);
        else if (m1.find(c) != m1.end() && m2.find(c) == m2.end()) // 하나만 있음
            out += m1[c];
        else
            out += m2[c];
    }

    if (in == 0 && out == 0)
    {
        return 65536;
    }

    answer = (double)in / (double)out * 65536;
    return answer;
}