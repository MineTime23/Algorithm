def solution(id_pw, db):
    answer = 'fail'
    for a,b in db:
        if id_pw[0] == a:
            if id_pw[1] == b:
                answer = "login"
            elif answer !=  "login":
                answer = "wrong pw"
    return answer