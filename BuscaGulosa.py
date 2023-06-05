import matplotlib.pyplot as plt

custo_e_peso = [[5, 200], [3, 150], [1, 52], [6, 317], [4, 250]]
peso_maximo_mochila = 500

def resolver_mochila(custo_e_peso, peso_maximo_mochila):
    custo_e_peso.sort(key=lambda x: x[0]/x[1], reverse=True)
    mochila = []
    peso_atual = 0
    custo_total = 0

    for item in custo_e_peso:
        if peso_atual + item[1] <= peso_maximo_mochila:
            mochila.append(1)
            peso_atual += item[1]
            custo_total += item[0]
        else:
            mochila.append(0)

    return custo_total, mochila

melhor_custo, melhor_combinacao = resolver_mochila(custo_e_peso, peso_maximo_mochila)

print("Melhor solução encontrada:")
print("Itens:", melhor_combinacao)
print("Custo total:", melhor_custo)

plt.bar(range(len(melhor_combinacao)), melhor_combinacao)
plt.xlabel('Itens')
plt.ylabel('Inclusão na Mochila')
plt.title('Itens Selecionados para a Mochila')
plt.show()
