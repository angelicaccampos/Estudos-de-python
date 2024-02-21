#   LISTA 1 - APC    #
#Questão 1 
c = input ('')
print (c)
print (2*c)
print (c, c)
print ('2'+str(c))
print ('['+str(c)+']')
#Question author's solution 
c = input()
print(c)
print(2*c)
print('%c %c' % (c, c))
print('2%c'% c)
print('[%c]' % c)

#Questão 2 
X = input ('')
Y = input ('')
Z = input ('')
print (X+Y+Z)
print (X)
print (Y+Y)
print (Z, Z, Z)
print ('X ==', str(X)+',', 'Y ==', str(Y)+',', 'Z ==', str(Z))
print ( 'X !=', str(Y)+',', 'Y !=', str(X)+',', 'Z ==', str(Z))
#Question author's solution
a = input()
b = input()
c = input()
print(a+b+c)
print(a)
print('%c%c' % (b, b))
print('%c %c %c' % (c, c, c))
print('X == %c, Y == %c, Z == %c' % (a, b, c))
print('X != %c, Y != %c, Z == %c\n' % (b, a, c))

#Questão 4
num = input ()
X = int(num[0])
Y = int(num[2])
print (float(pow(X,Y)))
#Question author's solution
import math
x, y = input().split()
x = int(x)
y = int(y)
pot = math.pow(x, y)
print(pot)

#Questão 5
from math import pow
def powAPC (X, Y):   
    print (f'{pow(X,Y)}')
#Question author's solution
import math
def powAPC(x, y):
    print(math.pow(x, y)) 
    
#Questão 6
def converte (C):
    print(round((C-32)*(5/9),1))
#Question author's solution
def converte(valor):
    res = ((valor - 32.0) * 5.0) / 9.0
    print(f'{res:.1f}')

#Questão 8
a,b,c = (input().split(" "))
a,b,c = float(a), float(b), float(c)
Du, Dudu, Edu = ((a) * 1.10), ((b) * 1.10), ((c) * 1.10)
s = (Du+ Dudu+ Edu)
print ("{:.2f}".format(Du), "{:.2f}".format(Dudu),"{:.2f}".format(Edu))
print("{:.2f}".format(s))
#Question author's solution
du, dudu, edu = input().split()
du = float(du)
dudu = float(dudu)
edu = float(edu)
soma = du + dudu + edu

#Questão 10
DD,MM,AA = input().split("/")
print (DD+'-'+MM +'-'+AA)
print (MM+'-'+DD +'-'+AA)
print (AA+'/'+MM +'/'+DD)
#Question author's solution
d, m, a = input().split('/')
print('%s-%s-%s' % (d, m, a))
print('%s-%s-%s' % (m, d, a))

#Questão 11
def maiorAB(a, b):
    if int(a) > int(b):
        print (a)
    else:
        print (b)
a, b = input().split(' ')
maiorAB(a, b)
#Question author's solution
def maiorAB(a, b):
    soma = a + b + abs(a-b)
    soma = soma // 2
    print(soma)
for i in range(5):
    a, b = [int(x) for x in input().split()]
    maiorAB(a, b)
    
#Questão 12
def trocarAB(a, b):
    print(b,a)
a, b = input().split(' ')
trocarAB(a, b)
#Question author's solution
def trocarAB(a, b):
    print(b, a)
for i in range(5):
    a, b = [int(x) for x in input().split()]
    trocarAB(a, b)
    
#Questão 14
def age(dias):
    dias >= 1 and dias <=1000001
    A = int(dias // 360)
    M = int((dias %360)// 30)
    D = int((dias %360)% 30)
    print(f'{A} {M} {D}')
d1,d2,d3  = input().split(" ")
d1,d2,d3  = int(d1), int(d2), int(d3)
age(d1)
age(d2)
age(d3)
#Question author's solution
def age(days):
    year = days // 360
    days = days % 360
    month = days // 30
    days = days % 30
    print(year, month, days)
a, b, c = [int(x) for x in input().split()]
age(a)
age(b)
age(c)

#Questão 17
def binario(a): 
    n = bin(a)
    print("0b"+n[2:] ) 
a = int(input())
binario(a)
#Question author's solution
def binario(a):
    print(bin(a))
a = int(input())
binario(a)

#Questão 30
""" Este programa lê um número inteiro e escreve uma mensagem apresentando este número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
x = input()
print(f'X = {x}')

#Questão 31
""" Este programa lê um número em ponto flutuante e escreve uma mensagem apresentando este número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
i = float(input())
print("X = %f" % (i))

#Questão 32
""" Este programa lê uma cadeia de caracteres e escreve uma mensagem apresentando este número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
i = str(input())
print("X = %s" % (i))

#Questão 33
""" Este programa lê um número e escreve uma mensagem apresentando este número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
i = int(input())
print("X = %d" % (i)) # <-- Mude Y para X */

#Questão 34
""" Este programa lê um número em ponto flutuante e escreve uma mensagem apresentando este número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
i = float(input())
print("X = %f" % (i)) # <-- Mude Y para X */

#Questão 35
""" Este programa lê uma cadeia de caracteres e escreve uma mensagem apresentando este número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
i = str(input())
print("X = %s" % (i)) # <-- Mude Y para X */

#Questão 36
""" Este programa lê um número e escreve uma mensagem apresentando o dobro desse número 
   em um formato específico:  "X = ?" (onde ? é o valor fornecido). """
i = int(input())
print("X = %d" % (i+i))

#Questão 38
def ritmoMedio(a, b, c, d):
    horasEmSegundos = a*3600
    minutosEmSegundos = b*60
    segundosTotais = horasEmSegundos + minutosEmSegundos + c
    segundosPorKm = segundosTotais /d
    minutos = segundosPorKm // 60
    segundos = segundosPorKm % 60
    minutos, segundos = [int(i) for i in [minutos, segundos]]
    if minutos < 10:
        minutos = f'0{minutos}'
    if segundos < 10:
        segundos = f'0{segundos}'
    print(f'{minutos}:{segundos} min/km')
#Question author's solution
def ritmoMedio(h,m,s,d):
    totalminutos = h*60 + m + s/60
    media = float(totalminutos)/float(d)
    minutos = int(media)
    restante = media-float(minutos)
    segundos = int(restante*60)
    print('{:02d}'.format(minutos)+":"+'{:02d}'.format(segundos)+" min/km")

#Questão 46
def vestimentas(x,y):
    numerosPares = 0 
    if x > y:
        numerosPares = x - (x-y)
    else: 
        numerosPares = y - (y-x)
    print(numerosPares *2)
#Question author's solution
def vestimentas(x,y):
    print(2*min(x,y))