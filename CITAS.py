# Sistema de Agenda de Turnos de Pacientes

agenda = []

while True:
    print("\n=================================")
    print("   AGENDA DE TURNOS PACIENTES")
    print("=================================")
    print("1. Registrar Turno")
    print("2. Consultar Agenda")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        fecha = input("Ingrese la fecha del turno (dd/mm/aaaa): ")
        hora = input("Ingrese la hora del turno (hh:mm): ")

        turno = {
            "Nombre": nombre,
            "Fecha": fecha,
            "Hora": hora
        }

        agenda.append(turno)
        print("\nTurno registrado exitosamente.")

    elif opcion == "2":
        print("\n===== LISTA DE TURNOS =====")

        if len(agenda) == 0:
            print("No existen turnos registrados.")
        else:
            for i, paciente in enumerate(agenda, start=1):
                print(f"{i}. {paciente['Nombre']} "
                      f"- Fecha: {paciente['Fecha']} "
                      f"- Hora: {paciente['Hora']}")

    elif opcion == "3":
        print("Sistema finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
