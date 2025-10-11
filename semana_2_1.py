# Programa de lanchonete de hamburguer de Micheal


# Dados
preco_hamburguer_total = 80
desconto_ingrediente = 10

# Tela de Inicio:
print("Loja de Hamburgueres do Micheal")
print("Faça o seu Pedido:")
print()

#Pergunta ao usuário:
print(" Digite 1 para sim e 0 para não")
print()

pergunta_preco_hamburguer = int(input("Irá querer o hamburguer com tudo incluso? "))
pergunta_desconto = int(input("Irá querer retirar a maionese?"))


# Uso do if:

if pergunta_preco_hamburguer == 1:
    print(" O Preço do hamburguer é:",preco_hamburguer_total,"R$")
if pergunta_preco_hamburguer ==0:
    pergunta_desconto = int(input("Irá querer retirar a maionese?"))

# Pergunta se tiver algum desconto:
if pergunta_desconto == 1:
    preco_desconto = preco_hamburguer_total - desconto_ingrediente
    print("O preço do seu hamburguer é de",preco_desconto,"R$")



# Questão do tempo de preparo:

tempo_hamburguer_tudo = 30
tempo_hamburguer_desconto = 2

# Se for preco total:
if pergunta_preco_hamburguer ==1:
    print("O tempo de preparo será de",tempo_hamburguer_tudo,"min")

#Se for preco com desconto:
if pergunta_desconto ==1:
    preco_novo = tempo_hamburguer_tudo - tempo_hamburguer_desconto
    print("O tempo de preparo será de",preco_novo,"min")







