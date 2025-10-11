# Programa para loja de frutas:
# Cabe 4 melâncias em 1 caixa

# Titulo:
print("Programa para loja de frutas")
print()

#Dados:
limite = 4

# Aqui a dona da loja irá inserir o número de frutas que ela possui;
# Nesse caso,é uma melância

qnt_melancia =float(input("Insira o número de melâncias: "))

qnt_caixas = qnt_melancia / limite
print(" A quantidade de caixas necessárias será de:",qnt_caixas,"caixa(s)")

# Multas:

if qnt_caixas > 200:
    multa = 0.50
    multa_total = multa * qnt_caixas
    print("A multa a ser paga será de:",multa_total,"R$")

else:
    print(" Não há nenhuma multa")
    print(" O frete é grátis")

# NÃO PODE COLOCAR ALGO DEPOIS DO ELSE



