#if,else,elif serão de comparações livres
# o match/switch case será somente de igualdade
# o valor booleano será usado

#Faça um programa que solicite 3 numeros
# e mostre o maior deles

numero1= float(input("Insira o primeiro número: "))
numero2= float(input("Insira o segundo número: "))
numero3= float(input("Insira o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é maior")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo número é maior")
elif numero3 > numero1 and numero3 > numero2:
    print("O terceiro número é maior")

else:
    print("Os números são iguais")

#If usa somente uma vez