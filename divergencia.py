import sympy as sp
x, y, z = sp.symbols('x y z')
simbolos = ["x","y","z"]

def calcularDivergencia():
    expresionEvaluar = []
    try:
        for i in range(3):
              cadena = input(f"ingrese la expresion para calcular en la cordenada {simbolos[i]} :\n")
                 # sp.symphi nos permitira convertir una cadena a una expresion compatible:
              expresion = sp.sympify(cadena)
              expresionEvaluar.append(expresion)
    except Exception as e:
        print("hubo un error al momento de ingresar los datos")
        return      
      
    #calculamos la divergencias de la expresiones
    divergencia = 0
    valueDeri = []
    for i in range(3):
        valueDeri.append(sp.diff(expresionEvaluar[i], simbolos[i]))
        divergencia += sp.diff(expresionEvaluar[i], simbolos[i])
    print("__________________________________________________________")         
    print("resultado de las derivadas con repecto a: ",simbolos)
    
    for i in range(3):
        print(f"d/d{simbolos[i]} : ",valueDeri[i])
    print("__________________________________________________________")        
    print("Resultado: ",divergencia)    
             

def seleccionarOpciones():
    print("1: calcular divegencia")
    print("2:ver como usar el programita")
    print("3:salir")
    opcion=int(input())
    return opcion


def verVanual():
    print("Nota el programa solo resulve polinomios")
    print("______________________________________________________")
    print("multiplicar con una variable ponemos *")
    print("Ejemplo: numero a variable:")
    print("2*x\n12*y")
    print("Ejemplo: variable a variable:")
    print("x*y\nx*y*z\nz*x")
    print("______________________________________________________")
    print("Elevar la potencia usamos **")
    print("Ejemplo elevar una variable a un numero")
    print("x**3\ny**4\nz*2")
    print("________________________________________________________")
    print("podemos realizar combinaciones como estas:")
    print("2*x**2/n2x**2+x*Y")
    print("Si escribiera algo mal el programa mandara un mensaje")
    

opcion = 0
while(opcion != 3):
    opcion = seleccionarOpciones()
    match opcion:
        case 1: calcularDivergencia()
        case 2:verVanual()
        case 3:print("haste luego")
        case _:print("opcion no encontrada")