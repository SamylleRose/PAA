# main.py

import time
import tracemalloc
import random
import matplotlib.pyplot as plt

# Importando as funções dos outros arquivos que criamos
from recursivo import multiplicacao_matrizes_recursiva
from dinamico import multiplicacao_matrizes_pd

def medir_desempenho(funcao, p, eh_recursivo=False):
    """Função auxiliar para medir tempo e memória de uma execução."""
    tracemalloc.start()
    inicio = time.perf_counter()
    
    if eh_recursivo:
        # A versão recursiva precisa dos índices iniciais e finais
        funcao(p, 1, len(p) - 1)
    else:
        # A versão dinâmica precisa apenas do array
        funcao(p)
        
    fim = time.perf_counter()
    _, pico_memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    tempo = fim - inicio
    memoria_kb = pico_memoria / 1024
    return tempo, memoria_kb

def main():
    
    tamanhos = [5, 8, 11, 14, 17] #Cenario de teste
    

    tempos_rec = []
    memoria_rec = []
    tempos_pd = []
    memoria_pd = []
    
    print(f"{'Qtd Matrizes':<15} | {'Tempo Rec (s)':<15} | {'Tempo PD (s)':<15} | {'Memória Rec (KB)':<18} | {'Memória PD (KB)':<18}")
    print("-" * 90)
    
    for n in tamanhos:
        # Gera um array aleatório 'p' de dimensões das matrizes para o teste
        p = [random.randint(10, 100) for _ in range(n + 1)]
        
        # Medição da versão Recursiva
        t_rec, m_rec = medir_desempenho(multiplicacao_matrizes_recursiva, p, eh_recursivo=True)
        tempos_rec.append(t_rec)
        memoria_rec.append(m_rec)
        
        # Medição da versão Dinâmica
        t_pd, m_pd = medir_desempenho(multiplicacao_matrizes_pd, p, eh_recursivo=False)
        tempos_pd.append(t_pd)
        memoria_pd.append(m_pd)
        
        # Imprime a linha da tabela formatada
        print(f"{n:<15} | {t_rec:<15.6f} | {t_pd:<15.6f} | {m_rec:<18.4f} | {m_pd:<18.4f}")

    
    # GERAÇÃO DOS GRÁFICOS
    # Gráfico 1: Tempo de Execução 
    plt.figure(figsize=(8, 5))
    plt.plot(tamanhos, tempos_rec, label='Recursivo (Força Bruta)', marker='o', color='#dc3545', linewidth=2)
    plt.plot(tamanhos, tempos_pd, label='Programação Dinâmica', marker='s', color='#007bff', linewidth=2)
    plt.title('Tempo de Execução vs Quantidade de Matrizes', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Quantidade de Matrizes (n)')
    plt.ylabel('Tempo (segundos)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    plt.savefig('grafico_tempo.jpg', dpi=300, format='jpg')
    plt.close()

    # Gráfico 2: Consumo de Memória 
    plt.figure(figsize=(8, 5))
    plt.plot(tamanhos, memoria_rec, label='Recursivo (Força Bruta)', marker='o', color='#dc3545', linewidth=2)
    plt.plot(tamanhos, memoria_pd, label='Programação Dinâmica', marker='s', color='#007bff', linewidth=2)
    plt.title('Consumo de Memória vs Quantidade de Matrizes', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Quantidade de Matrizes (n)')
    plt.ylabel('Pico de Memória (KB)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    plt.savefig('grafico_memoria.jpg', dpi=300, format='jpg')
    plt.close() 

    print("\nSucesso! As imagens 'grafico_tempo.jpg' e 'grafico_memoria.jpg' foram geradas e salvas na sua pasta.")

if __name__ == '__main__':
    main()