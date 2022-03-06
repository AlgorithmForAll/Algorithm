"""
매칭 점수
https://programmers.co.kr/learn/courses/30/lessons/42893
"""
import re


def solution(word, pages):
    word = word.lower()
    base_scores = dict()
    urls = dict()
    ex_urls = dict()

    for idx, page in enumerate(pages):
        page = page.lower()

        url = re.search('(<meta property.+content=")(https://.*)"/>', page).group(2)
        urls[url] = idx

        base_score = 0
        for w in re.findall("[a-z]+", page):
            if w == word:
                base_score += 1
        base_scores[url] = base_score

        ex_url = re.findall('(<a href=")(https://\S*)">', page)
        ex_urls[url] = [eu[1] for eu in ex_url]

    match_scores = []
    for idx, url in enumerate(urls.keys()):
        link_score = 0
        for k, val in ex_urls.items():
            if url in val:
                link_score += (base_scores[k] / len(val))

        total = base_scores[url] + link_score
        match_scores.append([total, idx])
    match_scores.sort(key=lambda x: (x[0], -x[1]))
    return match_scores[-1][1]


print(solution("blind", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
