nota1 = float(input("Ingrese la nota 1"))
nota2 = float(input("Ingrese la nota 2"))
nota3 = float(input("Ingrese la nota 3"))
nota4 = float(input("Ingrese la nota 4"))
matricula = float(input("Costo de la matricula"))

promedio = (nota1 + nota2 + nota3 + nota4) / 4
print(promedio)

if promedio >=4:
    print(f"Excelente tienes un descuento de {matricula*20/100}")
else:
    print()
