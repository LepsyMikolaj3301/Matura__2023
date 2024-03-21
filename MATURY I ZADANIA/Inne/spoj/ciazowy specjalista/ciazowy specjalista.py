"""
matka jest o 21 lat starsza od swojego dziecka
za 6 lat dziecko będzie 5 razy młodsze od matki

x -> wiek dziecka
x + 21 -> wiek matki

5 * (x + 6) = x + 27
4x = -3
x = -3/4 -> 9 miesięcy

z ( dziecko + y ) = dziecko + x
z*dziecko - dziecko = x - zy
dziecko( z - 1 ) = x - zy
dziecko = x - zy / ( z - 1)


dobry wzór:
a: wiek dziecka
a = x + y - zy / z - 1

"""


DANE = []
with open("ciozowy specjalista.txt", 'r') as file:
    for lines in file:
        line = lines.rstrip('\n')
        DANE.append(line.split())
proby = int(DANE[0][0])
odpowiedzi = []
for i in range(1, proby + 1):
    o_X_lat, za_Y_lat, z_razy_m = DANE[i]
    o_X_lat, za_Y_lat, z_razy_m = int(o_X_lat), int(za_Y_lat), int(z_razy_m)
    ciaza = -1 * (o_X_lat + za_Y_lat - (z_razy_m * za_Y_lat)) / (z_razy_m - 1)
    odpowiedzi.append(int(ciaza * 12))   #ciaza jest ułamkiem lat, my chcemy miesiące
print(odpowiedzi)
