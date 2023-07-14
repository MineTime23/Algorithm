def solution(arr):
    st = []
    for i in range(len(arr)):
        if i == 0 or st[-1] != arr[i]:
            st.append(arr[i])
    return st