alerta = "2026-10-12 22:47 PUERTA_PRINCIPAL ACCESO_DENEGADO tarjeta=4410-2210-7788"
hora = alerta[11:16]
evento = alerta[34:49].lower().replace("_"," ")
lugar = alerta[17:33].lower().replace("_"," ")

print(f"[{hora}] {evento} en {lugar} · tarjeta {"****-****-"+alerta[-4:]}")