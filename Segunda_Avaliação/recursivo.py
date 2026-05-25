# recursivo.py

def multiplicacao_matrizes_recursiva(p, i, j):
    # Caso base: apenas uma matriz, custo de multiplicação é 0
    if i == j:
        return 0
    
    min_custo = float('inf')
    
    # Testa todas as posições possíveis para "quebrar" a cadeia
    for k in range(i, j):
        custo = (multiplicacao_matrizes_recursiva(p, i, k) +
                 multiplicacao_matrizes_recursiva(p, k + 1, j) +
                 p[i-1] * p[k] * p[j])
        
        if custo < min_custo:
            min_custo = custo
            
    return min_custo