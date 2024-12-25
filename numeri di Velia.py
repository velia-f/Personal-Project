import sympy as sp

def polinomio_fattoriale_e_differenze(k):
    # Definisco la variabile simbolica n
    n = sp.symbols('n')
    
    # Inizializzo il polinomio con il valore n
    polinomio = n
    
    # Moltiplico i termini da (n-1) a (n-k)
    for i in range(1, k + 1):
        polinomio *= (n - i)
    
    # Espando il polinomio
    polinomio_espanso = sp.expand(polinomio)
    
    # Ottengo i coefficienti del polinomio in ordine decrescente
    coefficienti = sp.Poly(polinomio_espanso, n).all_coeffs()
    
    # Rimuovo l'ultimo coefficiente che corrisponde a 0
    coefficienti = coefficienti[:-1]
    
    # Calcolo la differenza tra coefficienti successivi
    differenze = []
    for i in range(1, len(coefficienti)):
        differenza = coefficienti[i] - coefficienti[i - 1]
        differenze.append(differenza)
    
    # Calcolo la somma algebrica delle differenze
    somma_algebrica_differenze = sum(differenze)
    
    # Calcolo la somma dei coefficienti
    somma_coefficienti = sum(coefficienti)
    
    # Calcolo la frazione tra l'ultimo valore dei coefficienti e la somma algebrica delle differenze
    if len(coefficienti) > 0 and somma_algebrica_differenze != 0:
        ultimo_valore_coefficienti = coefficienti[-1]
        frazione = ultimo_valore_coefficienti / somma_algebrica_differenze
    else:
        frazione = None
    
    # Stampo il polinomio risultante
    print(f"Polinomio risultante dalla moltiplicazione dei primi {k} termini:")
    print(polinomio_espanso)
    
    # Stampo i coefficienti e le loro differenze
    print(f"\nCoefficienti: {coefficienti}")
    print(f"Differenze tra coefficienti successivi: {differenze}")
    
    # Stampo la somma algebrica delle differenze
    print(f"\nSomma algebrica delle differenze: {somma_algebrica_differenze}")
    
    # Stampo la somma dei coefficienti
    print(f"Somma dei coefficienti: {somma_coefficienti}")
    
    # Stampo la frazione
    if frazione is not None:
        print(f"\nFrazione: {ultimo_valore_coefficienti} / {somma_algebrica_differenze} = {frazione}")
    else:
        print("\nNon è possibile calcolare la frazione perché la somma algebrica delle differenze è zero o le liste sono troppo corte.")

# Esempio d'uso con k=7
polinomio_fattoriale_e_differenze(11)
##################################################################################################
import numpy as np

# Definire i valori noti
n = np.array([1, 2, 3, 4, 5, 6])
a = np.array([2, 11, 35, 85, 175, 322])

# Creare la matrice del sistema
X = np.vstack([n**4, n**3, n**2, n, np.ones(len(n))]).T

# Risolvere per i coefficienti
coefficients = np.linalg.lstsq(X, a, rcond=None)[0]

print("\n\nCoefficiente del polinomio del TERZO ordine (val const):", coefficients)


def calcola_polinomio(n, a, b, c, d, e):
    # Calcola il valore del polinomio
    P_n = a * n**4 + b * n**3 + c * n**2 + d * n + e
    return P_n

a, b, c, d, e = [float(c) for c in coefficients]

# Valore di n
n = 7 #per trovare il TERZO val al lvl k=n+1, ovvero n^10

# Calcolare il valore di P(n)
valore_polinomio = calcola_polinomio(n, a, b, c, d, e)

print(f"Il valore del polinomio per n={n} è: {valore_polinomio:.2f}")
##################################################################################################
import sympy as sp

# Definire la variabile simbolica
n = sp.symbols('n')

# Definire i valori della sequenza corrispondenti alle posizioni
values = [6, 50, 225, 735, 1960, 4536, 9450, 18150]

# Costruire l'espressione del polinomio generico di sesto grado
polynomial = sum(sp.symbols(f'a{i}') * n**i for i in range(6, -1, -1))

# Costruire un sistema di equazioni
equations = []
for pos, val in enumerate(values):
    equation = polynomial.subs(n, pos+1) - val
    equations.append(equation)

# Risolvere il sistema per trovare i coefficienti del polinomio
coefficients = sp.solve(equations)

# Sostituire i coefficienti trovati nel polinomio
polynomial = polynomial.subs(coefficients)

# Stampare il polinomio risultante
print("\n\nPolinomio risultante:")
print(polynomial)

# Calcolare il prossimo valore nella sequenza (n=9)
next_value = polynomial.subs(n, 9)
print(f"\nIl prossimo valore di QUARTO ordine nella sequenza (n=9) è: {next_value}")
