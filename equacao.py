from math import sqrt
print("Cálculo da equação do 2o grau")
print("a.x^2+b.x+c=0")
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
if a==0 and b!=0 and c!=0:
    print("Equação do primeiro grau")
    print("{0}.x+{1}=0".format(b,c))
    x=-c/b
    print("O valor de x é: {0:.16f}".format(x))
    if b>0:
        print("A reta é crescente! / ")
    else:
        print("A reta é decrescente! \ ")
elif a!=0 and b!=0 and c==0:
    print("Equação do segundo grau incompleta")
    d = (b**2)-(4*a*c)
    if d<0:
        print("Não há raízes reais.")
    elif d>0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print("As raízes são: {0:.16f} e {1:.16f}".format(x1,x2))
    if a>0 and d>0:
        print("Concavidade para cima.")
    elif a<0 and d>0:
        print("Concavidade para baixo.")
elif a!=0 and b!=0 and c!=0:
    print("Equação do segundo grau")
    d = (b**2)-(4*a*c)
    if d<0:
        print("Não há raízes reais.")
    elif d>0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print("As raízes são: {0:.16f} e {1:.16f}".format(x1,x2))
    if a>0 and d>0:
        print("Concavidade para cima.")
    elif a<0 and d>0:
        print("Concavidade para baixo.")
elif a==0 and b==0 and c!=0:
    print("Não é uma equação.")



