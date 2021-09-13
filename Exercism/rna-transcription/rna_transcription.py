def to_rna(dna_strand):
    transcp = {'A':'U','T':'A','C':'G','G':'C'}
    new = ''
    for i in dna_strand:
        new += transcp.get(i)    
    return(new)
