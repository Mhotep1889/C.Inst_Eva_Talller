llamada = input("Ingrese el destino de la llamada: ")
duracion = float(input("Duración de la llamada en minutos: "))

tarifas = {
    "Estados Unidos": 900,
    "Canadá": 800,
    "Europa": 950,
    "Resto del mundo": 1250
}

costo_sin_descuento = duracion * tarifas.get(llamada, 0)

if duracion > 15:
    descuento = 0.2  
    costo_con_descuento = costo_sin_descuento * (1 - descuento)
else:
    costo_con_descuento = costo_sin_descuento

print(f"El costo total de la llamada a {llamada} es: {costo_con_descuento:.2f} pesos.")
