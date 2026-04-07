
# UTN - TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN
#TP integrador – Repetitivas- Condicionales y Secuenciales.

#Alumno: Troncoso Leonardo Gabriel

#__________________________________________________________________________________
#Ejercicio 1: “Caja del Kiosco” 
#__________________________________________________________________________________

nombre = input("Por favor, ingrese su nombre: ")
while not nombre.isalpha() or nombre == "":
    print("Error: El nombre solo debe contener letras. Por favor, intente nuevamente.")
    nombre = input("Por favor, ingrese su nombre: ")
cantidad_productos = input("Por favor, ingrese la cantidad de productos a comprar: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Error: La cantidad de productos debe ser un número entero positivo. Por favor, intente nuevamente.")
    cantidad_productos = input("Por favor, ingrese la cantidad de productos a comprar nuevamente: ")
cantidad_productos = int(cantidad_productos)
total_sin_descuentos = 0 
total_con_descuentos = 0   
for i in range(1, cantidad_productos + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        print("Error: El precio debe ser un número entero. Por favor, intente nuevamente.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)
    descuento = input(f"Producto {i} - Descuento (S/N): ").lower().strip()
    while descuento not in "s" and descuento not in "n":
        print("Error: Debe ingresar 'S' para sí o 'N' para no. Por favor, intente nuevamente.")
        descuento = input(f"Producto {i} - Descuento (S/N): ").lower().strip()
    total_sin_descuentos += precio
    if descuento == "s":
        total_con_descuentos += precio * 0.9
    else:
        total_con_descuentos += precio

ahorro_total = total_sin_descuentos - total_con_descuentos
promedio_por_producto = total_con_descuentos / cantidad_productos
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")

#__________________________________________________________________________________
#Ejercicio 2:  “Acceso al Campus y Menú Seguro” 
#__________________________________________________________________________________

i=0
usuario = ""
clave = ""
print(f"Intento {i+1}/3:")
usuario = input("Ingrese Usuario: ")
clave = input("Ingrese su Clave: ")
while (usuario != "alumno" or clave != "python123") and (i<3):
     if i==2:
        print("Cuenta bloqueada")
        exit()
     i+=1
     print("Error: credenciales inválidas. ")
     print(f"Intento {i+1}/3: ")
     usuario = input("Ingrese Usuario: ")
     clave = input("Ingrese su Clave: ")
print("Acceso concedido.")
menu = ""
while menu != "4":
    print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    menu = input("Opción: ")
    if not menu.isdigit():
        print("Error: ingrese un número válido.")
    elif int(menu) < 1 or int(menu) > 4:
        print("Error: opción fuera de rango.")
    elif menu == "1":
        print("Inscripto")
    elif menu == "2":
        nueva_clave = input("Nueva clave: ")
        if len(nueva_clave) < 6:
            print("Error: mínimo 6 caracteres.")
        else:
            confirmacion = input("Confirme la nueva clave: ")
            if nueva_clave != confirmacion:
                print("Error: las claves no coinciden.")
            else:
                clave = nueva_clave
                print("Clave cambiada exitosamente.")
    elif menu == "3":
        print("¡Vas por buen camino, sigue así!")
print("Saliendo del sistema")

#__________________________________________________________________________________
#Ejercicio 3:  “Agenda de Turnos con Nombres (sin listas)”
#__________________________________________________________________________________

# Inicializo variables para almacenar los turnos y el nombre del operador
opcion = ""
Lunes1 = Lunes2 = Lunes3 = Lunes4 = ""
Martes1 = Martes2 = Martes3 = ""
turnos_ocupados_lunes = 0
turnos_ocupados_martes = 0

# Solicito el nombre del operador y valido que solo contenga letras
nombre_operador = input("Ingrese el nombre del operador: ").strip().lower()
while not nombre_operador.isalpha():
    print("Error: El nombre del operador solo debe contener letras. Por favor, intente nuevamente.")
    nombre_operador = input("Ingrese el nombre del operador: ").strip().lower()
# Menú principal del sistema    
while opcion != "5":
    print("1) Reservar turno \n2) Cancelar turno \n3) Ver agenda del día \n4) Ver resumen general  \n5) Cerrar sistema")
    opcion = input("Opción: ")
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
    elif int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción fuera de rango.")
# Validación de cada opción del menú        
    elif opcion == "1":
        print("Reservar turno.")
        print("1) Lunes \n2) Martes")
        dia= input("Seleccione el día: ")
# Validación para asegurarse de que el usuario ingrese un número
        if not dia.isdigit():    
            print("Error: ingrese un número válido.")
        elif int(dia) < 1 or int(dia) > 2:
            print("Error: opción fuera de rango.")
# Validación del nombre del paciente y reserva de turno            
        else:
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
            if not nombre_paciente.isalpha():
                print("Error: El nombre del paciente solo debe contener letras. Por favor, intente nuevamente.")
# Validación para evitar que un paciente tenga más de un turno reservado y para asignar el turno al paciente si hay disponibilidad en Lunes                
            else:
                if dia == "1":
                    if nombre_paciente == Lunes1 or nombre_paciente == Lunes2 or nombre_paciente == Lunes3 or nombre_paciente == Lunes4:
                        print("Error: El paciente ya tiene un turno reservado el lunes.")
                    elif Lunes1 == "":
                        Lunes1 = nombre_paciente
                        print("Turno reservado para el lunes en el turno 1.")
                    elif Lunes2 == "":
                        Lunes2 = nombre_paciente
                        print("Turno reservado para el lunes en el turno 2.")
                    elif Lunes3 == "":
                        Lunes3 = nombre_paciente
                        print("Turno reservado para el lunes en el turno 3.")
                    elif Lunes4 == "":
                        Lunes4 = nombre_paciente
                        print("Turno reservado para el lunes en el turno 4.")
                    else:
                        print("Error: No hay turnos disponibles para el lunes.")
# Validación para evitar que un paciente tenga más de un turno reservado y para asignar el turno al paciente si hay disponibilidad en Martes                        
                elif dia == "2":
                    if nombre_paciente == Martes1 or nombre_paciente == Martes2 or nombre_paciente == Martes3:
                        print("Error: El paciente ya tiene un turno reservado el martes.")
                    elif Martes1 == "":
                        Martes1 = nombre_paciente
                        print("Turno reservado para el martes en el turno 1.")
                    elif Martes2 == "":
                        Martes2 = nombre_paciente
                        print("Turno reservado para el martes en el turno 2.")
                    elif Martes3 == "":
                        Martes3 = nombre_paciente
                        print("Turno reservado para el martes en el turno 3.")
                    else:
                        print("Error: No hay turnos disponibles para el martes.")
# Validación del nombre del paciente para cancelar el turno y cancelación del turno si el paciente se encuentra en la agenda
    elif opcion == "2":
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        if not nombre_paciente.isalpha():
            print("Error: El nombre del paciente solo debe contener letras. Por favor, intente nuevamente.")
# Validación para asegurarse de que el paciente tenga un turno reservado Lunes o Martes,antes de intentar cancelarlo            
        else:
            if nombre_paciente == Lunes1:
                Lunes1 = ""
                print("Turno cancelado para el lunes en el turno 1.")
            elif nombre_paciente == Lunes2:
                Lunes2 = ""
                print("Turno cancelado para el lunes en el turno 2.")
            elif nombre_paciente == Lunes3:
                Lunes3 = ""
                print("Turno cancelado para el lunes en el turno 3.")
            elif nombre_paciente == Lunes4:
                Lunes4 = ""
                print("Turno cancelado para el lunes en el turno 4.")
            elif nombre_paciente == Martes1:
                Martes1 = ""
                print("Turno cancelado para el martes en el turno 1.")
            elif nombre_paciente == Martes2:
                Martes2 = ""
                print("Turno cancelado para el martes en el turno 2.")
            elif nombre_paciente == Martes3:
                Martes3 = ""
                print("Turno cancelado para el martes en el turno 3.")
            else:
                print("Error: Paciente no encontrado.")
# Visualización de la agenda del día, mostrando los turnos ocupados y disponibles para cada día, 
# y mostrando un mensaje indicando qué día tiene más turnos ocupados o si ambos días tienen la misma cantidad de turnos ocupados.
    elif opcion == "3":
        print("Agenda del día:")
        print("\nLunes:")
        if Lunes1 == "":
            print("Turno 1: (libre)")
        else:
            print(f"Turno 1: {Lunes1}")
        if Lunes2 == "":
            print("Turno 2: (libre)")
        else:
            print(f"Turno 2: {Lunes2}")
        if Lunes3 == "":
            print("Turno 3: (libre)")
        else:
            print(f"Turno 3: {Lunes3}")    
        if Lunes4 == "":
            print("Turno 4: (libre)")
        else:
            print(f"Turno 4: {Lunes4}")
        print("\nMartes:")
        if Martes1 == "":
            print("Turno 1: (libre)")
        else:
            print(f"Turno 1: {Martes1}")
        if Martes2 == "":
            print("Turno 2: (libre)")
        else:
            print(f"Turno 2: {Martes2}")
        if Martes3 == "":
            print("Turno 3: (libre)")
        else:
            print(f"Turno 3: {Martes3}")  
# Cálculo de turnos ocupados y disponibles para cada día, y comparación para determinar qué día tiene más turnos ocupados 
# o si ambos días tienen la misma cantidad de turnos ocupados.                
    elif opcion == "4":
        turnos_ocupados_lunes = 0
        turnos_ocupados_martes = 0
        if Lunes1 != "":
            turnos_ocupados_lunes += 1
        if Lunes2 != "":
            turnos_ocupados_lunes += 1
        if Lunes3 != "":
            turnos_ocupados_lunes += 1
        if Lunes4 != "":
            turnos_ocupados_lunes += 1
        if Martes1 != "":
            turnos_ocupados_martes += 1
        if Martes2 != "":
            turnos_ocupados_martes += 1
        if Martes3 != "":
            turnos_ocupados_martes += 1
        print(f"Turnos ocupados el lunes: {turnos_ocupados_lunes}")
        print(f"Turnos disponibles el lunes: {4 - turnos_ocupados_lunes}")
        print(f"Turnos ocupados el martes: {turnos_ocupados_martes}")
        print(f"Turnos disponibles el martes: {3 - turnos_ocupados_martes}")
        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print("El día con más turnos ocupados es el lunes.")
        elif turnos_ocupados_martes > turnos_ocupados_lunes:
            print("El día con más turnos ocupados es el martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")
# Opción para cerrar el sistema            
print("Cerrando sistema...")

#__________________________________________________________________________________
#Ejercicio 4: “Escape Room: La Bóveda” 
#__________________________________________________________________________________

# Variables iniciales
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
alarma_activada = ""
forzar_cerradura = 0

nombre_agente = input("Ingrese su nombre de agente: ")
# Validación del nombre del agente
while not nombre_agente.isalpha():
    print("Nombre inválido. Por favor, ingrese un nombre válido.")
    nombre_agente = input("Ingrese su nombre de agente: ")
# condiciones para permanecer en el juego 
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    if alarma:
        alarma_activada = "Activada"
    else:
        alarma_activada = "Desactivada"
# Menu de opciones y estado actual del juego        
    print(f"\n{nombre_agente} \nSu estado actual: Energía: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}, Alarma: {alarma_activada}")
    print("\nMenú de acciones:")
    print("\n1. Forzar cerradura ")
    print("2. Hackear panel.")
    print("3. Descansar ")
    opcion = input("Ingrese la opción que desee: ")
# Validación de la opción ingresada
    while not opcion.isdigit() or int(opcion) == 0 or int(opcion) > 3:
        print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
        opcion = input("Ingrese la opción que desee: ")
# opcioón 1: Forzar cerradura (costo: -20 energía, -2 tiempo)
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzar_cerradura += 1
        
        if forzar_cerradura == 3:
            alarma = True
            print("¡Alarma activada! La cerradura se trabó.")           
        elif energia < 40:
            riesgo_alarma = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")
            while not riesgo_alarma.isdigit() or int(riesgo_alarma) == 0 or int(riesgo_alarma) > 3:
                print("Número inválido. Por favor, ingrese un número del 1 al 3.")
                riesgo_alarma = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")
            if riesgo_alarma == "3":
                alarma = True
                print("¡Alarma activada! La cerradura se trabó.")
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada con éxito.")
        else:
            cerraduras_abiertas += 1
            print("Cerradura forzada con éxito.")  
# opción 2: Hackear panel  (costo: -10 energía, -3 tiempo)
    elif opcion == "2":
        forzar_cerradura = 0
        energia -= 10
        tiempo -= 3
        for paso in range(1, 5):
            print(f"Hackeando... Paso {paso}/4")
            codigo_parcial += "A"
        if len(codigo_parcial) >= 8: #and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta automáticamente por hackeo.")
        else:
            print("Hackeo incompleto. No se abrió la cerradura.")
# opción 3: Descansar  (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)          
    elif opcion == "3":
        forzar_cerradura = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma está activada. Energía extra perdida.")
        else:
            print("Descansaste y recuperaste energía.")
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡Sistema bloqueado por alarma! Has perdido.")
        break
# Condiociones de victoria o derrota
if cerraduras_abiertas == 3:
    print("¡Victoria! Has abierto la bóveda y ganado el juego.")
elif energia <= 0 or tiempo <= 0:
    print("¡Derrota! Te has quedado sin energía o tiempo.")

#__________________________________________________________________________________
#Ejercicio 5:  “Escape Room:"La Arena del Gladiador" 
#__________________________________________________________________________________

# Inicialización de variables y validación del nombre del gladiador
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

juego_activo = True
print (f"¡BIENVENIDO A LA ARENA, {nombre}! Prepárate para la batalla.")
print("=== INICIO DEL COMBATE ===")
# Ciclo de combate mientras ambos tengan vida
while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"{nombre} (Vida: {vida_gladiador}) vs Enemigo (Vida: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        opcion = input("Ingrese una opción: ")
        while not opcion.isdigit() or int(opcion) <= 0 or int(opcion) > 3:
            print("Error: Por favor, ingrese un número válido.")
            opcion = input("Ingrese una opción: ")

# opción 1: Ataque pesado            
        if opcion == '1':
            daño_final = ataque_pesado
            if vida_enemigo < 20:
                daño_final *= 1.5
            vida_enemigo -= daño_final
            print(f"¡Atacaste al enemigo por {daño_final:.2f} puntos de daño!")

# opción 2: Ráfaga veloz
        elif opcion == '2':
            print("¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
# opción 3: Curar                
        elif opcion == '3':
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1
                print("¡Te has curado por 30 puntos de vida!")
            else:
                print("¡No quedan pociones! Pierdes el turno.")
        turno_gladiador = False
    else:
        vida_gladiador -= ataque_enemigo
        print(f"¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")
        turno_gladiador = True
    print("=== NUEVO TURNO ===")
# Evaluación del resultado final
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")