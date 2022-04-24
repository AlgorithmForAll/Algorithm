"""
sort 람다식 안보고 써서 뿌듯함
dict쓸때 dictA['none']하면 error발생하는데
dictA.get('none')하면 에러안남 
"""


def solution(genres, plays):
    answer = []
    # 많이 재생된장르, 장르내에서 많이 재생된 노래, 장르내 재생횟수 같으면 고유번호 낮은거 먼저 수록
    # 장르당 2개씩
    init = {}
    score = {}
    for gi in range(len(genres)):
        if genres[gi] in init:
            score[genres[gi]] += plays[gi]
            init[genres[gi]].append((plays[gi], gi))
        else:
            score[genres[gi]] = plays[gi]
            init[genres[gi]] = [(plays[gi], gi)]
    print(init, score)
    _score = list(score.items())
    # 장르별 우선순위 정하기
    _score.sort(key=lambda x: -x[1])
    print(_score)
    for _s in _score:
        genre, score = _s
        init[genre].sort(key=lambda x: -x[0])
        if len(init[genre]) == 1:
            pls, pli = init[genre][0]
            answer.append(pli)
        else:
            pls, pli = init[genre][0]
            answer.append(pli)
            pls, pli = init[genre][1]
            answer.append(pli)
    # 장르당 노래별 우선순위 정하기 (리스트 삽입)
    print(answer)
    return answer
