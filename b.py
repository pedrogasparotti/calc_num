import numpy as np
from scipy.linalg import hilbert
import scipy.linalg as la

# Função para gerar o vetor b
def generate_b(n):
    b = np.zeros(n)
    for i in range(1, n + 1):
        b[i-1] = sum(1 / (i + j - 1) for j in range(1, n + 1))
    return b

# Função para resolver o sistema usando scipy.linalg.solve
def solve_hilbert_system_scipy(n):
    H = hilbert(n)
    b = generate_b(n)
    x_exact = np.ones(n)
    x_numeric = la.solve(H, b)
    error = np.linalg.norm(x_numeric - x_exact) / np.linalg.norm(x_exact)
    return x_numeric, error

# Testar para n = 5, 20, 50, 100
n_values = [5, 20, 50, 100]
for n in n_values:
    x_numeric, error = solve_hilbert_system_scipy(n)
    print(f"\nResultados para n = {n}:")
    print(f"Solução numérica (primeiros 5 elementos): {x_numeric[:5]}")
    print(f"Erro relativo: {error:.2e}")