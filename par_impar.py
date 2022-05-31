import random
rdn = random.randint(1,10)
escolha =""
num = 0
num2 = 0
num2 = rdn

while escolha != "par" and escolha != "impar":
    escolha = str(input("Par ou Impar?\n"))
    if escolha != "par" and escolha != "impar":
        print("\nInforme um valor válido: par ou impar\n")

num = int(input("Digite um número de 1 até 10:\n"))
if escolha == "par":
    print(f"O BOT escolheu o valor {num2}")
    if (num + num2) % 2 == 0:
        print("YOU WIN!!!")
    else:
        print("YOU LOSE!!!")
else:
    print(f"O BOT escolheu o valor {num2}")
    if (num + num2) % 2 != 0:
        print("YOU WIN!!!")
    else:
        print("YOU LOSE!!!")