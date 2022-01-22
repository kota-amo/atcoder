S,T,X = map(int,input().split())
if X>=S and X<T:
    print("Yes")
elif X>=S and T<S:
    print("Yes")
elif T<S and X < T:
    print("Yes")
else:
    print("No")
