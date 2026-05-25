# dinamico.py

def multiplicacao_matrizes_pd(p):
    n = len(p)
    # Cria uma tabela n x n preenchida com 0
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    # L é o comprimento da cadeia de matrizes
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            
            for k in range(i, j):
                # Custo da subestrutura ótima
                q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    
    # O resultado ótimo final fica no topo da tabela
    return m[1][n-1]