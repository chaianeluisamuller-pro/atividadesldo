
#convidados = ["Chaiane","Otávio","Marli","Cláudio"]
#pergunta = input("Verifique quem foi convidado: ")

#if pergunta in convidados:
   # print(f"O convidada(a) {pergunta} foi convidado(a)")
#else:
    #print(f"O {pergunta} não foi convidado(a)")


#numero = -1
#for numero in range (1,11,2):
    #print(numero)

print("1 - Maçã | 2 - Banana | 3- Laranja")

numero = int(input("Digite um número: "))

match numero:
    case 1:
        print("Maçã")
match numero:
    case 2:
        print("Banana")
match numero:
    case 3:
        print("Laranja")
match numero:
    case _:
        print("Numero inválido ❌")




