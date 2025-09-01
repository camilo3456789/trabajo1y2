
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g/dL): "))
genero = int(input("Ingrese el género (1: Masculino, 2: Femenino): "))


if genero == 1:  
    if hemoglobina < 12.2:
        print("Baja")
    elif 12.2 <= hemoglobina <= 16.6:
        print("Normal")
    else:
        print("Alta")
elif genero == 2: 
    if hemoglobina < 12.6:
        print("Baja")
    elif 12.6 <= hemoglobina <= 15:
        print("Normal")
    else:
        print("Alta")
else:
    print("No es posible generar la alerta")
