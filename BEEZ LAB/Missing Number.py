l=list(map(int,input().split()))
l.sort()
for i in range(1,max(l)+1):
    if i not in l:
        print(i)
        break