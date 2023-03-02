# A ideia desse código é apresentar uma aplicação simples do método de Runge-Kutta


import numpy as np
import matplotlib.pyplot as plt

# A EDO
def f(x,y):
  return x-3*y

# Definir condição inicial com ponto conhecido
x0 = 0
y0 = 1

# Vetores que irão acumular os pontos
xi = [x0]
yi = [y0]

a = 0
b = 2
n = 10
h = (b-a)/n

# iteração
for i in range(n):
  k1 = f(x0,y0)
  k2 = f(x0+h/2, y0+h/2*k1)
  k3 = f(x0+h/2, y0+h/2*k2)
  k4 = f(x0+h, y0+h*k3)
  yk = y0 + h/6*(k1 + 2*k2 +2*k3 + k4)
 
  x0 = x0 + h
  y0 = yk

  print(f"({round(x0,2)},{round(y0,2)})")

  xi.append(round(x0,2))
  yi.append(round(yk,2))

print()
print(xi)
print(yi)

plt.plot(xi,yi,'o')
plt.show()