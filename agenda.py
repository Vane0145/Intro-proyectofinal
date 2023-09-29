'''Script en python que implemente una agenda 
de contactos haciendo uso de un diccionario.
Para el diccionario las llaves serán los nombre de los contactos y como valor estará una
tupla que contenga el número telefónico y el correo electrónico. 
Se tendrá un menú con las siguientes opciones:
1. Agregar contacto
2. Mostrar contacto
3. Buscar contacto
4. Modificar contanto
5. Eliminar contacto
6.Salir
'''


import os
import pathlib

AGREGAR = 1
MOSTRAR = 2
MODIFICAR = 3
BUSCAR = 4
ELIMINAR = 5
SALIR = 0


#Llamado de Funciones
#Función Menú
def menu():
    os.system('cls')
    print('**** Almacenamiento de Contactos en Archivo ****')
    print(f'''*** Menú de Opciones 
    {AGREGAR}) Agregar
    {MOSTRAR}) Mostrar
    {MODIFICAR}) Modificar
    {BUSCAR}) Buscar
    {ELIMINAR}) Eliminar
    {SALIR}) Salir
    ''')    

# Función Cargar Agenda
def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for line in archivo:
                contacto, telefono, email= line.strip().split(',')
                agenda.setdefault(contacto, (telefono,email))
    else:
        with open(nombre_archivo, 'w') as archivo:
            pass #Bloque no hace nada

# Función Agregar
def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('*** AGREGAR CONTACTO ***')
    nombre = input('Digita un nombre: ')
    if agenda.get(nombre):
        print('Contacto ya existe...')
    else:
        telefono = input('Digite el número de telefono: ')
        email = input('Digite correo electronico: ')
        with open(nombre_archivo,'a')as archivo:
            archivo.write(f'{nombre}, {telefono},{email}\n')
            print('Contacto agregado con éxito...!')

# Funcion Mostrar
def mostrar_agenda(agenda):
    os.system('cls')
    agenda = dict()
    nombre_archivo = 'agenda.txt'
    with open(nombre_archivo, 'r') as archivo:
        for line in archivo:
            contacto,telefono,email = line.strip().split(',')
            agenda.setdefault(contacto, (telefono,email))
    print('*** Mis Contactos ***')
    print('*** MOSTRAR ***')
    if len(agenda) >= 0:
        for contacto,datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Teléfono: {datos[0]}')
            print(f'Correo: {datos[1]}')
            print('^.^''o.o'*2)
    else:
        print('No hay contactos registrados.')
    archivo.close()

#Función Modificar
def modificar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('*** Mis Contactos ***')
    print('*** MODIFICAR ***')
    if len(agenda) > 0:
        nombre = input('Digite un nombre: ')
        cuentacont = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Teléfono: {datos[0]}')
                print(f'Correo: {datos[1]}')
                print('^.^''o.o'*3)
                cuentacont += 1
                telefono_search = datos[0]
                email_search = datos[1]
                nuevo_telefono = input('Digite el nuevo número de teléfono: ')
                nuevo_email = input('Digite el nuevo correo electrónico: ')
                agenda[contacto] = (nuevo_telefono, nuevo_email)
                with open(nombre_archivo, 'r') as archivo:
                    data = archivo.read()
                    data = data.replace(f'{contacto},{telefono_search},{email_search}', f'{contacto},{nuevo_telefono},{nuevo_email}')
                with open(nombre_archivo, 'w') as archivo:
                    archivo.write(data)
                print('Contacto actualizado con éxito...')
        if cuentacont == 0:
            print('No se encontró el contacto.')
    else:
        print('No hay contactos registrados.')

# Funcion buscar
def buscar_contacto(agenda):
    os.system('cls')
    print('*** Mis Contactos ***')
    print ('*** BUSCAR ***')
    if len(agenda) >= 0:
        nombre = input('Digite un nombre: ')
        cuentacont = 0
        for contacto,datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Teléfono: {datos[0]}')
                print(f'Correo: {datos[1]}')
                print('^.^''o.o'*3)
                cuentacont +=1
            if cuentacont == 0:
                print('No se encontro el contacto.')
            else:
                print(f' Se encontraron {cuentacont} contactos.') 
    else: 
        print('No hay contactos registrados.')

#  Delete contact
def eliminar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('*** MiS Contactos ***')
    print('*** ELIMINAR ***')
    if len(agenda) > 0:
        nombre = input('Digite un nombre: ')
        if nombre in agenda:
            contacto_eliminado = agenda.pop(nombre)
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
            with open(nombre_archivo, 'w') as archivo:
                for linea in lineas:
                    if f'{nombre},' not in linea:
                        archivo.write(linea)
            print(f'Contacto eliminado con éxito:\nNombre: {nombre}\nTeléfono: {contacto_eliminado[0]}\nCorreo: {contacto_eliminado[1]}')
        else:
            print('No se encontró el contacto.')
    else:
        print('No hay contactos registrados.')

input('*** Bienvenido(a) a tu agenda personal***')
# Ciclo para controlar el Menú
def main():
    agenda = dict()
    nombre_archivo = 'agenda.txt'
    cargar_agenda(agenda, nombre_archivo)
    continuar = True
    while continuar:
        menu()
        try:
            opc = int(input('Seleccione una opción: '))
            print('has digitado una opcion')
            if opc == AGREGAR:
                agregar_contacto(agenda, nombre_archivo)
            elif opc == MOSTRAR:
                mostrar_agenda(agenda)
            elif opc == MODIFICAR:
                modificar_contacto(agenda, nombre_archivo)
            elif opc == BUSCAR:
                buscar_contacto(agenda)
            elif opc == ELIMINAR:
                eliminar_contacto(agenda, nombre_archivo)
            elif opc == SALIR:
                continuar = False
            else:
                print('Opción no es válida...!')
        except ValueError:
            print('¡Error! Digita una opcion del 0 al 5: ')

        input('Presione enter para continuar...')
    print('Estamos para servirle, muchas gracias')

if __name__=='__main__':
    main()