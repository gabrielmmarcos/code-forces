name = input('')

letter_repeated = []
count = 0

for i in range(0, len(name) ):
    for j in range(0, len(name)):
        if name[i] == name[j]:
            count += 1
            if count > 1:
                if name[i] in letter_repeated:
                    continue
                letter_repeated.append(name[j])
                count = 0
    count = 0


qtd = (len(name) - len(letter_repeated))
print(qtd)
if qtd % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
  
        