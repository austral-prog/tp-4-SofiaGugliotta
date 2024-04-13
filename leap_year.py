def leap_year():
    
    A= int(input("Ingrese un año: "))

    if((A % 100 != 0) and(A % 4 == 0)) or ((A % 100 == 0)and(A % 400 == 0))
        print(f"El año {A} es bisiesto")
    else: print(f"El año {A} no es bisiesto")
