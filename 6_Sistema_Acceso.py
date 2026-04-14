# Datos de acceso
usuario_valido = "admin"
password_valida = "1234"

intentos_fallidos = 0
limite_bloqueo = 3

while intentos_fallidos < limite_bloqueo:
    print(f"\n--- Intento de seguridad: {intentos_fallidos}/{limite_bloqueo} ---")
    user_input = input("Ingrese usuario: ")

    if user_input == usuario_valido:
        # El usuario es correcto, procedemos a pedir la contraseña
        pass_input = input("Ingrese contraseña: ")

        if pass_input == password_valida:
            print("¡Acceso concedido!")
            break  # Sale del bucle completamente
        else:
            # Aquí es donde ocurre el conteo para el bloqueo
            intentos_fallidos += 1
            print(f"Contraseña incorrecta para el usuario '{usuario_valido}'.")
    else:
        # El usuario es incorrecto: no se cuenta para el bloqueo
        print("Usuario inválido, intente nuevamente.")

# Verificamos si salió por bloqueo o por éxito
if intentos_fallidos == limite_bloqueo:
    print("\n[ALERTA] Sistema bloqueado por 3 fallos de contraseña.")
    print("Por favor, contacte al administrador para restablecer el acceso.")