Usuario = "admin"
Contraseña = "1234"

while  True:
    Usuario_Ingresado = input("\n""Ingrese su usuario: ")
    Contraseña_Ingresada = input("Ingrese su contraseña: ")
    
    if Usuario_Ingresado == Usuario and Contraseña_Ingresada == Contraseña:
        print("\n""¡Acceso concedido! Bienvenido al sistema de acceso.""\n")
        break
    else:
        print("\n""¡Acceso denegado! Usuario o contraseña incorrectos. Intente nuevamente.""\n")