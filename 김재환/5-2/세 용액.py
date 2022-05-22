"""
투포인터 + 이분탐색
arr[i] + arr[j] + arr[k]
i를 고정시키고 j,k를 투포인터처럼 활용하는 기법

https://www.acmicpc.net/board/view/84255
"함수의 local 변수들은 런타임에 추가 될 수 없기 때문에 고정크기 array에 저장 될 수 있고, 
빠르게 접근 할 수 있으나 글로벌 변수들은 런타임에 추가될 수 있기에 dict에 저장하기 때문에 
저장/읽기에서 local 변수보다 느리다."
=> 내부적으로 빠르게 읽기 위해서는 로컬 변수가 짱이다??
"""

diff = 1000000000 * 3
answer = []


def solution():
    global diff
    for i in range(len(arr)-2):

        j = i+1
        k = len(arr)-1

        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total == 0:
                print(arr[i], arr[j], arr[k])
                exit()

            if abs(total) < abs(diff):
                answer = [arr[i], arr[j], arr[k]]
                diff = total

            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    solution()
