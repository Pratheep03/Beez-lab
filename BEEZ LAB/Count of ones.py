x=int(input())
y=int(input())
countOnes=0
for i in range(x,y+1):
    k=list(str(i))
    countOnes+=k.count("1")
print(countOnes)

