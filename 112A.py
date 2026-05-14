first = input('').lower()
sercond = input('').lower()

discionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25,'z':26}

letter_1 = ''
letter_2 = ''

for i in range(0, len(first)):
    if not first[i] == sercond[i]:
        letter_1 = first[i]
        letter_2 = sercond[i]
        break

if len(letter_1) == 0:
    print('0')
else: 
    indice_1 = list(discionary.keys()).index(letter_1)    
    indice_2 = list(discionary.keys()).index(letter_2)  
    if indice_1 > indice_2:
        print('1')
    else:
        print('-1')