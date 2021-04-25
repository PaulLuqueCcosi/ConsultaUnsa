#!/usr/bin/python3

import urllib.request
from sys import argv
from datetime import datetime
import re
import sys

# Configuracion


textIntro = """
 ____                      _ _              _       _            
 / ___|___  _ __  ___ _   _| | |_ __ _    __| | __ _| |_ ___  ___ 
| |   / _ \| '_ \/ __| | | | | __/ _` |  / _` |/ _` | __/ _ \/ __|
| |__| (_) | | | \__ \ |_| | | || (_| | | (_| | (_| | || (_) \__ \\
 \____\___/|_| |_|___/\__,_|_|\__\__,_|  \__,_|\__,_|\__\___/|___/
                                                                  
             _     _ _                     _      
 _ __  _   _| |__ | (_) ___ ___  ___    __| | ___ 
| '_ \| | | | '_ \| | |/ __/ _ \/ __|  / _` |/ _ \\
| |_) | |_| | |_) | | | (_| (_) \__ \ | (_| |  __/
| .__/ \__,_|_.__/|_|_|\___\___/|___/  \__,_|\___|
|_|                                               
           _             _ _             _                  _        _       
  ___  ___| |_ _   _  __| (_) __ _ _ __ | |_ ___  ___    __| | ___  | | __ _ 
 / _ \/ __| __| | | |/ _` | |/ _` | '_ \| __/ _ \/ __|  / _` |/ _ \ | |/ _` |
|  __/\__ \ |_| |_| | (_| | | (_| | | | | ||  __/\__ \ | (_| |  __/ | | (_| |
 \___||___/\__|\__,_|\__,_|_|\__,_|_| |_|\__\___||___/  \__,_|\___| |_|\__,_|
                                                                             
 _   _ _   _ ____    _    
| | | | \ | / ___|  / \   
| | | |  \| \___ \ / _ \  
| |_| | |\  |___) / ___ \ 
 \___/|_| \_|____/_/   \_\\
                          
"""

salida = """
                        __   _,--="=--,_   __
                       /  \."    .-.    "./  \\
                      /  ,/  _   : :   _  \/` \\
                      \  `| /o\  :_:  /o\ |\__/
                       `-'| :="~` _ `~"=: |
                          \`     (_)     `/
                   .-"-.   \      |      /   .-"-.
.-----------------{     }--|  /,.-'-.,\  |--{     }-----------------.
 )                (_)_)_)  \_/`~-===-~`\_/  (_(_(_)                (
(  That is all, thank you very much for trying the software (V1.0)  )
 )                                                                 (
'-------------------------------------------------------------------'

"""


class ErrorNumEscuela(ValueError):
    def __init__(self, message, *args):
        super(ErrorNumEscuela, self).__init__(message, *args)


class Alumno:
    def __init__(self, args):
        self.num = args[0]
        self.CUI = args[1]
        self.surName = args[2]
        self.name = args[3]
        self.group = args[4]

    def __str__(self):

        if len(self.surName) < 9:
            apell = self.surName + "\t\t\t"
        elif len(self.surName) <= 15:
            apell = self.surName + "\t\t"
        else:
            apell = self.surName + "\t"

        if len(self.name) < 8:
            nombreF = self.name + "\t\t\t"
        elif len(self.name) <= 15:
            nombreF = self.name + "\t\t"
        else:
            nombreF = self.name + "\t"

        cabeza = "Apellidos\t\tNombres\t\t\tCUI\t\tGrupo\tAÑO\n\n"

        text = apell + nombreF + self.CUI + \
            "\t"+self.group + "\t"+self.CUI[0:4]

        return text


class Escuela:

    listaAlumnos = []

    def __init__(self, name, proceso):
        self.name = name
        self.proceso = proceso
        # self.listaAlumnos = listaAlumnos


# DATOS ---------------------------------
escuelas = {
    401: "AGRONOMÍA",
    402: "BIOLOGÍA",
    404: "INGENIERÍA PESQUERA",
    403: "CIENCIAS DE LA NUTRICIÓN",
    405: "ENFERMERÍA",
    431: "ARQUITECTURA",
    432: "FÍSICA",
    433: "MATEMÁTICAS",
    434: "QUÍMICA",
    435: "INGENIERÍA GEOFÍSICA",
    436: "INGENIERÍA GEOLÓGICA",
    437: "INGENIERÍA ELECTRÓNICA",
    438: "INGENIERÍA INDUSTRIAL",
    440: "INGENIERÍA CIVIL",
    441: "INGENIERÍA METALÚRGICA",
    442: "INGENIERÍA QUÍMICA",
    443: "INGENIERÍA DE MINAS",
    444: "INGENIERÍA DE INDUSTRIAS ALIMENTARIAS",
    445: "INGENIERÍA DE MATERIALES",
    446: "INGENIERÍA DE SISTEMAS",
    447: "INGENIERÍA ELÉCTRICA",
    448: "INGENIERÍA MECÁNICA",
    449: "INGENIERÍA AMBIENTAL",
    450: "CIENCIA DE LA COMPUTACIÓN",
    451: "INGENIERÍA SANITARIA",
    452: "INGENIERÍA EN TELECOMUNICACIONES",
    461: "EDUCACIÓN",
    463: "HISTORIA",
    464: "SOCIOLOGÍA",
    465: "TRABAJO SOCIAL",
    466: "ANTROPOLOGÍA",
    467: "ADMINISTRACIÓN",
    468: "CONTABILIDAD",
    469: "DERECHO",
    470: "ECONOMÍA",
    471: "ARTES",
    472: "FILOSOFÍA",
    473: "LITERATURA Y LINGÜÍSTICA",
    474: "PSICOLOGÍA",
    475: "RELACIONES INDUSTRIALES",
    478: "CIENCIAS DE LA COMUNICACIÓN",
    479: "TURISMO Y HOTELERÍA",
    486: "FINANZAS",
    487: "MARKETING",
    488: "BANCA Y SEGUROS",
    489: "GESTIÓN"
}

# funciones ------------------------------


def mostrarEscuelas():  # Mejorar
    print("-----------------------------------------------------------------------------")
    for key, value in escuelas.items():
        print(f"[{key}]-{value}")
    print("-----------------------------------------------------------------------------")


def preguntarEscuela():

    try:
        numEscu = int(input("Ingrese escuela: "))
        if (escuelas.get(numEscu) != None):
            print("Selecionado")

            return [numEscu, str(escuelas.get(numEscu))]
        else:
            print("NUMERO NO REGISTRADO")
            raise ErrorNumEscuela("No valido")

    except ValueError:
        print("INGRESE SOLO NUMEROS")
        op = input(
            "Presione ENTER para continuar \nPresione '0' para volver a ver las opciones: ")
        if op == "0":
            mostrarEscuelas()
        return preguntarEscuela()

    except ErrorNumEscuela:
        op = input(
            "Presione ENTER para continuar \nPresione '0' para volver a ver las opciones: ")

        if op == "0":
            mostrarEscuelas()
        return preguntarEscuela()


def generarArchivo(datos):
    print("La escuela es: %s" % data[1])

    # Esto es con internet-------------- (Todo con ### al final)
    url = "http://extranet.unsa.edu.pe/sisacad/ver_grupos_por_escuela.php?codescu=" + \
        str(data[0])

    try:

        if True:  # ONLINE (T = online, F = offline)

            # print("Cargando URL: " + url)                     ###
            print("Conectando a servidor [...]")
            with urllib.request.urlopen(url) as html_request:
                html = str(html_request.read(), "utf-8")
                print("Recibiendo datos [...]")
                # print(html)

                p = convertirFormato(html)
                lista = convertirLista(p)

                return lista
            return None

        else:

            # LOCAL
            ruta = "/home/pool/pruebas/python/CUI-SIN-FECHA/"
            name_file = str(data[1])+"-"+str(data[0])+".html"
            ruta += name_file
            html = open(ruta, "r")
            html = html.read()
            print("Reciviendo datos [...]")

            p = convertirFormato(html)
            lista = convertirLista(p)

            return lista

    except Exception as e:
        print(e.messages())
        print("*** ERROR EN LA CONEXION 1***\n*** Verifique su conexion a internet e intente nuevamente ***")
        sys.exit()


# Metodos internos
def convertirFormato(text):

    print("-------------- Procesando texto (ESTO PUEDE TARDAR UN MOMENTO) --------------")
    text = text.replace("</tr><tr>", "|")
    text = text.replace("<tr>", "|", 1)
    text = text.replace("</tr>", "|", 1)

    # EXpresiones Regulares -----------------
    text = re.sub("(.|\n)*<BODY>(\n)*", "", text)

    # texto plano--------------------

    # remm = "<HTML>\n<HEAD>  <TITLE> Matricula - Informacion </TITLE>\n  <LINK HREF=\"estilos_matricula.css\" REL=\"stylesheet\" TYPE=\"text/css\">\n  <SCRIPT language=JavaScript>\n  </SCRIPT>\n</HEAD>\n\n<BODY>\n"
    # text = text.replace(remm, "", 1)

    return text


def convertirLista(p):

    lista = []
    new = re.match("^([^|]+)\|(.+)", p)
    while(new):
        if new:
            lista.append(new.group(1))
            p = new.group(2)
        new = re.match("^([^|]+)\|(.+)", p)

    return lista
# ---------------------------------------


def arregloProcesado(lista):
    try:
        linea = lista[0]
        pa = re.match(
            ".*(202[1-9]-I{1,2}).*(<\/h2><h2><center>(.*)<\/center>)", linea)
        curso = pa.group(3)
        proceso = pa.group(1)
        item = str(curso)+"|"+str(proceso)
        lista[0] = item

        # Para la cabeza (1)
        lista[1] = re.sub(
            "(<th \w*=[1-9][1-9]%>|(<\/th><th \w*=[0-9][0-9]%>)|(<\/th><th>)|(<\/th>)|( y ))", "|", lista[1])
        lista[1] = str(lista[1])[1:len(lista[1])-1]

        # DEl segundo para adelante (2)
        i = 2
        while (i < len(lista)):
            lista[i] = re.sub(
                "((((<\/font>)?<\/td>)?<td align=center>)|(<\/td><td>)|(, )|(<\/td>))", "|", lista[i])
            lista[i] = str(lista[i])[1:len(lista[i])-1]
            i += 1

        return lista
    except IndexError:
        print("*** NO SE PUEDE PROCESAR ***")
        print("*** verifique si conexion a internet e intentelo de nuevo ***")
        sys.exit()


def arregloDatosSeparados(lista):
    i = 0
    listaPrincipall = []
    while (i < len(lista)):
        listaDefinida = str(lista[i]).split("|")
        listaPrincipall.append(listaDefinida)
        i += 1
    return listaPrincipall


def listaClaseAlumnos(lista):

    escuela = Escuela(lista[0][0], lista[0][1])

    j = 2
    listaAlumnos = []
    while (j < len(lista)):
        escuela.listaAlumnos.append(Alumno(lista[j]))
        listaAlumnos.append(Alumno(lista[j]))  # OJO
        j += 1

    return escuela


# ---------------------------------------------------------------------------

def imprimir(listaAlumnos):

    if listaAlumnos == None:
        pass

    elif len(listaAlumnos) == 0:
        print("\n------------------------------ SIN RESULTADOS ------------------------------\n")

    else:

        print("\n-------------------------------- RESULTADOS --------------------------------\n")

        print("APELLIDOS\t\tNOMBRES\t\t\tCUI\t\tGRUPO\tAÑO\n\n")

        for alum in listaAlumnos:
            print(alum)

        print("\n------------------------------ FIN RESULTADOS ------------------------------\n")


def menuPrincipal(clase):
    while True:
        text = """
[1] Mostrar todos los alumno                [2] Buscar alumno (Nombre o CUI)
[3] Busqueda avanzada                       [4] Salir\n"""

        # print("Seleccione una opcion", end="")
        print(text)
        try:
            op = int(input(": "))

            if op == 1:
                # print("Mostrar todos")
                mostrarTodosAlumnos(clase)
                # menuPrincipal(clase)

            elif op == 2:
                # print("Buscar alumno")
                buscarAlumno(clase)
                # menuPrincipal(clase)
            elif op == 3:
                buscarAvanzado(clase)
                # menuPrincipal(clase)
            elif op == 4:
                print(salida)
                sys.exit(0)
            else:
                print("*** OPCION NO VALIDA ***")
                # menuPrincipal(clase)
        except ValueError:
            print("*** INGRESE SOLO NUMEROS ***")


def mostrarTodosAlumnos(clase):
    lista = clase.listaAlumnos
    imprimir(lista)


def buscarAlumno(clase):

    while True:

        print("Buscando en : "+clase.name)
        print("Proceso : "+clase.proceso)

        text = """
[1] CUI                [2] Nombre                 [3] Apellido
[4] CUI(parcial)       [5] Nombre(parcial)        [6] Apellido(parcial)
[7] Atras                                         [8] Salir\n"""

        print(text)

        try:
            op = int(input(": "))

            if op == 1:
                lis = buscarPorCUI(clase)
                imprimir(lis)
                # buscarAlumno(clase)

            elif op == 2:
                lis = buscarPorName(clase)
                imprimir(lis)
                # buscarAlumno(clase)

            elif op == 3:
                lis = buscarPorApellido(clase)
                imprimir(lis)
                # buscarAlumno(clase)

            elif op == 4:
                lis = buscarPorCUIParte(clase)
                imprimir(lis)
                # buscarAlumno(clase)

            elif op == 5:
                lis = buscarPorNameParte(clase)
                imprimir(lis)
                # buscarAlumno(clase)
            elif op == 6:
                lis = buscarPorApellidoParte(clase)
                imprimir(lis)
                # buscarAlumno(clase)
            elif op == 7:
                print("Atras")
                break
            elif op == 8:
                print(salida)
                sys.exit(0)
            else:
                print("*** OPCION NO VALIDA ***")
                # buscarAlumno(clase)
        except Exception as e:

            print("*** INGRESE SOLO NUMEROS ***")


def buscarAvanzado(clase):
    while True:

        print("Buscando en : "+clase.name)
        print("Proceso : "+clase.proceso)

        text = """
[1] Año ingreso         [2] Grupo (ultima matricula)     [3] Combinar ([1] [2])
[4] Seleccionar que     [5] Atras                        [6] Salir 
    parametros buscar\n"""

        print(text)

        try:
            op = int(input(": "))

            if op == 1:
                lis = buscarPorAnio(clase)
                imprimir(lis)
                # buscarAvanzado(clase)

            elif op == 2:
                lis = buscarPorGrupo(clase)
                imprimir(lis)
                # buscarAvanzado(clase)

            elif op == 3:
                lis = buscarCombinar1_2(clase)
                imprimir(lis)
                # buscarAvanzado(clase)
            elif op == 4:
                lis = buscarIntroducirDatos(clase)
                imprimir(lis)
                # buscarAvanzado(clase)

            elif op == 5:

                break
            elif op == 6:
                print(salida)
                sys.exit(0)
            else:
                print("*** OPCION NO VALIDA ***")
                # buscarAvanzado(clase)
        except Exception as e:

            print("*** INGRESE SOLO NUMEROS***")


# Metodos internos BUSCAR AVANZADO

def buscarPorAnio(clase):
    anio = input("AÑO: ")
    if (len(anio) != 4 or anio.isdigit() == False):
        print("*** INGRESE UN AÑO VALIDO ***")
        return None
    else:

        print("Buscando el AÑO: "+anio + " [...]")
        listaResultados = []
        # print(clase.listaAlumnos)

        for alum in clase.listaAlumnos:
            anioAlum = str(alum.CUI)[0:4]
            if anio == anioAlum:
                listaResultados.append(alum)

        return listaResultados


def buscarPorGrupo(clase):
    try:
        group = int(input("Grupo: "))
    except Exception:
        group = 10  # ERROR

    if (group > 3 or group < 1):
        print("*** INGRESE UN GRUPO CORRECTO (1,2,3)  ***")
        # buscarAvanzado(clase)
        return None
    else:
        print("Buscando el grupo: "+str(group) + " [...]")
        listaResultados = []
        group = str(group)
        for alum in clase.listaAlumnos:
            if group == alum.group:
                listaResultados.append(alum)

                # break
        return listaResultados


def buscarCombinar1_2(clase):

    lista = buscarPorAnio(clase)

    if lista == None:
        return None

    claseTem = Escuela(clase.name, clase.proceso)
    claseTem.listaAlumnos = lista

    lista = buscarPorGrupo(claseTem)

    return lista


def buscarIntroducirDatos(clase):
    claseTem = Escuela(clase.name, clase.proceso)

    cuiCompleto = False
    cuiParte = False
    cuiParteW = False
    nameCompleto = False
    nameParte = False
    nameParteW = False
    surNameCompelto = False
    surNameParte = False
    surNameParteW = False
    group = False
    anio = False

    txt = """ 
[] CUI                  [] CUI(parcial)         [] Nombre
[] Nombre(parcial)      [] Apellido             [] Apellido(parcial)
[] Grupo                [] AÑO INGRESO     

Estas son las opciones 
INGRESE <ENTER> PARA PASAR 
INGRESE <CALQUIER TECLA> PARA SELECCIONAR E INGRESAR EL VALOR\n
"""
    print(txt)
    listaResultadosFinal = None
    listaResultados = clase.listaAlumnos

    # CUI
    cuiOp = input("[?]CUI (<enter>, 'y'):")
    if cuiOp == "":
        print("[x] CUI")
    else:
        print("[✓] CUI: ")
        for i in range(3):  # PUede haber un error
            listaResultadosTem = buscarPorCUI(clase)  # POr ser el primero
            if listaResultadosTem != None:
                listaResultados = listaResultadosTem
                cuiCompleto = True
                break

    # CUI PARTE
    if not(cuiCompleto):

        cuiOpPart = input("[?]CUI -  parte (<enter>, 'y'):")
        if cuiOpPart == "":
            print("[x] CUI parte")
        else:
            print("[✓] CUI: parte")
            for i in range(3):  # PUede haber un error
                claseTem.listaAlumnos = listaResultados
                listaResultadosTem = buscarPorCUIParte(claseTem)
                if listaResultadosTem != None:  # esta bien
                    cuiParte = True
                    listaResultados = listaResultadosTem
                    break

    # Nombre
    nameOp = input("[?] NOMBRE (<enter>, 'y'):")
    if nameOp == "":
        print("[x] NOMBRE")
    else:
        print("[✓] NOMBRE ")
        for i in range(3):  # PUede haber un error
            claseTem.listaAlumnos = listaResultados
            listaResultadosTem = buscarPorName(claseTem)
            if listaResultadosTem != None:  # esta bien
                nameCompleto = True
                listaResultados = listaResultadosTem
                break

    # NOMBRE PARTE
    if not(nameCompleto):
        cuiOpPart = input("[?]NOMBRE -  parte (<enter>, 'y'):")
        if cuiOpPart == "":
            print("[x] NOMBRE parte")
        else:
            print("[✓] NOMBRE parte")
            for i in range(3):  # PUede haber un error
                claseTem.listaAlumnos = listaResultados
                listaResultadosTem = buscarPorNameParte(claseTem)
                if listaResultadosTem != None:  # esta bien
                    nameParte = True
                    listaResultados = listaResultadosTem
                    break

    # APELLIDO
    surNameOp = input("[?] APELLIDO (<enter>, 'y'):")
    if surNameOp == "":
        print("[x] APELLIDO")
    else:
        print("[✓] APELLIDO ")
        for i in range(3):  # PUede haber un error
            claseTem.listaAlumnos = listaResultados
            listaResultadosTem = buscarPorApellido(claseTem)
            if listaResultadosTem != None:  # esta bien
                surNameCompelto = True
                listaResultados = listaResultadosTem
                break

    # APELLIDO PARTE
    if not(surNameCompelto):
        cuiOpPart = input("[?]APELLIDO -  parte (<enter>, 'y'):")
        if cuiOpPart == "":
            print("[x] APELLIDO parte")
        else:
            print("[✓] APELLIO parte")
            for i in range(3):  # PUede haber un error
                claseTem.listaAlumnos = listaResultados
                listaResultadosTem = buscarPorApellidoParte(claseTem)
                if listaResultadosTem != None:  # esta bien
                    surNameParte = True
                    listaResultados = listaResultadosTem
                    break

    # GRUPO
    groupOp = input("[?] GRUPO (<enter>, 'y'):")
    if groupOp == "":
        print("[x] GRUPO")
    else:
        print("[✓] GRUPO ")
        for i in range(3):  # PUede haber un error
            claseTem.listaAlumnos = listaResultados
            listaResultadosTem = buscarPorGrupo(claseTem)
            if listaResultadosTem != None:  # esta bien
                group = True
                listaResultados = listaResultadosTem
                break

     # AÑO INGRESO
    anioOp = input("[?] AÑO INGRESO (<enter>, 'y'):")
    if anioOp == "":
        print("[x] AÑO INGRESO")
    else:
        print("[✓] AÑO INGRESO ")
        for i in range(3):  # PUede haber un error
            claseTem.listaAlumnos = listaResultados
            listaResultadosTem = buscarPorAnio(claseTem)
            if listaResultadosTem != None:  # esta bien
                anio = True
                listaResultados = listaResultadosTem
                break

    # Resultados finales
    # CCoregir el final (Puede ser con TRUE o FALSE en las funciones que encuentra)
    # IMPRIME LOS VALORES
    print("\nRESUMEN")
    if cuiCompleto:
        print("[✓] CUI", end='\t\t\t')
    else:
        print("[x] CUI", end='\t\t\t')

    if cuiParte:
        print("[✓] CUI parcial", end='\n')
    else:
        print("[x] CUI parcial", end='\n')

    if nameCompleto:
        print("[✓] NOMBRE", end='\t\t')
    else:
        print("[x] NOMBRE", end='\t\t')

    if nameParte:
        print("[✓] NOMBRE parcial", end='\n')
    else:
        print("[x] NOMBRE parcial", end='\n')

    if surNameCompelto:
        print("[✓] APELLIDO", end='\t\t')
    else:
        print("[x] APELLIDO", end='\t\t')

    if surNameParte:
        print("[✓] APELLIDO parcial", end='\n')
    else:
        print("[x] APELLIDO parcial", end='\n')

    if group:
        print("[✓] GRUPO", end='\t\t')
    else:
        print("[x] GRUPO", end='\t\t')

    if anio:
        print("[✓] AÑO", end='\n')
    else:
        print("[x] AÑO", end='\n')

    if (cuiCompleto or
        cuiParte or
        nameCompleto or
        nameParte or
        surNameCompelto or
        surNameParte or
        group or
            anio):
        listaResultadosFinal = listaResultados
    else:
        print("* NO EXISTEN PARAMETROS PARA LA BUSQUEDA *")

    return listaResultadosFinal


# Metodos internos BUSCAR BASICO
def buscarPorCUI(clase):
    cui = input("CUI: ")
    if (len(cui) != 8 or cui.isdigit() == False):
        print("*** INGRESE UN CUI VALIDO ***")
        return None
    else:
        print("Buscando el cui: "+cui + " [...]")
        listaResultados = []

        for alum in clase.listaAlumnos:

            if cui == alum.CUI:
                listaResultados.append(alum)
                break

        return listaResultados


def buscarPorName(clase):

    name = input("Nombre: ")
    if (len(name) <= 1 or re.search("[1-9]+", name)):
        print("*** INGRESE UN NOMBRE CORRECTO  ***")
        return None
    else:
        name = name.upper()
        print("Buscando el Nombre: "+name + " [...]")
        listaResultados = []

        # print(clase.listaAlumnos)

        for alum in clase.listaAlumnos:
            alumListName = str(alum.name).split(" ")

            try:
                if (name == alumListName[0] or name == alumListName[1]):
                    listaResultados.append(alum)
            except IndexError:
                continue

        return listaResultados


def buscarPorApellido(clase):
    surName = input("Apellido: ")
    if (len(surName) <= 1 or re.search("[1-9]+", surName)):
        print("*** INGRESE UN APELLIDO CORRECTO  ***")
        return None
    else:
        surName = surName.upper()
        print("Buscando el Apellido: "+surName + " [...]")
        listaResultados = []

        # print(clase.listaAlumnos)

        for alum in clase.listaAlumnos:
            alumListSurName = str(alum.surName).split("/")
            # print(alumListSurName)
            try:
                if (surName == alumListSurName[0] or surName == alumListSurName[1]):
                    listaResultados.append(alum)
            except IndexError:
                continue

        return listaResultados


def buscarPorCUIParte(clase):
    cui = input("Parte del CUI: ")
    if ((len(cui) > 8 or len(cui) <= 1) or cui.isdigit() == False):
        print("*** INGRESE UN CUI VALIDO ***")
        return None
    else:
        print("Buscando el cui (parte): "+cui + " [...]")
        listaResultados = []

        # print(clase.listaAlumnos)

        for alum in clase.listaAlumnos:

            if re.search(str(cui), alum.CUI):
                listaResultados.append(alum)

        return listaResultados


def buscarPorNameParte(clase):

    namePart = input("Parte del nombre: ")
    if (len(namePart) <= 1 or re.search("[1-9]+", namePart)):
        print("*** INGRESE UN NOMBRE CORRECTO  ***")
        return None
    else:
        namePart = namePart.upper()
        print("Buscando el Nombre (parte): "+namePart + " [...]")
        listaResultados = []

        for alum in clase.listaAlumnos:
            alumListNamePart = str(alum.name).split(" ")

            try:
                if (re.search(namePart, alumListNamePart[0]) or re.search(namePart, alumListNamePart[1])):
                    listaResultados.append(alum)
            except IndexError:
                continue

        return listaResultados


def buscarPorApellidoParte(clase):

    surNamePart = input("Parte del apellido: ")
    if (len(surNamePart) <= 1 or re.search("[1-9]+", surNamePart)):
        print("*** INGRESE UN APELLIDO CORRECTO  ***")
        return None
    else:
        surNamePart = surNamePart.upper()
        print("Buscando el Nombre (parte): "+surNamePart + " [...]")
        listaResultados = []

        for alum in clase.listaAlumnos:
            alumListsurNamePart = str(alum.surName).split("/")

            try:
                if (re.search(surNamePart, alumListsurNamePart[0]) or re.search(surNamePart, alumListsurNamePart[1])):
                    listaResultados.append(alum)
            except IndexError:
                continue

        return listaResultados


# Iniciar--------------------------------


print(textIntro)

input("Presione <ENTER>")


mostrarEscuelas()
data = preguntarEscuela()
lista = generarArchivo(data)
lista = arregloProcesado(lista)
lista = arregloDatosSeparados(lista)
clase = listaClaseAlumnos(lista)
menuPrincipal(clase)
