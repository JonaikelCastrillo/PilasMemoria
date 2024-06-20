from Historial import Historial
historial = Historial()

opcion = 0

while opcion != 7:
    opcion = int(input("Digite la opción que requiera:\n"
                       "1. Visitar página \n" 
                       "2. Retroceder a la página anterior\n"
                       "3. Ver última página visitada\n"
                       "4. Mostrar Historial\n" 
                       "5. Vaciar historial\n"
                       "6. Buscar página\n"
                       "7. Salir: \n"))
    
    match opcion:
        case 1:
            url = input("Ingrese el url de la página: ")
            historial.apilar(url)
        case 2:
            historial.desapilar()
        case 3:
            print("El url de la última página visitada es:", historial.ver_cima())
        case 4:
            historial.mostrar_elementos()
        case 5:
            historial.vaciar()
        case 6:
            url = input("Ingrese el url que desea buscar: ")
            historial.buscar(url)
        case 7:
            print("Saliendo...")
        case _:
            print("Opció inválida")

































"""print("La pila está vacía?", pila.esta_vacia())

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)

print("La pila está vacía?", pila.esta_vacia())
print("El elemento en la cima es:", pila.ver_cima())

print("\nElementos de la pila:")
pila.mostrar_elementos()

print("\nOrdenada de menor a mayor:")
pila.ordenar()

nueva_pila = pila.copiar()
print("\nElementos de la copia: ")
nueva_pila.mostrar_elementos()

print("\nBuscar elemento:")
pila.buscar(3)


print("\nVaciando pila...")
pila.vaciar()

print("\nDesapilando elementos...")
while not pila.esta_vacia():
    print(pila.desapilar())"""
    