lista_reservas=[]

#FUNCION UTILIADA PARA INGRESAR LOS DATOS DE LA RESERVA
def ingresar_datos():
    lista_reservas=[]
    print("Ingrese los datos de la reserva");
    while True:
        nombre=input("NOMBRE: ");
        if len(nombre) <= 1:
            print("NOMBRE INVÁLIDO\n")
        else:
            lista_reservas.append(nombre);
            break
    while True:
        apellido=input("APELLIDO: ");
        if len(apellido) <= 1:
            print("APELLIDO INVÁLIDO\n")
        else:
            lista_reservas.append(apellido);
            break
    while True:
        ciudad_origen=input("CIUDAD DE ORIGEN: ");
        if len(ciudad_origen) <= 1:
            print("NOMBRE INVÁLIDO\n")
        else:
            lista_reservas.append(ciudad_origen);
            break
    
    while True:
        print("\tSeleccione destino(1-3):\n1.Torres del Paine\n2.Carretera Austral\n3.Chiloé");
        destino=int(input("DESTINO: "));
        destino1="Torres del Paine";
        destino2="Carretera Austral";
        destino3="Chiloé"
        if destino==1:
            lista_reservas.append(nombre);
            break
            
        elif destino==2:
            lista_reservas.append(destino1);
            break
        elif destino==3:
            lista_reservas.append(nombre);
            break
        else:
            print("Destino inválido")

    personas=input("CANTIDAD DE PERSONAS: ");
    lista_reservas.append(personas);
    with open("reservas.txt", "w") as documento:
        for elemento in lista_reservas:
            documento.write(f"{elemento}");
        print("Datos guardados")

#para guardar datos
def guardar():
    with open("reservas.txt", "w") as documento:
        for elemento in lista_reservas:
            documento.write(f"{elemento}");
        print("Datos guardados")

def imprimir_lista():
    print (lista_reservas);


