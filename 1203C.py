N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

m = [["." for j in range(N)] for i in range(N)]

list=[]

for k in range(min(P-A,R-B),max(Q-A,S-B)):
    if 0<=A+k-1 and A+k-1<N and 0<=B+k-1 and B+k-1<N and k>=max(1-A,1-B) and k<=min(N-A,N-B):
        m[A+k-1][B+k-1]="#"
for k in range(min(P-A,R-B),max(Q-A,S-B)):
    if 0<=A+k-1 and A+k-1<N and B-k-1>=0 and B-k-1<N and k>=max(1-A,B-N) and k<=min(N-A,B-1):
        m[A+k-1][B-k-1]="#"

for i in range(P-1,Q):
    for j in range(R-1,S):
        print(m[i][j],end="")
    print("\n")




