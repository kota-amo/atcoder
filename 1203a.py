N = int(input())

if N<10:
    print("AGC00"+str(N))
elif N>=10 and N<42:
    print("AGC0"+str(N))
elif N>=42:
    print("AGC0"+str(N+1))

