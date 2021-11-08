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

    #print(alfabeto)

    plt.bar(alfabeto.keys(), alfabeto.values())
    plt.show()

# Testes
# hist(np.array([1, 2, 3, 4, 5, 6, 8, 8, 2, 1, 3, 3, 5, 7, 8, 9], dtype=np.uint8))
# hist("jaidjsdiajdiadjasdi")
