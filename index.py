import random,csv
#print(random.randint(10,50))

trabajadores = ["Juan Pérez",
                "María García",
                "Carlos López",
                "Ana Martínez",
                "Pedro Rodrígeuz",
                "Laura Hernández",
                "Miguel Sánchez",
                "Isabel Gómez",
                "Francisco Díaz",
                "Elena Fernández"]

def sueldo_aleatorio(trabajadores): #<----------1) Funcion que agrega un valor aleatorio a los usuarios

        lista = []
        objeto = [usuarios for usuarios in trabajadores]
        for usuario in objeto:
            agregar = usuario,random.randint(300000,2500000)
            lista.append(agregar)
        
        for trabajador in lista:
            print(f'EL sueldo de {trabajador[0]} es: {trabajador[1]}')
        
def Sueldos(trabajadores):
        lista = []
        objeto = [usuarios for usuarios in trabajadores]
        for usuario in objeto:
            agregar = usuario,random.randint(300000,2500000)
            lista.append(agregar)

        total_sueldo = 0;

        print(f'\nSueldos menores a $800.000\n')
        print('Nombre empleado\t Sueldo')
        for trabajador in lista:
            if trabajador[1] <= 800000:
                print(f'{trabajador[0]}\t${trabajador[1]}')
        print(f'\nSueldos entre a $800.000 y $2.000.000\n')
        print('Nombre empleado\t Sueldo')
        for trabajador in lista:    
            if trabajador[1] >= 800000 and trabajador[1] <= 2000000:
                print(f'{trabajador[0]}\t${trabajador[1]}')
            
        print(f'\nSueldos superior a $2.000.000\n')
        print('Nombre empleado\t Sueldo')
        for trabajador in lista:
            if trabajador[1] > 2000000:
                print(f'{trabajador[0]}\t${trabajador[1]}')
            total_sueldo += trabajador[1] + trabajador[1]

        print(F'TOTAL SUELDOS: ${total_sueldo}')


def estadísticas(trabajadores):
        lista = []
        objeto = [usuarios for usuarios in trabajadores]
        for usuario in objeto:
            agregar = usuario,random.randint(300000,2500000)
            lista.append(agregar)

        total = 0
        valores = []
        for empleados in lista:
            valores.append(empleados[1])
        
        for empleados in lista:
            total += empleados[1] + empleados[1]
        Promedio_sueldo = (total/10)
        Media_geo_sueldo = (total**(1/10))

        print(f'El sueldo mas alto es: {max(valores)}\nEl sueldo mas bajo es: {min(valores)}\nPromedio de sueldos es: {Promedio_sueldo}\nMedia geométrica es: {Media_geo_sueldo}')

def reporte(trabajadores):
        lista = []
        objeto = [usuarios for usuarios in trabajadores]
        for usuario in objeto:
            agregar = usuario,random.randint(300000,2500000)
            lista.append(agregar)

        print(f'Nombre empleado\tSueldo Base\tDescuento Salud\t\tDescuento AFP\t\t Sueldo líquido')
        for empleados in lista:

            print(f'{empleados[0]}\t{empleados[1]}\t\t{(empleados[1]*0.07/100)}\t{(empleados[1]*0.12/100)}\t\t{(empleados[1]*0.19/100)}')


try:
    while True:
        opcion = 0
        print("\nBienvenido a menú")
        print("\n[1]Asignar sueldos aleatorios.\n[2]Clasificar Sueldos.\n[3]Ver estadísticas.\n[4]Reporte Sueldos.\n[5]Salir del programa.")
        opcion = int(input("\nIngrese una opcion: "))
        if opcion <1 or opcion >6:
            print("!!!Debe ingresar una opcion valida!!!")
        else:   
            match opcion:
                case 1:
                    opc = 0
                    print(sueldo_aleatorio(trabajadores))
                    opc = int(input("\n¿Desea realizar otra operacion?\n[1]SI\n[0]NO\n  "))
                    if opc != 0:
                        continue
                    else:
                        print("Hasta pronto")
                        break
                case 2:
                    opc = 0
                    Sueldos(trabajadores)
                    opc = int(input("\n¿Desea realizar otra operacion?\n[1]SI\n[0]NO\n  "))
                    if opc != 0:
                        continue
                    else:
                        print("Hasta pronto")
                        break
                case 3:
                    opc = 0
                    estadísticas(trabajadores)
                    opc = int(input("\n¿Desea realizar otra operacion?\n[1]SI\n[0]NO\n  "))
                    if opc != 0:
                        continue
                    else:
                        print("Hasta pronto")
                        break
                case 4:
                    opc = 0
                    reporte(trabajadores)
                    opc = int(input("\n¿Desea realizar otra operacion?\n[1]SI\n[0]NO\n  "))
                    if opc != 0:
                        continue
                    else:
                        print("Hasta pronto")
                        break
                case 5:
                    print("Finalizando programa...\nDesarrollado por Diego Arias\nRUT 17.560.742-0")
                    break
except:
    print("Debe ingresar una opcion valida:",ValueError)