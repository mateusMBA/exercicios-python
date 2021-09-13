def computador_escolhe_jogada(n,m):
    print("\n** Computador joga!\n")
    for removidas in range(1,m+1):
        if ((n-removidas) % (m+1) == 0):
            return (removidas)
    return (removidas)

def usuario_escolhe_jogada(n,m):
    print("\n** Sua vez!!")
    removidas = int(input("Digite quantas peças deseja remover: "))
    while(removidas > m or removidas <= 0 or removidas > n):
        print("\nOops! Jogada inválida! Tente de novo.")
        print(F"\nVocê só pode retirar até {m} peças!")
        removidas = int(input("Digite quantas peças deseja remover: "))
    return removidas

def campeonato():
    for jogo in range(3):
        print(F"\n****  Rodada {jogo+1}  ****")
        partida()
    print(F"\nPlacar: Você {placar_pessoa} X {placar_comp} Computador")
    

def partida():
    global placar_comp, placar_pessoa
    n = int(input("Quantas peças? "))
    while(n <= 0):
        print("\nO número de peças deve ser mairo que 0!!\n")
        n = int(input("Quantas peças? "))
    
    m = int(input("Limites de peças por jogada: "))
    while(m <= 0 ):
        print("\nNúmero inválido!!!\n")
        m = int(input("Limites de peças por jogada: "))
    
    if (n % (m+1) == 0):
        print("\nVocê começa!")
        usuario_jogou = False
        computador_jogou = True
    else:
        print("\nComputador começa!")
        usuario_jogou = True
        computador_jogou = False
	
    while (n != 0):
        if usuario_jogou:
            peças_removidas = computador_escolhe_jogada(n,m)
            usuario_jogou = False   
            computador_jogou = True
            n -= peças_removidas
            print(F"O computador retirou {peças_removidas} peças.")
            print(F"Restam {n} peças no tabuleiro")
            continue
        
        if computador_jogou:
            peças_removidas = usuario_escolhe_jogada(n,m)
            usuario_jogou = True
            computador_jogou = False
            n -= peças_removidas
            print(F"\nVocê retirou {peças_removidas} peças.")
            print(F"Restam {n} peças no tabuleiro")
            continue
            
    if computador_jogou:
        print("\n*** Computador Venceu! ***")
        placar_comp = placar_comp + 1
    else:
        print("\n*** Você Venceu!*** ")
        placar_pessoa += 1

placar_comp = 0
placar_pessoa = 0

print("******************************************\n")
print("           Vamos jogar NIM\n")
print("******************************************\n\n")

print("Selecione\n")
print("1 - jogar uma partida")
print("2 - jogar campeonato")

opcao = int(input("Opção: "))

while(opcao != 1 and opcao != 2):
    print("\nOpção inválida!!")
    print("\nSelecione\n")
    print("1 - jogar uma partida")
    print("2 - jogar campeonato")
    opcao = int(input("Opção: "))


if (opcao == 1):
    partida()
else:
    campeonato()