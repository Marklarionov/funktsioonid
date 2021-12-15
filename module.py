from math import *
#def kolmnurga_pindala(külg:float,kõrgus:float):
#    """Leiab kolmnurga_pindalat. On antud kõrgus ja külje pikkus. Tabastab S float formaadis.
#    ["+","-","*","/"]
#    :param float külg: Kolmnurga külje pikkus
#    :param float kõrgus: Kõrgus vastav küljele
#    :rtype: var
#    """
#    if külg<0 or kõrgus<0:
#        S="Valed andemd!"
#    else:
#        S=0.5*külg*kõrgus

#    return S

#--1--

#def arithmetic(a:float,b:float,c:str):
#   """Täidab liitmine,lahutamine, korrutamine ja jagamine.
#   ["+","-","*","/"]
#   :param float a: esimene arv
#   :param float b: teine arv
#   :param str c: aritmeetilise tehe
#   """
#   if c=="-":
#       vastus=a-b
#   elif c=="+":
#       vastus=a+b
#   elif c=="/" and b==0:
#       vastus="Div/0"
#   elif c=="/":
#       vastus=a/b
#   elif c=="*":
#       vastus=a*b

#--2--

def is_year_leap(year:int):
    """Sisestame aasta number ja tagastame True,kui aasta on liigaasta ja False
    """
    if year%4: