# reto 3: para cada un de lo N pacientes a partir de su genero 1: masculino, 2 Femmenino y su nivel de hemglobina actual contabilice 3 lertas  (masculino <12.2 baja femenino <12,6 baja masculino entre 12,2 y 16,6 normal y femenno entre 12,6 hasta 15normal si es mas de eso alta) si el vaor de genero se sale de 1 y 2 debe solicitar nuevamente ambos vares hasta que se valido debe mostrar el promedo para cada genero y cuantos estan por debajo y por encm dse este en ambos generos
N = int(input("ingrese el numero de pacientes:"))
masculino_baja = 0
masculino_normal = 0 
masculino_alta = 0
femenino_baja = 0
femenino_normal = 0
femenino_alta = 0
suma_masculino = 0
suma_femenino = 0
contador_masculino = 0
contador_femenino = 0
for i in range(N):
    genero = int(input("ingrese el genero 1: masculino, 2 femenino: "))
    while genero < 1 or genero > 2:
        print("genero invalido, intente de nuevo")
        genero = int(input("ingrese el genero 1: masculino, 2 femenino: "))
    hemoglobina = float(input("ingrese el nivel de hemoglobina: "))
    if genero == 1:
        suma_masculino += hemoglobina
        contador_masculino += 1
        if hemoglobina < 12.2:
            masculino_baja += 1
        elif 12.2 <= hemoglobina <= 16.6:
            masculino_normal += 1
        else:
            masculino_alta += 1
    else:
        suma_femenino += hemoglobina
        contador_femenino += 1
        if hemoglobina < 12.6:
            femenino_baja += 1
        elif 12.6 <= hemoglobina <= 15:
            femenino_normal += 1
        else:
            femenino_alta += 1
if contador_masculino > 0:
    promedio_masculino = suma_masculino / contador_masculino
    print(f"Promedio de hemoglobina masculino: {promedio_masculino:.2f}")
else:
    print("No se ingresaron datos para pacientes masculinos.")
if contador_femenino > 0:
    promedio_femenino = suma_femenino / contador_femenino
    print(f"Promedio de hemoglobina femenino: {promedio_femenino:.2f}")
else:
    print("No se ingresaron datos para pacientes femeninos.")
print(f"Pacientes masculinos - Baja: {masculino_baja}, Normal: {masculino_normal}, Alta: {masculino_alta}")
print(f"Pacientes femeninos - Baja: {femenino_baja}, Normal: {femenino_normal}, Alta: {femenino_alta}")
             

