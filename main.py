import math
# Basta alterar a função do metodo f(x) e g(x) para a função desejada e então rodar o codigo

def f(x):
      return (2*x -math.sin(x)+4) # Precisa ser mudado de acordo com a função
def g(x):
      return (-math.sqrt(math.exp(x))) #Deve ser mudada para a função geratriz usada no metodo iterativo.

def df(x):
      h= 0.0000001
      return(f(x+h)-f(x)/h)

def check(a,b):
      if  f(a)*f(b)<0:
            return 1
      else:
            return 0

while True:
      print("\n\nVISUALIZADOR CALCULO NUMERICO\nLEMBRE-SE DE ALTERAR A FUNÇÃO f(x) E g(x)\n"
            "Escolha uma opção:\n"
            "1.Bisseção\n"
            "2.Newton\n"
            "3.Cordas\n"
            "4.Linear\n"
            "5.Sair")
      x = input("Escolha: ")
      xi = 0
      match x:
            case "1":
                  a = float(input("inicio do intervalo: "))
                  b = float(input("fim do intervalo: "))
                  e = float(0.01)
                  check = check(a, b)
                  if check == 1:
                        i = 0
                        while(math.fabs((b-a)/2) > e or i<3):
                              xi = (a+b)/2
                              if f(xi) == 0:
                                    print("A raiz é:",xi)
                                    print("Erro: ",math.fabs((b-a)/2)-xi)
                                    break
                              else:
                                    if f(a)*f(xi) < 0:
                                          b = xi
                                    else:
                                          a = xi
                              i+=1
                        if(i>=3):
                              print("A raiz é aproximadamente:",xi)
                              print("Erro:",math.fabs((b-a)/2))
                  else:
                        print("Intervalo não contem raiz. ")
                        break

            case "2":
                  TOL = 0.001
                  x0 = float(input("Aproximação inicial: "))
                  i = 1
                  while(math.fabs(f(x0))> TOL or i<3):
                        x =x0 -f(x0)/df(x0)
                        x0 = x
                        i+=1
                  print("Rais =",x0," \n Erro =",math.sqrt(f(x0)**2),"\n")


            case "3":
                  TOL=0.0001
                  xn = 0.0
                  xl = []
                  a = float(input("Inicio do intervalo: "))
                  b = float(input("Fim do intervalo: "))

                  xl.append(a)
                  xl.append(b)

                  i=1
                  n=1
                  while(math.fabs(f(xn))>TOL or i<3):
                        xn =xl[n] - (xl[n]- xl[n-1])/(f(xl[n]) - f(xl[n-1]))*f(xl[n])
                        xl.append(xn)
                        n+=1
                        i+=1
                  print("\nRaiz: ",xn,"\nErro: ",f(xn))
            case "4":
                  x0=float(input("Aproximação inicial: "))
                  x1=0
                  i=0
                  while (i<3):
                        x1 = g(x0)
                        x0 = x1
                        i+=1
                  print("\nRaiz: ", x1)
                  print("\nf(x) =", f(x1))
                  print("\ng(x) =", g(x1))
            case "5":
                  print("Adeus!!")
                  exit(0)


