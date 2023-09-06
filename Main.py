import os
import time
import sys
import shutil
from datetime import date


def FacturacionTours():
  print("Facturando Tours..")
  LeerTodosLosArchivos("DatosAsignados")
  TourSeleccionado=input("Seleccione el nombre del tour que desea facturar: ")
  if os.path.exists("DatosFacturacion/Factura" + TourSeleccionado +".txt") :
     print("El tour ya fue facturado")
     time.sleep(2)
     borrarPantalla()
     Main()
  else:
      url = "DatosAsignados/" + TourSeleccionado +".txt"
      archivo = open(url, "r")
      lista = archivo.readlines()
      archivo.close()
      urlNuevo = "DatosFacturacion/Factura" + TourSeleccionado +".txt"
      archivo = open(urlNuevo, "w")
      archivo.write(lista[0])
      archivo.write(lista[1])
      archivo.write(lista[2])
      archivo.write(lista[3])
      archivo.write(lista[4])
      archivo.write(lista[5])
      archivo.write(lista[6])
      archivo.write(lista[7])
      archivo.write(lista[8])
      archivo.write(lista[9])
      archivo.write(lista[10])
      archivo.write(lista[11])
      costosdelTour = int(lista[4])
      nochesdeseadas = int(input("Ingrese las noches que desea: "))
      costototal=  costosdelTour * nochesdeseadas
      IMPUESTO = 16
      impuesto = costototal * IMPUESTO / 100
      costototal = costototal + impuesto
      print("El costo total es de: " + str(costototal))
      cuantoPaga = int(input("Ingrese cuanto paga el cliente: "))
      if cuantoPaga >= costototal:
        FechaFactura = date.today()
        cambio = cuantoPaga - costototal
        print("------------------------")
        print(f"Se facturo el tour con exito a {TourSeleccionado}")
        print(f"El cambio es de {cambio}")
        print(f"Fecha de la factura: {FechaFactura}")
        archivo.write("------------------------" + "\n")
        archivo.write("Informacion de la factura" + "\n")
        archivo.write("Fecha de la factura: " + str(FechaFactura) + "\n")
        archivo.write("Costo total por noche: " + str(costototal) + "\n")
        archivo.write("Impuesto: " + str(impuesto) + "\n")
        archivo.write("Pago del cliente: " + str(cuantoPaga) + "\n")
        archivo.write("Cambio: " + str(cambio) + "\n")
        archivo.close()
        Continuar = input("Desea continuar ? (Precione cualquier tecla): ")
        if Continuar == "Si":
          borrarPantalla()
          Main()
        else:
          borrarPantalla()
          Main()
      else:
        print("El cliente no pago lo suficiente")
        time.sleep(2)
        borrarPantalla()
        Main()
        

def AsignarTours():
  print("Asignando tours...")
  LeerTodosLosArchivos("Datos")
  TourSeleccionado=input("Escriba el nombre del tour que desea asignar: ")
  if os.path.exists("Datos/" + TourSeleccionado +".txt") :
    url = "Datos/" + TourSeleccionado +".txt"
    archivo = open(url, "r")
    lista = archivo.readlines()
    archivo.close()
    nombreUsuario = input("Ingrese el nombre del Cliente: ")
    apellidoUsuario = input("Ingrese el apellido del Cliente: ")
    telefonoUsuario = input("Ingrese el telefono del Cliente: ")
    CedulaUsuario = input("Ingrese la cedula del Cliente: ")
    urlNuevo = "DatosAsignados/"+ nombreUsuario +".txt"
    archivo = open(urlNuevo, "w")
    archivo.write(lista[0])
    archivo.write(lista[1])
    archivo.write(lista[2])
    archivo.write(lista[3])
    archivo.write(lista[4])
    archivo.write(lista[5])
    archivo.write(lista[6])
    archivo.write("------------------------" + "\n")
    archivo.write("Informacion del usuario" + "\n")
    archivo.write("Nombre del usuario: " + nombreUsuario + "\n")
    archivo.write("Apellido del usuario: " + apellidoUsuario + "\n")
    archivo.write("Telefono del usuario: " + telefonoUsuario + "\n")
    archivo.write("Cedula del usuario: " + CedulaUsuario + "\n")
    archivo.close()
    print("Tour asignado con exito")
    time.sleep(2)
    borrarPantalla()
    Main()
  else:
    print("El tour no existe")
    time.sleep(2)
    borrarPantalla()
    Main()


def ValidarCarpetaVacia(carpeta):
  if os.listdir(carpeta) == []:
    if carpeta == "Datos":
      print("Nececita agregar tours primero")
      time.sleep(2)
      borrarPantalla()
      Main()
    if carpeta == "DatosFacturacion":
      print("No hay facturas disponibles")
      time.sleep(2)
      borrarPantalla()
      Main()    
    if carpeta == "DatosAsignados":
      print("No hay tours asignados")
      time.sleep(2)
      borrarPantalla()
      Main() 
  else:
    return True


def ValidarExisteTour(nombreTour):
 if os.path.exists("Datos/" + nombreTour +".txt") :
    print("El tour ya existe , reintente")
    time.sleep(2)
    borrarPantalla()
    AgregarTour()


def ValidarExisteElID(id):
  for file in os.listdir("Datos"):
    if file.endswith(".txt"):
      archivo = open(os.path.join("Datos", file), "r")
      for line in archivo:
        if id in line:
          print("El ID ya existe")
          time.sleep(2)
          borrarPantalla()
          AgregarTour()
      archivo.close()


def AgregarTour():
  print("Agregando un nuevo tour...")
  id = str(input("Ingrese el numero del tour: "))
  ValidarExisteElID(id)
  nombreTour = str(input("Ingrese el nombre del tour: "))
  ValidarExisteTour(nombreTour)
  url = "Datos/" + nombreTour +".txt"
  archivo = open(url, "w")
  archivo.write("----------------------------------------------\n")
  archivo.write(f"ID: {id}" + "\n")
  descripcion = str(input("Ingrese la descripcion del tour: "))
  if descripcion == "":
    descripcion = "N/A"
  archivo.write("Descripcion: " + descripcion + "\n")
  try :
    CostoPorNoche = int(input("Ingrese el costo por noche: "))
  except ValueError:
    print("El valor ingresado no es valido")
    time.sleep(2)
    borrarPantalla()
    AgregarTour()
  if CostoPorNoche == "":
    CostoPorNoche = "N/A"
  archivo.write("Costo por noche: \n")
  archivo.write(f"{CostoPorNoche} \n")
  NombreGuia = str(input("Ingrese el nombre del guia: "))
  if NombreGuia == "":
    NombreGuia = "N/A"
  archivo.write("Nombre del guia: " + NombreGuia + "\n")
  Duracion = str(input("Ingrese la duracion del tour: "))
  if Duracion == "":
    Duracion = "N/A"
  archivo.write("Duracion: " + Duracion + "\n")
  Transporte = str(input("Ingrese (si/no) si el tours tiene transporte: "))
  if Transporte == "":
    Transporte = "N/A"
  archivo.write("Transporte: " + Transporte + "\n")
  archivo.close()
  print("Tour creado con exito")
  time.sleep(2)
  borrarPantalla()
  Main()


def LeerTodosLosArchivos(carpeta):
  for file in os.listdir(carpeta):
    if file.endswith(".txt"):
      nombreTour = file[:-4]
      print("Nombre del Tour --> " , nombreTour)
      archivo = open(os.path.join(carpeta, file), "r")
      print(archivo.read()) 
      archivo.close()


def LeerTodosLosTitulos():
  for file in os.listdir("Datos"):
    if file.endswith(".txt"):
      nombreTour = file[:-4]
      print("Nombre del Tour --> " , nombreTour)


def ModificarTour(nombreTour):
  url = "Datos/" + nombreTour +".txt"
  archivo = open(url, "r")
  lista = archivo.readlines()
  archivo.close()
  archivo = open(url, "w")
  archivo.write(lista[0])
  archivo.write(lista[1])
  descripcion = str(input("Ingrese la descripcion del tour: "))
  if descripcion == "":
    descripcion = "N/A"
  archivo.write("Descripcion: " + descripcion + "\n")
  CostoPorNoche = str(input("Ingrese el costo por noche: "))
  if CostoPorNoche == "":
    CostoPorNoche = "N/A"
  archivo.write("Costo por noche: \n")
  archivo.write(f"{CostoPorNoche} \n")
  NombreGuia = str(input("Ingrese el nombre del guia: "))
  if NombreGuia == "":
    NombreGuia = "N/A"
  archivo.write("Nombre del guia: " + NombreGuia + "\n")
  Duracion = str(input("Ingrese la duracion del tour: "))
  if Duracion == "":
    Duracion = "N/A"
  archivo.write("Duracion: " + Duracion + "\n")
  Transporte = str(input("Ingrese el transporte del tour: "))
  if Transporte == "":
    Transporte = "N/A"
  archivo.write("Transporte: " + Transporte + "\n")
  archivo.close()
  print("Tour modificado con exito")
  time.sleep(2)
  borrarPantalla()
  Main()


def EliminarTours(nombreTour):
  source = "Datos/" + nombreTour +".txt"
  destination = "DatosEliminados/" + nombreTour +".txt"
  shutil.copy(source, destination)
  print("Archivo eliminado exitosamente.")
  os.remove("Datos/" + nombreTour +".txt")


def OpcionMenu():
    while True:
        try:
            opc = int(input("<----Bienvenido al Administrador del Hotel Verde Ujarras---->"
                  "\n----Cual opcion desea utilizar----  ?"
                  "\n----> 1) Visualizar Tours"
                  "\n----> 2) Agregar Tours"
                  "\n----> 3) Asignar Tours"
                  "\n----> 4) Modificar tours"
                  "\n----> 5) Eliminar Tours" #ELiminado Logico
                  "\n----> 6) Facturacion de Tours"
                  "\n----> 7) Salir "
                  "\n:")) 
            break
        except ValueError:
            print("No es un numero, intentelo de nuevo")
            time.sleep(2)
            borrarPantalla()
    return opc


def borrarPantalla(): 
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")


def finalizar(var):
    if var == None:
      var = str(input("Desea utilizar otra funcion ? \n Y/N \n:"))
      var = var.upper()
      
    var = var.upper()
    if var == "Y" :
      borrarPantalla() 
      Main()

    elif var == "N":
      print("Salio del sistema")
      print("Saliendo en 1...2..")
      time.sleep(2)
      borrarPantalla()
      sys.exit()
    else:
      print("Opcion no valida")
      time.sleep(2)
      borrarPantalla()
      finalizar(None)


def Opcion1():
  if ValidarCarpetaVacia("Datos") == True:
    LeerTodosLosArchivos("Datos")
    var = str(input("Desea utilizar otra funcion ? \n Y/N \n:"))
    finalizar(var)


def Opcion2():
  AgregarTour()
  

def Opcion3():
  if ValidarCarpetaVacia("Datos") == True:
    AsignarTours()

#Modificar Tours 
def Opcion4():
  if ValidarCarpetaVacia("Datos") == True:
    print("Lista de Tours: ")
    LeerTodosLosTitulos()
    print("----------------------------------------------")
    TourSeleccionado=str(input("Cual tour desea modificar:\n"))
    if os.path.exists("Datos/" + TourSeleccionado +".txt") :
      ModificarTour(TourSeleccionado)
    else :
      print("El tour no existe")
      time.sleep(2)
      borrarPantalla()
      Main()

#Eliminar Tours Logico
def Opcion5():
  if ValidarCarpetaVacia("Datos") == True:
    print("Lista de Tours: ")
    LeerTodosLosTitulos()
    print("----------------------------------------------")
    TourSeleccionado=str(input("Escriba el tour que desea eliminar \n"
                              "Si desea regresar al menu principal digite Y \n:"))
    if TourSeleccionado == "Y":
      borrarPantalla()
      Main()
    if os.path.exists("Datos/" + TourSeleccionado +".txt") :
      confirmacion = input("Esta seguro que desea eliminar el tour " + TourSeleccionado + " ? \n Y/N \n:")
      if confirmacion == "Y":
        print("Seleccionado correctamente")
        EliminarTours(TourSeleccionado)
        finalizar(None)
      elif confirmacion == "N":
        print("Reintentando en 1...2..")
        time.sleep(2)
        borrarPantalla()
        Main()
    else:
      print("No existe, reintente")
      print("Reintentando en 1...2..")
      time.sleep(2)
      borrarPantalla()
      Opcion5()
 
#SubMenu Facturacion
def SubMenu6():
  borrarPantalla()
  try:
    opc = int(input("<----Bienvenido al SubMenu Facturacion del Hotel Verde Ujarras---->"
                      "\n----Cual opcion desea utilizar----  ?"
                      "\n----> 1) Visualizar Facturas"
                      "\n----> 2) Facturar un Tour"
                      "\n----> 3) Atras"
                      "\n:"))
    if opc == 1:
      Opcion7()
    elif opc == 2:
      if ValidarCarpetaVacia("DatosAsignados") == True:
        FacturacionTours()
    elif opc == 3 :
      borrarPantalla()
      Main()
    else:
      print("Opcion no valida ,  reintente")
      time.sleep(2)
      borrarPantalla()
      Main()
  except ValueError:
    print("No es un numero, intentelo de nuevo")
    time.sleep(2)
    borrarPantalla()
    Main()

#Funcion Visualizar Facturas
def Opcion7():
  if ValidarCarpetaVacia("DatosFacturacion") == True:
    LeerTodosLosArchivos("DatosFacturacion")
    var = str(input("Desea utilizar otra funcion ? \n Y/N \n:"))
    finalizar(var)

#Menu principal
def menu(opc):
  while True:
    if opc == 1:
      Opcion1()
    elif opc == 2:
      Opcion2()
    elif opc == 3 :
      Opcion3()
    elif opc == 4 :
      Opcion4()
    elif opc == 5 :
      Opcion5()
    elif opc == 6 :
      SubMenu6()
    elif opc == 7:
      var = "N"
      finalizar(var)
    else:
      print("Opcion no valida ,  reintente")
      time.sleep(2)
      borrarPantalla()
      Main()

#Main xd 
def Main():
 opc = OpcionMenu()
 menu(opc)

  
Main() 