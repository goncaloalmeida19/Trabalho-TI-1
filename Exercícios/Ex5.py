import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy as np
from scipy.io import wavfile


def hist(fonte):
    # Dicionário alfabeto irá conter as ocorrências de cada
    # símbolo do alfabeto
    alfabeto = {}
    # Gerar alfabeto a usar no histograma
    for i in fonte:
        if not i in alfabeto:
            alfabeto[i] = 0

    for i in fonte:  # Registar uma ocorrência (i é a chave)
        alfabeto[i] += 1

    plt.bar([str(i) for i in list(alfabeto.keys())], alfabeto.values())
    plt.show()
    return alfabeto


# agrupa os elementos de uma lista 2 a 2
def agrupa(f):
    list = []
    for i in range(int(len(f) / 2 - 1)):
        list.append((f[i * 2], f[i * 2 + 1]))
    return list


# Função que devolve uma tabela com as probabilidades de ocorrência de cada elemento da tabela passada como argumento
def prob(ocorr):
    return ocorr / sum(ocorr)


# Função que passada uma tabela de probabilidades devolve a entropia
def entropia(p):
    p = p[p != 0]
    return -sum(p*np.log2(p))


# Leitura dos ficheiros de imagem e som
kid = list(np.array(mp.imread("..\Fontes\kid.bmp")).flatten())
homer = list(np.array(mp.imread("..\Fontes\homer.bmp")).flatten())
homerBin = list(np.array(mp.imread("..\Fontes\homerBin.bmp")).flatten())
guitarSolo = list(wavfile.read("..\Fontes\guitarSolo.wav")[1])

# Leitura do ficheiro de texto
english = ""
with open("..\Fontes\english.txt", "r") as file:
    for l in file:
        for c in l:
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                english += c

files = [kid, homer, homerBin, guitarSolo, english]
file_names = ["kid.bmp", "homer.bmp", "homerBin.bmp", "guitarSolo.wav", "english.txt"]
# Ciclo 'for' que para cada ficheiro lido anteriormente agrupa os símbolos dois a dois e
# mostra, em relação aos símbolos agrupados, o seu histograma e a sua entropia
for i in range(len(files)):
    f = agrupa(files[i])
    alfabeto = hist(f)
    ocorrencias = np.array(list(alfabeto.values()))
    probabilidades = prob(ocorrencias)
    # Divide-se a entropia por 2 visto que se pretende obter o número
    # de bits por símbolo e não o número de bits por tuplo de símbolos
    ent = entropia(probabilidades)/2
    print("Entropia de \"" + file_names[i] + "\":", "%.4f" % ent, "bits/símbolo")
