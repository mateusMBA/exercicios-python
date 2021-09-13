def proteins(strand):
    protein_dict = {'Stop': ['UAA','UAG','UGA'],
                'Methionine':['AUG'],
                'Phenylalanine':['UUU','UUC'],
                'Leucine':['UUA','UUG'],
                'Serine':['UCU','UCC','UCA','UCG'],
                'Tyrosine':['UAU','UAC'],
                'Cysteine':['UGU','UGC'],
                'Tryptophan':['UGG']}


    transcp = []
    for i in range(0,len(strand),3):
        aux = strand[i:i+3]
        for k,j in protein_dict.items():
            if (aux in protein_dict.get('Stop')):
                return(transcp)
            if (aux in j):
                transcp.append(k)

    return(transcp)
