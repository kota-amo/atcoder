import heapq

N,K = map(int,input().split())
P = list(map(int,input().split()))

que = P[0:K]
print(min(que))

#リストを優先度付きキューに変換
heapq.heapify(que) 

for i in range(K,N):
    #優先度付きキューから最小値を取り出して出力
    minima = heapq.heappop(que)
    #P[i]と比較して小さい方が最小値
    minima = max(minima,P[i])
    
    #優先度付きキューに要素を挿入
    heapq.heappush(que,minima)
    print(que)
      
    #優先度付きキューから最小値を取り出して出力
    ans = heapq.heappop(que)
    print(ans)
    
    #優先度付きキューに要素を挿入
    heapq.heappush(que,ans)

