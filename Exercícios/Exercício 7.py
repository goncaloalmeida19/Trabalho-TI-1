print("Samuel")

def med_bits(pr, P):
    codec = HuffmanCodec.from_frequencies(P)
    symbols, lengths = codec.get_code_len()
    media = sum((np.array(lengths) * np.array(pr)))
    return media