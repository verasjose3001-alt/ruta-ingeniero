donantes_txt = "37"
meta_txt = "50"
litros_txt = "0.45"

donante_faltante = int(meta_txt)- int(donantes_txt) 
avance = int(meta_txt) / int(donante_faltante) * 100
litros_faltante = donante_faltante * float(litros_txt)

print("Faltan:",donante_faltante)
print("Avance:",avance)
print("Litros faltante:",litros_faltante)
