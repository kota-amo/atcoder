N = int(input())
S=[""]*N
S = [input() for i in range(N)]  

f = max(set(S), key=S.count)
print(f)


