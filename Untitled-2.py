
hombres_baja = hombres_alta = hombres_normal = 0
mujeres_baja = mujeres_alta = mujeres_normal = 0


n = int(input("Ingrese el número de pacientes: "))

for i in range(n):
    h = float(input(f"\nPaciente {i+1} - Nivel de hemoglobina (g/dL): "))
    g = int(input("Género (1: Masculino, 2: Femenino): "))

   
    while g not in [1, 2]:
        g = int(input("Género inválido. Ingrese 1 (Masculino) o 2 (Femenino): "))

    if g == 1: 
        if h < 12.2:
            hombres_baja += 1
        elif h <= 16.6:
            hombres_normal += 1
        else:
            hombres_alta += 1
    else:       
        if h < 12.6:
            mujeres_baja += 1
        elif h <= 15:
            mujeres_normal += 1
        else:
            mujeres_alta += 1


print("\n--- Resultados ---")
print(hombres_baja, hombres_alta, hombres_normal, mujeres_baja, mujeres_alta, mujeres_normal)
