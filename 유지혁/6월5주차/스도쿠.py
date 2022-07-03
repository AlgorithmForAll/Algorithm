#2239 스도쿠
#DFS
import sys
input = sys.stdin.readline

def dfs(idx):
    #모든 빈칸에 다 숫자를 넣었으면 출력
    if idx == len(zeros):
        for i in range(9):
            print(''.join(sudoku[i]))
        exit()
    
    #idx번째 빈칸 채우기 시작
    cx, cy = zeros[idx]
    for num in range(1,10):
        num = str(num)
        flag = True #해당 위치에 num이 들어와도 되는지 확인하는 flag
        
        #행 체크
        for y in range(9):
            if sudoku[cx][y] == num:
                flag = False
                break

        #열 체크
        for x in range(9):
            if sudoku[x][cy] == num:
                flag = False
               
            if flag == False:
                break

        #3*3 체크
        sx = (cx // 3) * 3
        sy = (cy // 3) * 3
        for x in range(3):
            for y in range(3):
                if sudoku[sx + x][sy + y] == num:
                    flag = False

                if flag == False:
                    break

        #flag == True인 경우 해당 위치에 num 넣기
        if flag == True:
            sudoku[cx][cy] = str(num)
            dfs(idx + 1)
            sudoku[cx][cy] = 0  

if __name__ == "__main__":
    sudoku = [] #수도쿠
    zeros = [] #0좌표
    for i in range(9):
        sudoku.append(list(input().rstrip()))
        for j in range(9):
            if sudoku[i][j] == '0':
                zeros.append((i, j))

    dfs(0)
