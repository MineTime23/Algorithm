def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya","1").replace("ye","2").replace("woo","3").replace("ma","4")
        babbling[i] = babbling[i].replace("11","X").replace("22","X").replace("33","X").replace("44","X")
        if babbling[i].isdigit() and "X" not in babbling[i]:
            answer += 1
    return answer