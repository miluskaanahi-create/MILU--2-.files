using System;

namespace ParqueDiversiones
{
    class Program
    {
        static void Main(string[] args)
        {
            Atraccion atraccion = new Atraccion();
            int opcion;

            do
            {
                Console.Clear();

                Console.WriteLine("=======================================");
                Console.WriteLine("      PARQUE DE DIVERSIONES");
                Console.WriteLine("=======================================");
                Console.WriteLine("1. Registrar persona");
                Console.WriteLine("2. Ingresar a la atracción");
                Console.WriteLine("3. Mostrar cola");
                Console.WriteLine("4. Consultar siguiente persona");
                Console.WriteLine("5. Cantidad de personas");
                Console.WriteLine("6. Reporte");
                Console.WriteLine("7. Salir");
                Console.WriteLine("=======================================");
                Console.Write("Seleccione una opción: ");

                if (!int.TryParse(Console.ReadLine(), out opcion))
                {
                    opcion = 0;
                }

                Console.WriteLine();

                switch (opcion)
                {
                    case 1:
                        Console.Write("Ingrese el nombre: ");
                        string nombre = Console.ReadLine();

                        if (!string.IsNullOrWhiteSpace(nombre))
                        {
                            atraccion.RegistrarPersona(nombre);
                        }
                        else
                        {
                            Console.WriteLine("Nombre inválido.");
                        }
                        break;

                    case 2:
                        atraccion.IngresarPersona();
                        break;

                    case 3:
                        atraccion.MostrarCola();
                        break;

                    case 4:
                        atraccion.ConsultarPrimero();
                        break;

                    case 5:
                        atraccion.CantidadPersonas();
                        break;

                    case 6:
                        atraccion.Reporte();
                        break;

                    case 7:
                        Console.WriteLine("Gracias por utilizar el sistema.");
                        break;

                    default:
                        Console.WriteLine("Opción incorrecta.");
                        break;
                }

                if (opcion != 7)
                {
                    Console.WriteLine("\nPresione una tecla para continuar...");
                    Console.ReadKey();
                }

            } while (opcion != 7);
        }
    }
}