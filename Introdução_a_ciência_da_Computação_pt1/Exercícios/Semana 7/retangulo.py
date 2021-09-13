largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

i = 1
while i <= altura:
    j = 1
    while j <= largura:
        print("#",end='')
        j += 1
    print()
    i += 1