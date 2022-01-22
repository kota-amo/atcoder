import bisect
N ,Q = map(int, input().split())
A = list(map(int,input().split()))
x = [int(input()) for i in range(Q)]  

A.sort()
left=0
right=N-1

for target in x:
    index = bisect.bisect_left(A, target)
    print(N- index)