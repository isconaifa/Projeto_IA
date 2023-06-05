import random
import matplotlib.pyplot as plt

custo_e_peso = [[5, 200], [3, 150], [1, 52], [6, 317], [4, 250], [5, 251], [7, 301]]
peso_maximo_mochila = 500
tamanho_populacao = 50
taxa_mutacao = 0.1
numero_geracoes = 100

def fitness(individuo):
    custo_total = 0
    peso_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            custo_total += custo_e_peso[i][0]
            peso_total += custo_e_peso[i][1]
    if peso_total > peso_maximo_mochila:
        return 0  # Penaliza soluções inválidas que ultrapassam o peso máximo da mochila
    else:
        return custo_total

def criar_individuo():
    return [random.randint(0, 1) for _ in range(len(custo_e_peso))]

def criar_populacao():
    return [criar_individuo() for _ in range(tamanho_populacao)]

def selecionar_pais(populacao):
    pais = random.choices(populacao, weights=[fitness(individuo) for individuo in populacao], k=2)
    return pais[0], pais[1]

def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao(individuo):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Troca 0 por 1 ou 1 por 0

populacao = criar_populacao()
melhores_fitness = []

for geracao in range(numero_geracoes):
    fitness_populacao = [(individuo, fitness(individuo)) for individuo in populacao]
    fitness_populacao = sorted(fitness_populacao, key=lambda x: x[1], reverse=True)

    melhores_fitness.append(fitness_populacao[0][1])

    nova_populacao = []

    for _ in range(int(tamanho_populacao / 2)):
        pai1, pai2 = selecionar_pais(populacao)
        filho1, filho2 = crossover(pai1, pai2)
        mutacao(filho1)
        mutacao(filho2)
        nova_populacao.append(filho1)
        nova_populacao.append(filho2)

    populacao = nova_populacao

melhor_individuo = max(fitness_populacao, key=lambda x: x[1])[0]
melhor_fitness = max(fitness_populacao, key=lambda x: x[1])[1]

print("Melhor solução encontrada:")
print("Itens:", melhor_individuo)
print("Custo total:", melhor_fitness)

plt.plot(range(numero_geracoes), melhores_fitness)
plt.xlabel('Geração')
plt.ylabel('Melhor Fitness')
plt.title('Evolução do Melhor Fitness')
plt.show()