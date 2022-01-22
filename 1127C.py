import heapq
N,W = map(int,input().split())
A = [0] * N   
B = [0] * N
for i in range(N):
   A[i], B[i] = map(int, input().split()) 
A=[-1 * i for i in A]
B.reverse()
heapq.heapify(A)
deli = 0
total =0
for i in range(N):
    flag = False
    m = heapq.heappop(A) * -1
    b =B[i]
    print(m,b)
    while b>0:
        deli += m
        total+=1
        b-=1
        if total>W:
            deli-=m
            flag = True
            break
    if flag == True:
        break
    else:  
        continue
print(deli)
