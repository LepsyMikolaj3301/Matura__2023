"""
suma kolejnych liczb podanego ciągu inputów


"""


liczby = []
while True:
    x = int(input("Liczba ( 0 kończy ciąg ) : ")) # liczba 0 kończy ciąg wejścia
    if x != 0:
        liczby.append(x)
    else:
        break
suma = liczby[0]
print(suma)
for num in liczby[1::]:
    suma += num
    print(suma)
