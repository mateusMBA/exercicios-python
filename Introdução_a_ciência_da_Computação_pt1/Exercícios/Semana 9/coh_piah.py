import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    comparação = [(as_a[i] - as_b[i]) for i in range(len(as_a))]
    return  similaridade(comparação)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = tamanho_medio_palavra(texto)
    ttr = type_token(texto)
    hlr = razao_hapax(texto)
    sal = tamanho_medio_sentença(texto)
    sac = complexidade_sentença(texto)
    pal = tamanho_medio_frase(texto)
    return [wal,ttr,hlr,sal,sac,pal]
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = dict()
    numero_texto = 1
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        similar = similaridade(assinatura)
        similaridades[similar] = numero_texto
        numero_texto += 1
    return similaridades.get(min(similaridades.keys()))

def tamanho_medio_palavra(texto):
    sentenças = separa_sentencas(texto)
    frases = []
    for i in sentenças:
        frases.extend(separa_frases(i))
    palavras = []
    for j in frases:
        palavras.extend(separa_palavras(j))
    soma_palavras = 0
    for i in palavras:
        soma_palavras += len(i)
    return (soma_palavras / len(palavras))

def type_token(texto):
    sentenças = separa_sentencas(texto)
    frases = []
    for i in sentenças:
        frases.extend(separa_frases(i))
    palavras = []
    for j in frases:
        palavras.extend(separa_palavras(j))
    palavras_diferentes = n_palavras_diferentes(palavras)
    return palavras_diferentes/len(palavras)

def razao_hapax(texto):
    sentenças = separa_sentencas(texto)
    frases = []
    for i in sentenças:
        frases.extend(separa_frases(i))
    palavras = []
    for j in frases:
        palavras.extend(separa_palavras(j))
    palavras_unicas = n_palavras_unicas(palavras)
    return palavras_unicas/len(palavras)

def tamanho_medio_sentença(texto):
    sentenças = separa_sentencas(texto)
    soma_caracteres = 0
    for i in sentenças:
        soma_caracteres += len(i) 
    return soma_caracteres / len(sentenças)

def complexidade_sentença(texto):
    sentenças = separa_sentencas(texto)
    frases = []
    for i in sentenças:
        frases.extend(separa_frases(i))
    return len(frases)/len(sentenças)

def tamanho_medio_frase(texto):
    sentenças = separa_sentencas(texto)
    frases = []
    for i in sentenças:
        frases.extend(separa_frases(i))
    soma_caracteres = 0
    for j in frases:
        soma_caracteres += len(j) 
    return soma_caracteres / len(frases)

def similaridade(assinatura):
    soma_traços = 0
    for i in assinatura:
        soma_traços += abs(i)
    return soma_traços/6