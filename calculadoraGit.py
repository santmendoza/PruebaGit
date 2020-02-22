import sys
#Santiago Mendoza V.1
x=0
while x!=1: 
    try: 
        a= float(input('Indica el Valor del Primer Numero: '))
        b=float (input('Indica el valor del Segundo Numero: '))
    except:
        print('Lo que haces no es valido amiguito')
        sys.exit()
       

    print('Selecciona la operacion que quieras realizar: ')
    print('#########################')
    print('###** 1.Sumar       **###')
    print('###** 2.Restar      **###')
    print('###** 3.Multiplicar **###')
    print('###** 4.Dividir     **###')
    print('###** 5.Salir       **###')
    print('#########################')

    n= int(input('Elige una opción: '))

    if n==1: 
        resultado= a+b

    if n==2:
        resultado= a-b
    if n==3:
        resultado= a*b
    if n==4 and b!=0:
        resultado= a/b

    if n==5 or b==0:
        print("Gracias por usar la calculadora")
        x=1
    
    if n>0 and n<5 and b!=0:
     print(resultado)
        
            



  
       

