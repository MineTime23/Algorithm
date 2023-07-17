a, b = list(map(int, input().split()))

arr = [i for i in range(a+1)]
for _ in range(b):
    a, b = list(map(int, input().split()))
    if a != b:
        arr[a],arr[b] = arr[b],arr[a]

for k in range(len(arr)):
    if k != 0:
        print(arr[k],end=" ")