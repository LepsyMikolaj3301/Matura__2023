"""
gracz A -> a żetonów
gracz B -> b żetonów
1. gracz który ma mniej żetonów, może wykonać ruch
robiąc ruch, gracz zabiera tyle żetonów b ile ma a i te żetony są wywalane z gry
2. gra sie kończy gdy żaden nie może wykonać ruchu

testy
a1 b1 -> ich żetony


"""

tries = int(input("Proby: "))
for _ in range(tries):
    a, b = input().split()
    a, b = int(a), int(b)
    while True:
        if a > b:
            a -= b
        elif b > a:
            b -= a
        else:
            break
    print(a + b)
    