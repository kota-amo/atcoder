N,X = map(int,input().split())
A = list(map(int,input().split()))

while X>0:
    if A[X-1]==0:
        break
    else:
        temp = X
        X = A[X-1]
        A[temp-1]=0

count =0
for item in A:
    if item == 0:
        count += 1
print(count)



