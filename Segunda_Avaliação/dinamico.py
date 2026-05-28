
def multiplicacao_matrizes_pd(p):
    n = len(p)
    # Cria uma tabela
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            
            for k in range(i, j):
                
                q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    
   
    return m[1][n-1]