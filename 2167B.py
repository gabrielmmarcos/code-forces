q = int(input())

for _ in range(q):
    n = int(input())
    string = input('')
    
    count = 0
    count_2 = 0
    
    checker = True
    
    for i in range(0, len(s)-1):
        for j in range(0, n-1):
            if s[i] == s[j]:
                count +=1
            if s[i] == t[j]:
                count_2 += 1
        
        if not count == count_2:
            checker = False
            break
        count = 0
        count_2 = 0
            
    if checker:
        print('YES')
    else:
        print('NO')