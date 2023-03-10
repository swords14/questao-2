import random

# Lê os limites do intervalo de números do usuário
inferior = int(input("Digite o limite inferior do intervalo: "))
superior = int(input("Digite o limite superior do intervalo: "))

# Sorteia um número aleatório dentro do intervalo especificado
numero_sorteado = random.randint(inferior, superior)

# Inicializa a variável de palpite do usuário com um valor inválido
palpite = 0

# Loop principal do jogo
while palpite != numero_sorteado:
    # Lê um palpite do usuário e converte para inteiro
    palpite = int(input("Digite um número entre " + str(inferior) + " e " + str(superior) + ": "))

    # Verifica se o palpite está correto e dá uma dica caso contrário
    if palpite == numero_sorteado:
        print("Parabéns, você acertou o número!")
    elif palpite < numero_sorteado:
        print("O número sorteado é maior que " + str(palpite))
    else:
        print("O número sorteado é menor que " + str(palpite))