import numpy as np

# Função que passada uma tabela de probabilidades devolve a entropia
def entropia(p):
    p = p[p != 0]
    return -sum(p * np.log2(p))


# Função que devolve uma tabela com as probabilidades de ocorrência de cada elemento da tabela passada como argumento
def prob(t):
    ocorr = {}
    for i in t:
        ocorr[i] = t.count(i)
    ocorr = np.array(list(ocorr.values()))

    return ocorr / sum(ocorr)


def print_info_mutua(info):
    print("Informação Mútua = [", end="")
    for i in range(len(info)):
        if i != 0:
            print(" ", end="")
        print("%.4f" % info[i], end="")
    print("]")


# Calcular a informação mútua entre a query e o target tendo em conta o passo (step)
def informacao_mutua(target, query, step):
    p_query = prob(query)
    info = []
    for i in range(0, len(target)-len(query)+1, step):
        # Tabela de probabilidades de uma secção do target
        p_target = prob(target[i:i + len(query)])

        # Obter a interseção da query com a secção to target a testar
        intersecao = [(query[j], target[j + i]) for j in range(len(query))]
        p_intersecao = prob(intersecao)

        ent_target_query_cond = entropia(p_intersecao) - entropia(p_query)  # H(X|Y) = H(X,Y) - H(Y)
        info.append(entropia(p_target) - ent_target_query_cond)  # I(X,Y) = H(X) -  H(X|Y)
    return info


query = [2, 6, 4, 10, 5, 9, 5, 8, 0, 8]
target = [6, 8, 9, 7, 2, 4, 9, 9, 4, 9, 1, 4, 8, 0, 1, 2, 2, 6, 3, 2, 0, 7, 4, 9, 5, 4, 8, 5, 2, 7, 8, 0, 7, 4,
                   8, 5, 7, 4, 3, 2, 2, 7, 3, 5, 2, 7, 4, 9, 9, 6]

info = informacao_mutua(target, query, 1)
print_info_mutua(info)
