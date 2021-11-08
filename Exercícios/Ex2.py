import matplotlib.pyplot as plt
import numpy as np


def hist(fonte):
    # Dicionário alfabeto irá conter as ocorrências de cada
    # símbolo do alfabeto
    alfabeto = {}
    # Gerar alfabeto a usar no histograma
    if isinstance(fonte, str):
        # Caso seja texto
        for i in range(ord('A'), ord('Z') + 1):
            alfabeto[chr(i)] = 0
        for i in range(ord('a'), ord('z') + 1):
            alfabeto[chr(i)] = 0
    else:
        # Caso sejam números
        bits = 2 ** int(str(fonte[0].dtype)[4:])
        for i in range(bits):
            alfabeto[i] = 0

    for i in fonte:  # Registar uma ocorrência (i é a chave)
        alfabeto[i] += 1

    plt.bar(alfabeto.keys(), alfabeto.values())
    plt.show()
    return alfabeto


# Função que devolve uma tabela com as probabilidades de ocorrência de cada elemento da tabela passada como argumento
def prob(ocorr):
    return ocorr / sum(ocorr)


def entropia(p):
    p = [i for i in p if i != 0]  # Ciclo 'for' que retira todos os zeros da tabela p
    # Fórmula da entropia
    return -sum(p*np.log2(p))


alfabeto = hist('a' * 90 + 'b' * 5 + 'c' * 3 + 'd' * 2)
ocorrencias = np.array(list(alfabeto.values()))
probabilidade = prob(ocorrencias)
ent = entropia(probabilidade)
print("Entropia: %.4f" % ent, "bits/símbolo")