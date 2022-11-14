import csv
import os
import time
import pandas as pd
from datetime import datetime, date
from os import system
import numpy as np

class Mascota:
    def __init__(self, nombre, fnacimiento, raza, nombredueno, dnidueno):
        self.nombre = nombre
        self.fnacimiento= fnacimiento
        self.raza = raza
        self.nombredueno=nombredueno
        self.dnidueno=dnidueno

    def __del__(self):
        return None

    def saluda(self) :
        print(f"Nombre:  {self.nombre}")
        print(f"Fecha de nacimiento: {self.fnacimiento}")
        print(f"Raza: {self.raza}")
        print(f"Nombre de dueño(a): {self.nombredueno}")
        print(f"DNI del dueño(a): {self.dnidueno}")


def cargarMascota(nombrearchivo):
    print("1")
    data = pd.read_csv('./'+nombrearchivo , encoding='latin1', sep= ';' )
    lista_mascotas = []
    for  index, row in data.iterrows():
        nombre = row['nombre']
        fnacimiento = row['fnacimiento']
        raza =row['raza']
        nombredueno = row['nombredueno']
        dnidueno = row['dnidueno']
        mascota =  Mascota(nombre, fnacimiento, raza, nombredueno, dnidueno)
        lista_mascotas.append(mascota)
    print("Se cargaron los datos de 5 mascotas")
    return(lista_mascotas)
    time.sleep(3)

def imprimirMascota(lista_mascotas):
    print("2")
    for mascota in lista_mascotas:
        mascota.saluda ()
        print("\n")

def agregarMascota(lista_mascotas):
    print("3")
    print(5*"*"+"REGISTRO - NUEVA MASCOTA"+"*"*5)
    nombre = input('Nombre: ')
    fnacimiento = input('Fecha de nacimiento: ')
    raza =input('Raza: ')
    nombredueno = input('Nombre de dueño(a): ')
    dnidueno = input('DNI del dueño(a): ')
    nuevamascota =  Mascota(nombre, fnacimiento, raza, nombredueno, dnidueno)
    lista_mascotas.append(nuevamascota)
    return(lista_mascotas)


def buscarMascota(lista_mascotas):
    print("4")
    opcion = ""
    while opcion != 's':
        lista_busqueda = []
        print(5*"*"+"Busqueda de mascotas"+ 5*"*")
        print("seleccione una opcion")
        print("[1] Busqueda por nombre")
        print("[2] Busqueda por edad")
        print("[3] Busqueda por raza")
        print("[4] Busqueda por nombre de dueño")
        print("[5] Busqueda por DNI de dueño")
        print("[s] Salir")
        opcion = input('Ingresa una opcion: ')
        if opcion == "1":
            print("1")
            nombre_busqueda = input("Ingrese nombre de mascota: ")
            for mascota in lista_mascotas:
                if mascota.nombre == nombre_busqueda:
                    lista_busqueda.append(mascota)
                
                ''' 
                if lista_mascotas.index('nombre') == nombre_busqueda:
                    lista_busqueda.append(elemento)'''
        elif opcion == "2":
            print("2")
            edad_busqueda = int(input("Ingrese edad de mascota: "))
            for mascota in lista_mascotas:
                if calculoedad(mascota.fnacimiento) == edad_busqueda:
                    lista_busqueda.append(mascota)

        elif opcion == "3":
            print("3")
            raza_busqueda = input("Ingrese raza de mascota: ")
            for mascota in lista_mascotas:
                if mascota.raza == raza_busqueda:
                    lista_busqueda.append(mascota)
        elif opcion == "4":
            print("4")
            nombre_dueño = input("Ingrese nombre de dueño: ")
            for mascota in lista_mascotas:
                if mascota.nombredueno == nombre_dueño:
                    lista_busqueda.append(mascota)
        elif opcion == "5":
            print("5")
            dni_dueño = int(input("Ingrese dni de dueño: "))
            for mascota in lista_mascotas:
                if int(mascota.dnidueno) == dni_dueño:
                    lista_busqueda.append(mascota)
        elif opcion == "s":
            respuesta = 's'
        elif opcion == "S":
            respuesta = 's'
        else:
            print('seleccione una opcion valida')
        
        for mascota in lista_busqueda:
            mascota.saluda ()
            print("\n")
        

def ordenarMascota(lista_mascotas):
    print("5")
    opcion = ""
    while opcion != 's':
        lista_ordenada = []
        print(5*"*"+"Ordenamiento de lista de mascotas"+ 5*"*")
        print("seleccione una opcion")
        print("[1] Ordenar por nombre")
        print("[2] Ordenar por edad")
        print("[3] Ordenar por raza")
        print("[4] Ordenar por nombre de dueño")
        print("[5] Ordenar por DNI de dueño")
        print("[s] Salir")
        opcion = input('Ingresa una opcion: ')
        
        if opcion == "1":
            print("1")
            lista_ordenada = sorted(lista_mascotas, key=lambda x: x.nombre)

        elif opcion == "2":
            print("2")
            lista_ordenada = sorted(lista_mascotas, key=lambda x: x.fnacimiento)
            

        elif opcion == "3":
            print("3")
            lista_ordenada = sorted(lista_mascotas, key=lambda x: x.raza)

        elif opcion == "4":
            print("4")
            lista_ordenada = sorted(lista_mascotas, key=lambda x: x.nombredueno)
        elif opcion == "5":
            print("5")
            lista_ordenada = sorted(lista_mascotas, key=lambda x: x.dnidueno)

        elif opcion == "s":
            respuesta = 's'
        elif opcion == "S":
            respuesta = 's'
        else:
            print('seleccione una opcion valida')
    
        for mascota in lista_ordenada:
            mascota.saluda ()
            print("\n")


def copia(lista_mascotas):
    print("6")
    lista_guardar = []
    for mascota in lista_mascotas:
        elemento = [mascota.nombre,mascota.fnacimiento,mascota.raza,mascota.nombredueno,mascota.dnidueno]
        lista_guardar.append(elemento)
    np.savetxt("file_name.csv", lista_guardar, delimiter=",", fmt='%s')


def calculoedad(fnacimiento):
    ahora =datetime.now()
    fecha = datetime.strptime(fnacimiento, '%d/%m/%Y')
    #dias
    num_dias =ahora-fecha
    num_dias = num_dias.days
    #obteniendo años
    años = num_dias//365
    return(años)





'''MENU PRINCIPAL'''


respuesta = ""
while respuesta != '7':
    print(10*"*"+"MENU PRINCIPAL VETERNARIA"+"*"*10)
    print("[1] Cargar datos")
    print("[2] Mostrar Mascotas")
    print("[3] Agregar Mascota")
    print("[4] Buscar Mascota")
    print("[5] Listar Mascotas")
    print("[6] Realizar copia en el dispositivo")
    print("[7] Salir")
    respuesta = input('Ingresa una opcion: ')
    if respuesta == "1":
        lista_mascotas = cargarMascota("DATOS VETERINARIA.csv")
    elif respuesta == "2":
        imprimirMascota(lista_mascotas)
    elif respuesta == "3":
        agregarMascota(lista_mascotas)
    elif respuesta == "4":
        buscarMascota(lista_mascotas)
    elif respuesta == "5":
        ordenarMascota(lista_mascotas)
    elif respuesta == "6":
        copia(lista_mascotas)
    elif respuesta == "7":
        respuesta = '7'
    else:
        print('Comando inválido')

    time.sleep(1)


