from random import randint

sorteado = randint(1, 10)

tentativas = 3

while True:
    palpite = int(input("Digite um número: "))
    
    if palpite == sorteado:
        print("Acertou!")
        break
    
    if palpite < sorteado:
        print("Muito baixo!")
    elif palpite > sorteado:
        print("Muito alto!")
        
    tentativas = tentativas - 1
    if tentativas == 0:
        print("Você perdeu!")
        break