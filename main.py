"""
Prototipo Programado - Áreas por reforestar en Guatemala
Algoritmos y Programación Básica
Desarrollado por Gerson Ramírez y Diego Betancourt
"""

""" Pendiente la extracción de información con csv
            persistencia de datos con PANDAS      """

#Liberias
import os
import getpass
import tabulate

#Listas
actRegist = []
infoG = []

#Info del admin
userS = "admin"
pssw = "admin"

""" Funciones """
#limpiar consola (estetico)
def clean():
    os.system("cls")

#Seguridad para actualizar la informacion
def security():
    print("Verifique su identidad")
    print("-"*50)
    userSC = input("Usuario: ")
    psswSC = getpass.getpass(prompt="Contraseña: ")
    if userSC == userS and psswSC == pssw:
        clean()
        print("Bienvenido")
        input()
        val = False
        clean()
    else:
        clean()
        print("¡Credenciales incorrectas!")
        input()
        val = True

    return(val)


#Se modula el ingreso de datos por pregunta
def register(data):
    dataI = str(input("Ingrese "+str(data)+" : " ))
    return(dataI)

#Encargado de preguntar nombre con formato
def name():
    print("-"*60)
    print("Ahora ingresará el nombre de su organización, empresa o \ninstitución, si es una persona escriba su nombre:")
    print("-"*60)
    profile = input("Nombre: ")
    return(profile)

#Se ingresa la información y se manda directamente a la lista al confirmar
def menuOpc(person):
    clean()
    actRegist = []
    print("registrando como ", person)
    print("Asegúrese de ingresar la información correctamente")
    print("-"*50)

    idPerson = str(len(infoG)+1)
    actRegist.append(idPerson)
    
    actRegist.append(person)
    actRegist.append(register("departamento"))
    actRegist.append(register("área del terreno (m3)"))
    actRegist.append(register("cantidad de árboles estimada"))
    actRegist.append(register("número de voluntarios"))
    actRegist.append(register("estado de la zona (%)"))
    actRegist.append(register("gasto estimado (Q)"))
    print("")

    dataSave = input("La siguiente información es correcta: (S/N): ")
    if dataSave == 'S':
        infoG.append(actRegist)
        print("La información ha sido agregada con éxito")
        print("")
    else:
        print("La información ha sido descartada")

#Se pregunta al usuario si desea seguir ingresando información, con el mismo nombre u otro distinto
def info():
    clean()
    dcs = "S"
    while dcs == "S":
        print("Bienvenido al sistema de ingreso de datos")
        sbj = name()
        dcs2 = "S"
        while dcs2 == "S":
            menuOpc(sbj)
            dcs2 = input("¿Desea seguir ingresando datos como "+sbj+"? (S/N): ")
            clean()
        dcs = input("¿Desea ingresar más información? (S/N): ")
        clean()

#Se encarga de mandar la información al archivo (.csv)
def save(): 
    clean()
    print("¡Pronto podrás guardar tus datos!")
    input()

def updateInfo(IDC):
    print("Ingrese el dato que desea modificar")
    print("-"*60)
    opc = input("1. Perfil \n2. Departamento \n3. Área de la zona \n4. Cantidad de Árboles  \n5. Número de voluntarios \n6.(%) Estado de la zona  \n7. (Q) Presupuesto estimado \nIngrese: ")
    print("-"*50)
    if opc.isdigit():
        opc = int(opc)
        if opc >= 1 and opc <= 7:
            if opc == 1:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][1] = newData
                print("¡Se ha realizado el cambio con éxito!")
            if opc == 2:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][2] = newData
                print("¡Se ha realizado el cambio con éxito!")
            if opc == 3:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][3] = newData
                print("¡Se ha realizado el cambio con éxito!")
            if opc == 4:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][4] = newData
                print("¡Se ha realizado el cambio con éxito!")
            if opc == 5:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][5] = newData
                print("¡Se ha realizado el cambio con éxito!")
            if opc == 6:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][6] = newData
                print("¡Se ha realizado el cambio con éxito!")
            if opc == 7:
                newData = input("Ingrese el dato nuevo: ")
                infoG[IDC-1][7] = newData
                print("¡Se ha realizado el cambio con éxito!")
        else:
            clean()
            print("La opción que ingresó no está dentro del rango")
            input()
    else:
        clean()
        print("La dato ingresado no es un número entero")
        input()
            
def update():
    clean()
    val = False
    while val == False:
        print("Sistema de actualización")
        print("-"*50)
        val = security()
        clean()
        print("Bienvenido al sistema de actualización")
        print("-"*50)
        print("Información disponible para modificar")
        print("-"*50)
        print(tabulate.tabulate(infoG, headers=["ID","Perfil","Departamento","Área","C. Árboles", "N. Voluntarios", "(%) Estado", "(Q) Presupuesto"]))
        print("-"*50)
        print("Opciones:")
        print("-"*50)
        opc = input("1. Modificar tabla \n2. Salir \nIngrese: ")
        print("-"*60)
        if opc.isdigit():
            opc = int(opc)
            if opc >= 1 and opc <= 2:
                if opc == 1:
                    idCheck = False
                    while idCheck == False:
                        print("La modificación se realiza a través del ID")
                        print("-"*60)
                        idChange = int(input("Ingrese el ID de la columna que desea cambiar: "))
                        if not idChange > len(infoG): 
                            print("-"*60)
                            updateInfo(idChange)
                            idCheck = True
                            val = True
                        else:
                            print("\n")
                            print("El ID escogido se encuentra fuera de rango")
                            print("\n")
                if opc == 2:
                    clean()
                    val = True
            else:
                clean()
                print("La opción que ingresó no está dentro del rango")
                input()
        else:
            clean()
            print("La dato ingresado no es un número entero")
            input()



#Funciona para poder salir del programa
def exitW():
    clean()
    ans = input("¿Desea guardar y salir? (S/N): ")
    if ans == "s":
        save()
        print("¡Los cambios han sido guardados!")
    else:
        print("¡Los cambios no han sido guardados!")
    return(True)

#El usuario podrá ver toda la información
def listInfo():
    clean()
    val = False
    while val == False:
        print("-"*50)
        print("Bienvenido al apartado para visualizar la información")
        print("-"*50)
        print("Opciones:")
        print("-"*50)
        opc = input("1. Mostrar toda la información \n2. Filtrar la información \n3. Salir \nIngrese: ")
        print("-"*50)
        if opc.isdigit():
            opc = int(opc)
            if opc >= 1 and opc <= 3:
                if opc == 1:
                    clean()
                    print(tabulate.tabulate(infoG, headers=["ID","Perfil","Departamento","Área","C. Árboles", "N. Voluntarios", "(%) Estado", "(Q) Presupuesto"]))
                    input()
                    val = True
                if opc == 2:
                    clean()
                    print("¡Funcionalidad aún no desarrollada! \nAplicación en Beta v.0")
                    input()
                    val = True
                if opc == 3:
                    clean()
                    val = True
            else:
                clean()
                print("La opción que ingresó no está dentro del rango")
                input()
        else:
            clean()
            print("La dato ingresado no es un número entero")
            input()

    

def menu():
    val = False
    while val == False:
        clean()
        print("Bienvenido al sistema")
        print("-"*40)
        print("1. Ingreso de datos \n2. Visualización de la información \n3. Actualizar información \n4. Guardar \n5. Salir")
        print("-"*40)
        opc = input("¿Qué desea realizar?: ")
        if opc.isdigit():
            opc = int(opc)
            if opc >= 1 and opc <= 5:
                if opc == 1:
                    info()
                if opc == 2:
                    listInfo()
                if opc == 3:
                    update()
                if opc == 4:
                    save()
                if opc == 5:
                    val = exitW()
            else:
                clean()
                print("La opción que ingresó no está dentro del rango")
                input()
        else:
            clean()
            print("La dato ingresado no es un número entero")
            input()

""" Algoritmo """
# Pendiente trabajar en Update para imprimir
menu()
