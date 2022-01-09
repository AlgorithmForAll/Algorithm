"""
단어 변환
https://programmers.co.kr/learn/courses/30/lessons/43163
"""


def solution(begin, target, words):
    def check(a, b):
        n = len(a)
        count = n
        for i in range(n):
            if a[i] == b[i]:
                count -= 1
        return count == 1

    def dfs(word, level, visited):
        if word == target:
            return level

        result = float('inf')
        for i in range(len(words)):
            if check(word, words[i]) and visited & (1 << (i + 1)) == 0:
                result = min(result, dfs(words[i], level + 1, visited | (1 << (i + 1))))
        return result

    answer = dfs(begin, 0, 0)
    return answer if answer != float('inf') else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "hog", "lot", "cog"]), 3)
print(solution("hit", "cog", ["hot", "dot", "hol", "lot", "cog"]), 0)
print(solution("hit", "cog", ["hot", "lit", "lig", "tig", "dot", "dog", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "tog", "vog", "lot", "cog"]), 4)
print(solution("aaaaaaaaaa", "bbbbbbbbbb",
               ["aaaaaaaaab", "aaaaaaaabb", "aaaaaaabbb", "aaaaaabbbb", "aaaaabbbbb", "aaaabbbbbb", "aaabbbbbbb",
                "aabbbbbbbb", "abbbbbbbbb",
                "aaaabaaaaa", "aaaabaaaba", "aaabbaaaab", "babaaabaab", "abbaaaabbb", "bbaabbbbaa", "babaabbbbb",
                "abbbbbbabb", "babbbbbbbb", "bbabbbbbbb", "bbbabbbbbb"]), 0)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
    "1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
