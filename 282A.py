n = int(input())
 
count = 0

for _ in range(n):
    linha = input()
    if '++' in linha:
        count+=1
    else:
        count -= 1

print(count)
    
    
    
    