import itertools
import matplotlib.pyplot as plt

custo_e_peso = [[5, 200], [3, 150], [1, 52], [6, 317], [4, 250], [7, 254], [9, 223]]
peso_maximo_mochila = 500

def calcular_custo_total(itens):
    custo_total = 0
    peso_total = 0
    for i in range(len(itens)):
        if itens[i] == 1:
            custo_total += custo_e_peso[i][0]
            peso_total += custo_e_peso[i][1]
    if peso_total > peso_maximo_mochila:
        return 0  # Penaliza soluções inválidas que ultrapassam o peso máximo da mochila
    else:
        return custo_total

num_itens = len(custo_e_peso)
melhor_custo = 0
melhor_combinacao = []

for r in range(1, num_itens+1):
    combinacoes = list(itertools.combinations(range(num_itens), r))
    for combinacao in combinacoes:
        itens = [0] * num_itens
        for i in combinacao:
            itens[i] = 1
        custo = calcular_custo_total(itens)
        if custo > melhor_custo:
            melhor_custo = custo
            melhor_combinacao = itens

print("Melhor solução encontrada:")
print("Itens:", melhor_combinacao)
print("Custo total:", melhor_custo)

plt.bar(range(len(melhor_combinacao)), melhor_combinacao)
plt.xlabel('Itens')
plt.ylabel('Inclusão na Mochila')
plt.title('Itens Selecionados para a Mochila')
plt.show()