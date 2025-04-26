import numpy as np

# Matriz do Sistema 1
A1 = np.array([[1, -1], [1, -1.00001]])
# Matriz do Sistema 2
A2 = np.array([[1, -1], [1, -0.99999]])

# Cálculo do número de condição
cond_A1 = np.linalg.cond(A1)
cond_A2 = np.linalg.cond(A2)

print(f"Número de condição de A1: {cond_A1}")
print(f"Número de condição de A2: {cond_A2}")