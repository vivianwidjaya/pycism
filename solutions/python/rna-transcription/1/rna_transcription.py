def to_rna(dna_strand):
    rna=""
    for strand in dna_strand:
        if strand == "G":
            rna += "C"
        elif strand == "C":
            rna += "G"
        elif strand == "T":
            rna += "A"
        elif strand == "A":
            rna += "U"
        else:
            rna+=""
    return rna
