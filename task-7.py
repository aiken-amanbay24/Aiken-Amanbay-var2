nums=list(map(int, input().split()))
dupl=[]
for i in nums:
    if i not in dupl:
        dupl.append(i)
print(dupl)