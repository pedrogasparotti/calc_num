# Resultados do Sistema Mal Condicionado

Os resultados que você compartilhou do b.py estão alinhados com o comportamento esperado de um sistema mal condicionado:

* Para n=5, a solução é precisa porque o número de condição é administrável.

* Para n≥20, a eliminação Gaussiana sem pivoteamento falha devido a pivôs pequenos, uma consequência direta do mal condicionamento da matriz de Hilbert.

* Usar pivoteamento parcial ou `scipy.linalg.solve` resolve a falha, mas o erro ainda cresce com n (de 10^(-13) para n=5 até 10^(-5) para n=100) devido ao aumento exponencial no número de condição.
