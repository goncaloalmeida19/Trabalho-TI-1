print("Samuel")

def med_bits(pr, P):
    codec = HuffmanCodec.from_frequencies(P)
    symbols, lengths = codec.get_code_len()
    media = sum((np.array(lengths) * np.array(pr)))
    return media


def agrupa(f):
    list = []
    for i in range(int(len(f) / 2 - 1)):
        list.append((f[i * 2], f[i * 2 + 1]))
    return list