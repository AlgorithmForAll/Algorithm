
#include <string>
#include <vector>
#include <iostream>

using namespace std;
int Map[100][100];

vector<int> solution(int rows, int columns, vector<vector<int>> queries)
{
    vector<int> answer;

    int num = 1;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            Map[i][j] = num++;
    for (int i = 0; i < queries.size(); i++)
    {
        int y1, x1, y2, x2;
        y1 = queries[i][0];
        x1 = queries[i][1];
        y2 = queries[i][2];
        x2 = queries[i][3];
        int move_x = x2 - x1;
        int move_y = y2 - y1;

        int y = y1 - 1;
        int x = x1;
        int tmp;
        int past = Map[y1 - 1][x1 - 1];
        int small = 100 * 100;
        // 동쪽
        for (int i = 0; i < move_x; i++)
        {
            tmp = Map[y][x];
            Map[y][x++] = past;
            small = min(past, small);
            past = tmp;
        }
        // 남쪽
        y++;
        x--;
        for (int i = 0; i < move_y; i++)
        {
            tmp = Map[y][x];
            Map[y++][x] = past;
            small = min(past, small);
            past = tmp;
        }
        y--;
        x--;
        // 서쪽
        for (int i = 0; i < move_x; i++)
        {
            tmp = Map[y][x];
            Map[y][x--] = past;
            small = min(past, small);
            past = tmp;
        }
        // 북쪽
        y--;
        x++;
        for (int i = 0; i < move_y; i++)
        {
            tmp = Map[y][x];
            Map[y--][x] = past;
            small = min(past, small);
            past = tmp;
        }
        answer.push_back(small);
    }

    return answer;
}

int main()
{
    solution(6, 6, {{2, 2, 5, 4}, {3, 3, 6, 6}, {5, 1, 6, 3}});
}