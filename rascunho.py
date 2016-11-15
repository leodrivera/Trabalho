#!/usr/bin/env python
# encoding: utf-8

"""
Rotina para cadastrar usuário

def registrar _arquivo(user)
f=open('arquivo.txt','w')
f.write(user.nome, ','  ,user.telefone,...)

Rotina para checar nome:
Se já cadastrado flag=1
Return flag

Rotina para carregar usuários:
f=open('arquivo.txt)
fazer loop em todas as linhas
Armazenar as variáveis de cada linha lista dados
dados[0] = usuário(dados[1],dados[2],...)

Código:
Recebe mensagem 'Adiciona_usuario' ou 'Faz_login' na lista a

If a[0] == 'Adiciona_usuario':
while 1: #Se a pessoa colocar nome repetido
  flag = checar_nome(a[1])
  If flag == 1:
    Envia para o cliente: 'not_ok'
  else:
  nome = usuario( a[0],a[1],...) # crio objeto da classe usuário
  registrar_arquivo(nome)

Elif: a[0] == 'Faz_login':
carregar_usuarios()
while 1: #Se a pessoa errar nome ou senha
If 'a[1].nome = a[1]' and 'a[1].senha=a[2]':
  Registrar ip e porta do usuário
  a[1].socket= 'IP do usuário:Porta'
else:
  Envia para o cliente 'not_ok'  # Recupera variáveis

try:
  f1 = open("clientes.txt")
  texto = f1.readlines()

except IOError:
  pass
"""

class MyClass(object):
    def __init__(self, number):
        self.number = number

my_objects = []

for i in range(3):
    my_objects.append(MyClass(i))

# later

for obj in my_objects:
    print obj.number


#for obj in my_objects:
#    print obj.number

class testa_entrada:
    valor = 0
    l = 0
    num = 0
    max = 100

    while 1:
        try:
            if (num == 'numero'): #Se for para checar se o valor inserido é um número
                valor = float(valor) #Transforma string em float. Se o valor for inteiro ou float, ele continua. Se
                if max == 100:
                    break                    # for string, ele abre exceção
            if len(valor) > max: #Se o valor digitado for maior que o tamanho máximo ele executa uma exceção
                raise
            else:
                break
            if len(valor) <= l: #Se o valor digitado for menor que o tamanho mínimo ele executa uma exceção
                raise
            else:
                break	#Quebra o loop
        except Exception, err:
            valor=raw_input('Valor inválido, digite novamente\n')	#Exceção pelo valor abaixo do mínimo determinado
    return valor #retorna valor válido