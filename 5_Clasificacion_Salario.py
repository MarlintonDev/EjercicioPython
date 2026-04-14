Salario = float(input("Ingrese su salario: $ "))

if Salario > 8000000:
    print("El salario ingresado esta categorizado como ALTO")
elif Salario >= 2500000 and Salario <= 8000000:
    print("El salario ingresado esta categorizado como MEDIO")
else:
    print("El salario ingresado esta categorizado como BAJO")