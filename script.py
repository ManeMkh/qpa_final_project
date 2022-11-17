def dna_to_rna(seq: str):
    return seq.replace("T", "U")

# RNA table taken from wikipedia
rna_codon_table = {
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "AAA": "K", "AAG": "K",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "UUA": "L", "UUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": 'Q', 'CAG': 'Q',
    'CGU': 'R', "CGC": 'R', "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}


def convert_rna_to_protein(arg: str) -> str:
    protein = ""

    for i in range(0, len(arg)-3, 3):
        if rna_codon_table[arg[i: i+3]] == "STOP":
            protein += "."
        else:
            protein += rna_codon_table[arg[i:i+3]]
    return protein
