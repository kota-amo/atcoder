from bisect import insort
N , K = map(int, input().split())
P = list(map(int,input().split()))

sortPK = P[0:K]
sortPK.sort()
print(sortPK[0])

for i in range(K,N):
    insort(sortPK, P[i])
    print(sortPK[-K])
