Nombre= input("Ingrese su nombre: ")
Cargo= input("Ingrese su cargo: ")
Salario= float(input("Ingrese su salario: "))


print("\n" + "="*30 + " CERTIFICACIÓN LABORAL " + "="*30 + "\n")
print(f"LA EMPRESA EJEMPLO S.A.S.\nNIT: 900.000.000-0\n")
print("CERTIFICA QUE:\n")
print(f"El(la) señor(a) {Nombre.upper()}, identificado(a) con documento de identidad,")
print(f"labora en nuestra organización desempeñando el cargo de {Cargo.upper()},")
print(f"con un salario mensual de ${Salario:,.0f}.\n")
print("se expide en la fecha actual.\n")
print("Atentamente,\n\nTalento Humano")
print("\n" + "="*80)