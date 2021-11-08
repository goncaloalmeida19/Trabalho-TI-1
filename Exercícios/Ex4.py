import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy as np
from scipy.io import wavfile
from Fontes.huffmancodec import HuffmanCodec


def hist(fonte):
    # Dicionário alfabeto irá conter as ocorrências de cada
    # símbolo do alfabeto
    alfabeto = {}
    # Gerar alfabeto a usar no histograma
    if isinstance(fonte, str):
        # Caso seja texto
        for i in range(ord('A'),ord('Z')+1):
            alfabeto[chr(i)] = 0
        for i in range(ord('a'),ord('z')+1):
            alfabeto[chr(i)] = 0
    else:
        # Caso sejam números
        for i in range(2**int(str(fonte[0].dtype)[4:])):
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


# Média de bits por símbolo, pr e P seguem a mesma ordem visto que P é um dicionário
# com os símbolos do alfabeto e respetivas ocorrências, e pr é gerado a partir de P
def med_bits(pr, P):
    codec = HuffmanCodec.from_frequencies(P)
    symbols, lengths = codec.get_code_len()
    media = sum((np.array(lengths) * np.array(pr)))
    return media


# Função que calcula a média de bits por símbolo com os tamanhos ao quadrado
# (para depois usar na fórmula da variância)
def med_quad_bits(pr, P):
    codec = HuffmanCodec.from_frequencies(P)
    symbols, lengths = codec.get_code_len()

    media = sum((np.array(lengths)**2 * np.array(pr)))
    return media


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
# Ciclo 'for' que para cada ficheiro lido anteriormente imprime o seu gráfico, a sua entropia e
# a média de bits por símbolo através de 'med_bits'
for i in range(len(files)):
    alfabeto = hist(files[i])
    ocorrencias = np.array(list(alfabeto.values()))
    probabilidades = prob(ocorrencias)
    ent = entropia(probabilidades)
    print("Ficheiro \"" + file_names[i] + "\":")
    print("Entropia: {0:.4f} bits/símbolo".format(ent))
    m = med_bits(probabilidades, alfabeto)
    print("Média de bits por símbolo: {0:.4f} bits/símbolo".format(m))
    # Variância = E(X^2) - [E(X)]^2
    print("Variância: {0:.4f} bits/símbolo\n".format(med_quad_bits(probabilidades, alfabeto) - (m ** 2)))