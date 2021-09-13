largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

i = 1
while i <= altura:
    if (i == 1 or i == altura):
        j = 1
        while j <= largura:
            print("#",end='')
            j += 1
        print()
        i += 1
    else:
        j = 1
        while j <= largura:
            if (j == 1 or j == largura):
                print("#",end='')
            else:
                print(' ',end='')
            j += 1
        print()
        i += 1