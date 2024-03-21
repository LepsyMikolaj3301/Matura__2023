"""
srednia arytmetyczna
ciąg n liczb, która z tych liczb jest najbliżej średniej arytmetycznej wszystkich liczb



"""


def srd_arytm(liczby: list) -> int:
    suma = 0
    for u in liczby:
        suma += u
    return suma // len(liczby)


tries = int(input("Proby: "))
for _ in range(tries):
    nums = list(input().split())
    for i in range(len(nums)):
        nums[i] = int(nums[i]) # :((
    srd = srd_arytm(nums)
    r, smalll = 100, 0 # r to roznica, smalll to liczba najblizej srd
    for i in nums:
        how_far = abs(srd - i)
        if how_far <= r:
            r = how_far
            smalll = i
    print(smalll)
