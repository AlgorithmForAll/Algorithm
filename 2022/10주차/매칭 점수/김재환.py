"""

"""
import re


def findWord(word, html):
    count = 0
    for w in re.findall('[a-z]+', html):  # 페이지 전체에서 단어검색
        if w == word:
            count += 1
    return count


def getInfo(word, pages):
    # 페이지를 순서대로 돌면서 기본점수 구하기
    order = []
    for page in pages:
        pageTitle = re.findall(
            f'<meta property="og:url" content="https://(\S+)"', page)[0]
        bodyhtml = re.findall('<body>(.+)</body>', page.lower(), re.DOTALL)[0]
        linklist = re.findall(f'<a href="https://(\S+)"', bodyhtml)

        score = findWord(word.lower(), bodyhtml)
        order.append(pageTitle)
        for i in linklist:
            if i in outerLink:
                outerLink[i].append(pageTitle)
            else:
                outerLink[i] = [pageTitle]
        link = len(linklist)
        standard[pageTitle] = [score, link]
    return order


outerLink = {}
standard = {}
totalScore = []


def getScore(order):
    print(order)
    for pageTitle in order:
        score, link = standard[pageTitle]
        result = 0
        if pageTitle in outerLink:
            sublinks = outerLink[pageTitle]

            for sublink in sublinks:
                sS, sL = standard[sublink]
                if sL == 0:
                    result += sS
                else:
                    result += sS/sL
        result += score
        totalScore.append(result)


def solution(word, pages):
    answer = 0
    order = getInfo(word, pages)
    getScore(order)
    print(standard)
    print(outerLink)
    print(totalScore)
    print(totalScore.index(max(totalScore)))
    return totalScore.index(max(totalScore))
