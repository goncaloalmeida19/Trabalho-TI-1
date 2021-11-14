import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy as np
from scipy.io import wavfile


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
        for i in range(10):
            alfabeto[str(i)] = 0
    else:
        # Caso sejam números
        bits = 2**int(str(fonte[0].dtype)[4:])
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


# Função que passada uma tabela de probabilidades devolve a entropia
def entropia(p):
    p = p[p != 0]
    return -sum(p*np.log2(p))


# Função que devolve a compressão máxima de um alfabeto
# Entropia máxima = log2(tamanho do alfabeto)
# Compressão máxima (%) = (Entropia máxima - Entropia) / (Entropia máxima) * 100
def comp_max(alf, ent):
    ent_max = np.log2(len(alf))
    return (ent_max-ent)/ent_max * 100


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
# Ciclo 'for' que para cada ficheiro lido anteriormente imprime o seu histograma e a sua entropia
for i in range(len(files)):
    alfabeto = hist(files[i])
    ocorrencias = np.array(list(alfabeto.values()))
    probabilidades = prob(ocorrencias)
    ent = entropia(probabilidades)
    print("Entropia de \"" + file_names[i] + "\": %.4f" % ent, "bits/símbolo")
    print("Compressão máxima de \"" + file_names[i] + "\": %.4f" % comp_max(alfabeto, ent), "%\n")
