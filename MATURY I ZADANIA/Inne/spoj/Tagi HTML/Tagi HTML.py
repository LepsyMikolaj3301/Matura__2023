"""
wszystkie znaki, pomiędzy "</ >" oraz "< >"

"""
# dajemy UPPER
#
# jeśli nie, wyszukujemy sobie odpowiednik w ASCII przez ord oraz chr


with open("Tagi HTML.txt", 'r') as file:
    the_HTML = ''
    for line in file:
        the_HTML += line
with open("Tagi HTML_o.txt", 'w') as file_o:
    new_HTML = ''
    the_splitter = False
    for character in the_HTML:
        if character == '<':
            the_splitter = True
        elif character == '>':
            the_splitter = False
        if the_splitter:
            new_HTML += character.upper()
        else:
            new_HTML += character
    file_o.write(new_HTML)


