N,W = map(int,input().split())
A = [0] * N   
B = [0] * N
for i in range(N):
   A[i], B[i] = map(int, input().split()) 

deli = 0
total =0
for i in range(N):
    flag = False
    m = max(A)
    mi = A.index(m)
    b =B[mi]
    print(m,b)
    while b>0:
        deli += m
        total+=1
        b-=1
        if total>W:
            deli-=m
            print("a")
            flag = True
            break
    if flag == True:
        break
    else:
        A[mi]=0      
        print("b")
        continue
print(deli)
print(total)