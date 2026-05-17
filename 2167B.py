q = int(input())

for _ in range(q):
    n = int(input())
    string = input('')
    text = string.split(' ')
    s = text[0]
    t = text[1]
    
    letra_em_ordem_s = sorted(s)
    verifica_s = "".join(letra_em_ordem_s)
    letra_em_ordem_t = sorted(t)
    verifica_t = "".join(letra_em_ordem_t)
    
    checker = True
    
    for i in range(0, len(s)):
        if not verifica_s == verifica_t:
            checker = False
            break
    
    # count = 0
    # count_2 = 0 
    # for i in range(0, len(s)-1):
    #     for j in range(0, len(s)-1):
    #         if s[i] == s[j]:
    #             count +=1
    #         if s[i] == t[j]:
    #             count_2 += 1
        
    #     if not count == count_2:
    #         checker = False
    #         break
    #     count = 0
    #     count_2 = 0
            
    if checker:
        print('YES')
    else:
        print('NO')