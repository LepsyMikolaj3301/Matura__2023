'''
napisz rekurencyjną funkcję power3 obliczającą wartość funkcji:

x^n = 1 dla n < 1
x^n = (x^(n/2))^2 dla n parzystego
x^n = x* (x^(n/2))^2 dla n nieparzystego

'''

def power3(x, n):
    if n < 1:
        return 1
    elif n%2 == 0:
        return power3(x, int(n/2)) * power3(x, int(n/2))
    elif n%2 != 0:
        return x * power3(x, int(n/2)) * power3(x, int(n/2)) 
print(power3(2,10))