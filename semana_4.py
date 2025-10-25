
print("Somente de 0-100")

numero=  int(input("insira um numero: "))

#Numero for inválido:
while  numero <=0 or numero >=100:
    print("Numero Inválido ❌")
    print("❌ERRO❌")
    print("Tente novamente")
    numero = int(input("insira um numero: "))

#Numero for válido:
if numero >=0 or numero <=100:
    print("Numero Válido ✔")


