llamada = input("Ingrese el destino de la llamada")
duracion = float(input("Duracion de la llamada en minutos"))

if llamada == "Estados Unidos" and duracion > 15:
    print(duracion * 820)
else:
    print(duracion * 900)

if llamada == "Canada" and duracion > 15:
    print(duracion * 740)
else:
    print(duracion * 800)

if llamada == "Europa" and duracion > 15:
    print(duracion * 931)
else:
    print(duracion * 950)

if llamada == "Resto del mundo" and duracion > 15:
    print(duracion * 1150)
else:
    print(duracion * 1250)
