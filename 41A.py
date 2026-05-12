s = input('')
t = input('')

if not len(s) == len(t):
    print('NO')
else:
    check = False
    for i in range(0, len(s)-1//2):
        if s[i] == t[len(t) - 1 -i]:
            continue
        check = True
        break
        
    if check == True:
        print('NO')
    else:      
        print('YES')
