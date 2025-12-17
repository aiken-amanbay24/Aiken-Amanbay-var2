count_vowels=list(input())
vowels=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in count_vowels:
    if i in vowels:
        count+=1
print(count)