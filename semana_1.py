# Semana 1 do Curso de Lógica de Programação
# O que eu aprendi:


print("GIT")
print("Python")

nascimento = int(input("Quando você nasceu? "))
atualidade = int(input("Em que ano que você está?"))

resultado = atualidade - nascimento
print("Você tem",resultado,"anos",sep="\n",end="")
# Aqui o sep sera o final das variaveis
# Nesse caso a variavel é tipo string,então ele separou o final de cada uma em uma linha
# o \n significa enter

# Assim que descobre o tipo de variavel:
# Para descobrir usa a função type acompanhada em () por o nome da variavel
# as variaveis podem ser int,float,booleana,string, undefined ou null (Não existe no python)
# existe no typescript,java

print ("O tipo dessa variavel é",type(resultado))

b = 10.5
print("Essa variavel b é do tipo",type(b))

a= 10
print("Essa variavel a é do tipo",type(a))

c= "Ola"
print("Essa variavel c é do tipo",type(c))

d= False
print("Essa variavel d é do tipo",type(d))

# ATENÇÃO:
# Quando for colocar uma variavel não pode usar virgula,espaço e acentuação
# Numero vai ser considerado como uma string se for colocado entre aspas
# Exemplo:

Valor_1 = "1"
print("O tipo de variavel do valor 1 é",type(Valor_1))
# No teste, irá aparecer que é do tipo string se colocar entre aspas, mas e se fizermos diferente?

Valor_2 = 2
print("O tipo da variavel é o tipo",type(Valor_2))
# Não colocando em aspas vira a a variavel certa que é string

Valor_3 = "3"
Valor_4 ="4"
# E se fizermos uma soma com as variaveis erradas?

Soma = Valor_3 + Valor_4
print("O valor dessa conta é",Soma)
# Se colocarmos com aspas irá virar uma variavel tipo string
# Sendo assim, se juntarmos as duas irão ser postas lado a lado
# como se fosse uma palavra

# Mas se for feito do jeito certo:

Valor_5 = 5
Valor_6 = 6

Soma_1 = Valor_5 + Valor_6
print("O valor correto dessa soma é",Soma_1,type(Soma_1))

#Teoria
# GIT gerencia versôes
# É uma ferramente de gerenciamento de versões
# No ambiente git há o codigo funcional que vai para o desenvolvimento
# que depois volta para o codigo funcional
# Temos as linguagens altamente tipadas e poucamente tipadas
# tipada significa que precisa informar o tipo de variavel
# Python é poucamente typada
# Temos diversas variaveis como int,booleana,float,undefined,string
# Na variavel não pode conter acento,espaço,numeros na frente e simbolos especiais
# Pode usar camel case: olaOla ou snake case: ola_ola
# Ambiente git tem o repositorio local e de origem, codigo,desenvolvimento,staging area
# Temos o push e pull
# git clone,status,add, commit -m, push
# Temos as linguagens interpretadas e compiladas
