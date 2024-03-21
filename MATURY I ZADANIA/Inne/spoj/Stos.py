"""
stos


"""
table = []
for _ in range(10):
    table.append(0)
iterajnik = 0
while True:
    if input() == '+':
        if iterajnik == 10:
            print(':(')
        else:
            table[iterajnik] = int(input())
            iterajnik += 1
            print(':)')
    else:
        if iterajnik == 0:
            print(':(')
        else:
            iterajnik -= 1
            print(table[iterajnik])
