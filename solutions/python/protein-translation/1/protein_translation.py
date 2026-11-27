amino_acid_table= {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UCG": "Serine",
}
stop = ["UAA", "UAG", "UGA"]

def proteins(strand):
    name = []
    for i in range(0, len(strand), 3):
        if strand[i:i+3] in amino_acid_table:
            name.append(amino_acid_table[strand[i:i+3]])
        elif strand[i:i+3] in stop:
            return name
    return name
        