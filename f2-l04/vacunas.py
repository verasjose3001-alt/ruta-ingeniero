escuela = input("Escuela: ").strip().upper()
codigo = input("Código: ")
alumnos = int(input("Alumnos: "))
vacunados = int(input("Vacunados: "))
dosis_en_ml = input("Dosis en ml: ").replace(",",".")
dosis_en_ml = float(dosis_en_ml)
faltan = alumnos - vacunados
avance = (vacunados / alumnos)*100
ml_vacuna_faltan = faltan * dosis_en_ml
print()
print("=== Jornada de vacunación · LD-0417 ===")
print(f"Escuela: {escuela}")
print(f"Vacunados: {vacunados}")
print(f"Faltan: {faltan}")
print(f"Avance: {avance} %")
print(f"Vacuna que falta: {ml_vacuna_faltan} ml")