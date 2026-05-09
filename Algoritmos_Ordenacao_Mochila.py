import time


valores = [0, 60, 150, 120, 160, 200, 150, 60] 
pesos = [0, 1, 3, 3, 4, 5, 5, 6]
n = len(valores) - 1


chamadas_recursivas = 0

def mochila_backtracking(i, W):
    global chamadas_recursivas
    chamadas_recursivas += 1
    
    if i == 0 or W == 0:
        return 0
    
    if pesos[i] > W:
        return mochila_backtracking(i - 1, W)
    
    usar = valores[i] + mochila_backtracking(i - 1, W - pesos[i])
    nao_usar = mochila_backtracking(i - 1, W)
    
    return max(usar, nao_usar)


def mochila_dinamica(W):
  
    M = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if pesos[i] <= w:
                M[i][w] = max(valores[i] + M[i-1][w-pesos[i]], M[i-1][w])
            else:
                M[i][w] = M[i-1][w]
                
    return M[n][W]


for cap in [6, 10]:
    print(f"\n--- Teste com W = {cap} ---")
    
   
    chamadas_recursivas = 0
    start = time.perf_counter()
    res_bt = mochila_backtracking(n, cap)
    end = time.perf_counter()
    print(f"Backtracking: Resultado={res_bt}, Tempo={end-start:.8f}s, Chamadas={chamadas_recursivas}")
    
  
    start = time.perf_counter()
    res_pd = mochila_dinamica(cap)
    end = time.perf_counter()
    print(f"Dinâmico: Resultado={res_pd}, Tempo={end-start:.8f}s")