#include <string>
#include <vector>
#include <string>
#include <algorithm> //reverse
#include <stack>
#include <iostream>
using namespace std;

bool is_even(string p)
{
    stack<char> s;

    for (char c : p)
    {
        if (s.empty())
        {
            if (c == '(')
                s.push(c);
            else
                return false;
        }
        else
        {
            if (c == '(')
                s.push(c);
            else
            {
                char top = s.top();
                if (top == '(')
                    s.pop();
                else
                    return false;
            }
        }
    }
    if (s.empty())
        return true;
    else
        return false;
}
pair<string, string> set_uv(string p)
{
    int L = 0;
    int R = 0;

    for (auto c : p)
    {
        c == '(' ? L++ : R++;
        if (L == R)
            break;
    }
    string u = p.substr(0, L + R);
    string v = p.substr(L + R, p.size() - (L + R));
    return {u, v};
}

string change(string p)
{
    if (p.size() == 0)
        return p;
    if (is_even(p))
        return p;
    pair<string, string> uv = set_uv(p);
    if (is_even(uv.first))
    { // 균형잡힌 경우
        return uv.first + change(uv.second);
    }
    else
    {
        string tmp = '(' + change(uv.second) + ')';
        string tmp2 = uv.first.substr(1, uv.first.size() - 2);
        for (char &c : tmp2)
        {
            c = c == '(' ? ')' : '(';
        }
        return tmp + tmp2;
    }
}

string solution(string p)
{
    return change(p);
    ;
}