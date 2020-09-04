a=input().strip()
print(a)
count=0
for i in a:
    if i.isalpha():
        count+=1
print("Number of characters:",end=" ")
print(count)
        