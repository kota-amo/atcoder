N ,Q = map(int, input().split())
A = list(map(int,input().split()))
x = [int(input()) for i in range(Q)]  

A.sort()

left = 0

for target in x:
    a.append(target)
    a.sort()
    rank = a.index(target)
    print(len(a)-rank-1)