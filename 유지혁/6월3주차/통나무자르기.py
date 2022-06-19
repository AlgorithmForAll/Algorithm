#1114 통나무 자르기
# https://jintak0401.github.io/posts/boj-1114/ 참고

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    L, K, C = map(int, input().split())
    arr = [0, *sorted([*map(int, input().split())]), L]
    pieces = [arr[i] - arr[i-1] for i in range(len(arr) - 1, 0, -1)]
    longest_piece = max(pieces)

    def cut(length):
        if longest_piece > length:
            return 10001, 0

        cur_len = 0
        count = 0
        for piece_len in pieces:
            cur_len += piece_len
            if cur_len > length:
                cur_len = piece_len
                count += 1

        return count, cur_len if count == C else pieces[-1]

    left, right = 0, L
    ans_pt, ans_len = 0, 0
    while left <= right:
        mid = (left + right) // 2
        cnt, pt = cut(mid)
        if cnt <= C:
            ans_pt = pt
            ans_len = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans_len, ans_pt)
