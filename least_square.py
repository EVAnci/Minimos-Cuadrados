from numpy import log as ln
import numpy as np

def input_data(parameter,example):
    flag=True
    while flag:
        flag=False
        value=input(f"    Ingrese los valores de {parameter} medidos, separados por coma sin espacios (ejemplo -> {example}): ")
        value=value.split(",")
        print(f"    Valores (verificar que no hayan espacios ni letras) -> {value}")
        valid=input("    ¿Estos valores son correctos? [Y/n]: ")
        if valid.lower() == "n":
            flag=True
        else:
            try:
                for i in range(len(value)):
                    value[i]=float(value[i])
            except:
                flag=True
                print("    Hay alguna letra o espacio en algún número. Intentelo de nuevo.")
    return value

def scalar_prod(f,g):
    result=0
    for i in range(len(f)):
        result+=f[i]*g[i]
    return result

print("---------------------------------------------------------------------------------------------------------------------------------------------")

print(" Aproximación de la intensidad de corriente en un circuito RC (resistor-capacitor) en serie durante el proceso de descarga de un capacitor.")
print("---------------------------------------------------------------------------------------------------------------------------------------------\n")

print("Nota: Al usar este tipo de aproximación, no es necesario conocer los valores de i_0 y RC (constante de tiempo τ) ya que estos valores se aproximarán con mínimos cuadrados y al final se proporcionarán los resultados.\n")

print("A continuación se solicitaran los valores medidos. Se proporciona la siguiente tabla de ejemplo para guiarlo durante la solicitud de datos:")
print("┌──────┬─────┬─────┬─────┬─────┬─────┐")
print("│t(seg)│  1  │  2  │  3  │  4  │  5  │")
print("├──────┼─────┼─────┼─────┼─────┼─────┤")
print("│ i(t) │8.187│6.703│5.488│4.493│3.679│")
print("├──────┼─────┼─────┼─────┼─────┼─────┤")
print("│ w(t) │  1  │  1  │  1  │  1  │  1  │")
print("└──────┴─────┴─────┴─────┴─────┴─────┘\n")

print("En caso de equivocarse, se le preguntarán si los valores son correctos.")
flag=True
while flag:
    flag=False
    time=input_data("tiempo en segundos", "1,2,3,4,5")
    i=input_data("intensidad en Amperes", "8.187,6.703,5.488,4.493,3.679")
    w=input_data("peso (w(t))", "1,1,1,1,1")
    if len(time) != len(i) or len(time) != len(w):
        flag=True
        print("[!] La cantidad de datos medidos de cada parámetro debe ser la misma")

f = [ln(x) for x in i]
# luego de despejar f(t)=ln(t(t))=ln(i_0)-\frac{t}{RC}
f1=w
f2=time
# Entonces se puede expresar como f(t)=µf1+ßf2 donde µ=ln(i_0) y ß=-\frac{t}{RC}

# Armamos el SEL

f1f1=scalar_prod(f1,f1)
f1f2=scalar_prod(f1,f2)
f2f2=scalar_prod(f2,f2)
ff1=scalar_prod(f,f1)
ff2=scalar_prod(f,f2)

# Matriz de coeficientes

A = np.array([
    [f1f1,f1f2],
    [f1f2,f2f2]
])

# Matriz B

B = np.array([ff1,ff2])

solution = np.linalg.solve(A,B)

# Con la solución operamos para obtener i_0 y RC

i_0 = np.exp(solution[0])
RC = -1/solution[1]

# Imprimimos la solución en pantalla

print(f"Resultados:\n    i_0=e^{solution[0]}={i_0}\n    RC={RC}")