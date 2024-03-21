"""
palindrom
lecisz kurwa od lewej i prawej strony i jak nie pasuje to na butle siadasz
elo
"""


def palindrom(slowo: str) -> bool:
    i, j = 0, len(slowo) - 1
    while i < j:
        if slowo[i] != slowo[j]:
            return False
        i += 1
        j -= 1
    return True

print(palindrom("ALAMALA"))