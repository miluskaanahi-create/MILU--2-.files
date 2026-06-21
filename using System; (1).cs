using System;

namespace AgendaTurnosClinica
{
    // REGISTRO (STRUCT)
    public struct Paciente
    {
        public string Cedula;
        public string Nombre;
        public int Edad;
        public string Telefono;
    }

    // CLASE TURNO
    public class Turno
    {
        public Paciente Paciente;
        public string Especialidad;
        public string Fecha;
        public string Hora;

        public void Mostrar()
        {
            Console.WriteLine("-----------------------------------------");
            Console.WriteLine("Cédula       : " + Paciente.Cedula);
            Console.WriteLine("Paciente     : " + Paciente.Nombre);
            Console.WriteLine("Edad         : " + Paciente.Edad);
            Console.WriteLine("Teléfono     : " + Paciente.Telefono);
            Console.WriteLine("Especialidad : " + Especialidad);
            Console.WriteLine("Fecha        : " + Fecha);
            Console.WriteLine("Hora         : " + Hora);
            Console.WriteLine("-----------------------------------------");
        }
    }

    class Program
    {
        static Turno[] agenda = new Turno[100];
        static int totalTurnos = 0;

        // MATRIZ DE HORARIOS
        static string[,] horarios =
        {
            {"08:00","09:00","10:00","11:00"},
            {"13:00","14:00","15:00","16:00"}
        };

        static void Main(string[] args)
        {
            int opcion;

            do
            {
                Console.Clear();

                Console.WriteLine("======================================");
                Console.WriteLine("   AGENDA DE TURNOS DE PACIENTES");
                Console.WriteLine("======================================");
                Console.WriteLine("1. Registrar Turno");
                Console.WriteLine("2. Consultar Turnos");
                Console.WriteLine("3. Buscar Paciente");
                Console.WriteLine("4. Modificar Turno");
                Console.WriteLine("5. Eliminar Turno");
                Console.WriteLine("6. Ver Horarios");
                Console.WriteLine("7. Reportería");
                Console.WriteLine("8. Salir");
                Console.WriteLine("======================================");

                Console.Write("Seleccione una opción: ");
                opcion = Convert.ToInt32(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        RegistrarTurno();
                        break;

                    case 2:
                        ConsultarTurnos();
                        break;

                    case 3:
                        BuscarPaciente();
                        break;

                    case 4:
                        ModificarTurno();
                        break;

                    case 5:
                        EliminarTurno();
                        break;

                    case 6:
                        MostrarHorarios();
                        break;

                    case 7:
                        Reporteria();
                        break;

                    case 8:
                        Console.WriteLine("Gracias por utilizar el sistema.");
                        break;

                    default:
                        Console.WriteLine("Opción incorrecta.");
                        Console.ReadKey();
                        break;
                }

            } while (opcion != 8);
        }

        static void RegistrarTurno()
        {
            Console.Clear();

            if (totalTurnos >= agenda.Length)
            {
                Console.WriteLine("Agenda llena.");
                Console.ReadKey();
                return;
            }

            Paciente paciente = new Paciente();

            Console.Write("Cédula: ");
            paciente.Cedula = Console.ReadLine();

            Console.Write("Nombre: ");
            paciente.Nombre = Console.ReadLine();

            Console.Write("Edad: ");
            paciente.Edad = Convert.ToInt32(Console.ReadLine());

            Console.Write("Teléfono: ");
            paciente.Telefono = Console.ReadLine();

            Turno turno = new Turno();

            turno.Paciente = paciente;

            Console.Write("Especialidad: ");
            turno.Especialidad = Console.ReadLine();

            Console.Write("Fecha: ");
            turno.Fecha = Console.ReadLine();

            Console.Write("Hora: ");
            turno.Hora = Console.ReadLine();

            agenda[totalTurnos] = turno;
            totalTurnos++;

            Console.WriteLine("\nTurno registrado correctamente.");
            Console.ReadKey();
        }

        static void ConsultarTurnos()
        {
            Console.Clear();

            Console.WriteLine("===== LISTADO DE TURNOS =====");

            if (totalTurnos == 0)
            {
                Console.WriteLine("No existen registros.");
            }
            else
            {
                for (int i = 0; i < totalTurnos; i++)
                {
                    Console.WriteLine("\nTurno #" + (i + 1));
                    agenda[i].Mostrar();
                }
            }

            Console.ReadKey();
        }

        static void BuscarPaciente()
        {
            Console.Clear();

            Console.Write("Ingrese la cédula: ");
            string cedula = Console.ReadLine();

            bool encontrado = false;

            for (int i = 0; i < totalTurnos; i++)
            {
                if (agenda[i].Paciente.Cedula == cedula)
                {
                    Console.WriteLine("\nPaciente encontrado:");
                    agenda[i].Mostrar();
                    encontrado = true;
                    break;
                }
            }

            if (!encontrado)
            {
                Console.WriteLine("Paciente no encontrado.");
            }

            Console.ReadKey();
        }

        static void ModificarTurno()
        {
            Console.Clear();

            Console.Write("Ingrese la cédula del paciente: ");
            string cedula = Console.ReadLine();

            bool encontrado = false;

            for (int i = 0; i < totalTurnos; i++)
            {
                if (agenda[i].Paciente.Cedula == cedula)
                {
                    Console.WriteLine("\nDatos actuales:");
                    agenda[i].Mostrar();

                    Console.Write("Nueva especialidad: ");
                    agenda[i].Especialidad = Console.ReadLine();

                    Console.Write("Nueva fecha: ");
                    agenda[i].Fecha = Console.ReadLine();

                    Console.Write("Nueva hora: ");
                    agenda[i].Hora = Console.ReadLine();

                    Console.WriteLine("\nTurno actualizado correctamente.");
                    encontrado = true;
                    break;
                }
            }

            if (!encontrado)
            {
                Console.WriteLine("Paciente no encontrado.");
            }

            Console.ReadKey();
        }

        static void EliminarTurno()
        {
            Console.Clear();

            Console.Write("Ingrese la cédula del paciente: ");
            string cedula = Console.ReadLine();

            bool encontrado = false;

            for (int i = 0; i < totalTurnos; i++)
            {
                if (agenda[i].Paciente.Cedula == cedula)
                {
                    for (int j = i; j < totalTurnos - 1; j++)
                    {
                        agenda[j] = agenda[j + 1];
                    }

                    totalTurnos--;

                    Console.WriteLine("Turno eliminado correctamente.");
                    encontrado = true;
                    break;
                }
            }

            if (!encontrado)
            {
                Console.WriteLine("Paciente no encontrado.");
            }

            Console.ReadKey();
        }

        static void MostrarHorarios()
        {
            Console.Clear();

            Console.WriteLine("===== HORARIOS DISPONIBLES =====");

            for (int fila = 0; fila < horarios.GetLength(0); fila++)
            {
                for (int columna = 0; columna < horarios.GetLength(1); columna++)
                {
                    Console.Write(horarios[fila, columna] + "\t");
                }

                Console.WriteLine();
            }

            Console.ReadKey();
        }

        static void Reporteria()
        {
            Console.Clear();

            Console.WriteLine("===== REPORTERÍA =====");

            Console.WriteLine("Total de turnos registrados: " + totalTurnos);

            if (totalTurnos > 0)
            {
                Console.WriteLine("\nPacientes registrados:");

                for (int i = 0; i < totalTurnos; i++)
                {
                    Console.WriteLine(
                        (i + 1) + ". " +
                        agenda[i].Paciente.Nombre +
                        " - " +
                        agenda[i].Especialidad
                    );
                }
            }
            else
            {
                Console.WriteLine("No existen registros.");
            }

            Console.ReadKey();
        }
    }
}





[
    