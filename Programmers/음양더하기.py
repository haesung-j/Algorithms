def solution(absolutes, signs):

    return sum([x if s else -x for x,s in zip(absolutes,signs)])
