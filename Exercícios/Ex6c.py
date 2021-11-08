import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Função que passada uma tabela de probabilidades devolve a entropia
def entropia(p):
    p = p[p != 0]
    return -sum(p * np.log2(p))


# Função que devolve uma tabela com as probabilidades de ocorrência de cada elemento da tabela passada como argumento
def prob(t):
    ocorr = {}
    for i in t:
        if i not in ocorr:
            ocorr[i] = 0
        else:
            ocorr[i] += 1
    ocorr = np.array(list(ocorr.values()))

    return ocorr / sum(ocorr)


def print_info_mutua(info):
    print("\tInformação Mútua = [", end="")
    for i in range(len(info)):
        if i != 0:
            print(" ", end="")
        print("%.4f" % info[i], end="")
    print("]")


# Calcula a informação mútua entre a query e o target tendo em conta o passo (step)
def informacao_mutua(target, query, step):
    p_query = prob(query)
    info = []
    for i in range(0, len(target)-len(query)+1, step):
        # Obter a secção do target a analisar
        p_target = prob(target[i:i+len(query)])

        # Obter a interseção da query com a parte to target a testar
        intersecao = [(query[j], target[j + i]) for j in range(len(query))]
        p_intersecao = prob(intersecao)

        ent_target_query_cond = entropia(p_intersecao) - entropia(p_query)  # H(Y|X) = H(X,Y) - H(Y)
        info.append(entropia(p_target) - ent_target_query_cond)  # I(X,Y) = H(X) -  H(Y|X)
    return info


query = list(wavfile.read("..\Fontes\guitarSolo.wav")[1])
# Ler os ficheiros target (Song0X.wav) e obter a informação mútua entre cada um e a query
songs = [list(wavfile.read("..\Fontes\Song0" + str(i) + ".wav")[1]) for i in range(1, 8)]
infos = [informacao_mutua(song, query, round(len(query)/4)) for song in songs]
for i in range(len(infos)):
    print("Song0"+str(i + 1)+":")
    plt.plot(infos[i])
    plt.show()
    print_info_mutua(infos[i])
print()

# Obter a informação mútua máxima de cada um e ordená-los por ordem decrescente desta
infoMutua = {"Song0"+str(i+1): max(infos[i]) for i in range(len(infos))}
infoMutua = sorted(infoMutua.items(), key=lambda x: x[1], reverse=True)
print("Máximo:")
for k, v in infoMutua:
    print("\t" + k + ": %.4f bits/símbolo" % v)
