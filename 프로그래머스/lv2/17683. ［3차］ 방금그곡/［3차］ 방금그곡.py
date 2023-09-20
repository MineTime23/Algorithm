import re
def solution(m, musicinfos):
    answer = []
    m = m.replace("C#","c")
    m = m.replace("D#","d")
    m = m.replace("F#","f")
    m = m.replace("G#","g")
    m = m.replace("A#","a")

    pattern = r"([ABCDEFG])"
    for idx,i in enumerate(musicinfos):
        str1 = i.split(",")
        #print(str1)
        
        str1[-1] = str1[-1].replace("C#","c")
        str1[-1] = str1[-1].replace("D#","d")
        str1[-1] = str1[-1].replace("F#","f")
        str1[-1] = str1[-1].replace("G#","g")
        str1[-1] = str1[-1].replace("A#","a")
        arrange = re.split(pattern,str1[-1])
        arrange = [i for i in arrange if i != ""]
        #print(arrange)
        
        start_time = str1[0].split(":")
        start_time = 60 * int(start_time[0]) + int(start_time[1])
        end_time = str1[1].split(":")
        end_time = 60 * int(end_time[0]) + int(end_time[1])
        time = end_time - start_time
        if time < len(arrange):
            arrange = arrange[:time]
        elif time > len(arrange):
            arrange = arrange * (time // len(arrange)) + arrange[:(time % len(arrange))]
        #print(arrange) 
        arrange = ''.join(arrange)
        
        if m in arrange:
            answer.append((str1[2],time,idx))
            
    #print(answer)
    answer = sorted(answer, key = lambda x : (-x[1],x[2]))
    if answer:
        return answer[0][0]
    return f"(None)"