camara = input("Cámara: ").strip().upper()
bateria = int(input("Batería %: "))
estado = input("Estado: ").strip().lower()
temperatura = input("Temperatura: ").replace(",",".")
temperatura = float(temperatura)

if estado != "online":
    color = "ROJO: sin conexión"
elif bateria <= 10 or temperatura >= 70:
    color = "ROJO: atender hoy"
elif bateria <= 30 or temperatura >= 60:
    color = "AMARILLO: revisar esta semana"
else:
    color = "VERDE: todo bien"

print()
print(f"=== Revisión {camara} ===")
print(f"Batería: {bateria}%")
print(f"Temperatura: {temperatura} °C")
print(f"Color: {color}")