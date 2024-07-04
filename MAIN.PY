"""Descripción de la Tarea: Desarrollar una aplicación en Python para la empresa de tours "SurExplora", con las siguientes funcionalidades:"""

"""1. Registrar Reserva:

  - Datos requeridos:
   - Nombre y apellido del cliente.
   - Ciudad de origen.
   - Detalle del tour (Torres del Paine, Carretera Austral, Chiloé).
   - Cantidad de personas.
  - Validar que todos los datos sean ingresados."""

import funcionesjiji as funcion


while True:
  print("\tSurExplora");
  print("1.Ingresar datos de la reserva");
  print("2.Ver todas las reservas realizadas");
  print("3.Imprimir detalle de reserva de un destino en particular");
  print("4.Salir");
  opcion=int(input("OPCIÓN:"))
  if(opcion==1):
        funcion.ingresar_datos();
  elif(opcion==2):
        print("\tReservas");
        funcion.imprimir_lista();
  elif(opcion==3):
        funcion.imprimir_lista()
  elif(opcion==4):
    print("Saliendo...")
    break
  else:
        print("Opción no válida");


"""2. Listar Reservas:
  - Mostrar en pantalla todas las reservas realizadas.

3. Imprimir Detalle de Reservas por Destino:
  - Seleccionar uno de los destinos y generar un archivo de texto (.txt) con el detalle de las reservas para ese destino.

4. Salir del Programa:
  - El programa debe funcionar hasta que el usuario decida salir.

5. GitHub
  - Subir el código completo del proyecto a GitHub."""

