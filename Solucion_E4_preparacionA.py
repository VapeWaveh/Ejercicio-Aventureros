def registrar_aventurero(lst_aventureros: dict, codigo: str, datos: list) -> bool:
    """
    Registra un aventurero en el sistema.
    """
    nombre, edad = datos
    if codigo not in lst_aventureros:
        lst_aventureros[codigo] = {"nombre" : nombre, "edad" : edad, "puntajes" : []}
        return True
    return False


def registrar_puntaje(lst_aventureros: dict, codigo: str, puntaje: int) -> bool:
    """
    Registra un puntaje para un aventurero.
    """
    if codigo in lst_aventureros:
        lst_aventureros[codigo]["puntajes"].append(puntaje)
        return True
    return False


def modificar_puntaje(lst_aventureros: dict, codigo: str, sesion: int, nuevo_puntaje: int) -> bool:
    """
    Modifica el puntaje de una sesión específica para un aventurero.
    """
    if codigo in lst_aventureros and 0 <= sesion < len(lst_aventureros[codigo]["puntajes"]):
        lst_aventureros[codigo]["puntajes"][sesion] = nuevo_puntaje
        return True
    return False

def mostrar_participacion(lst_aventureros: dict) -> None:
    """
    Muestra la participación total y promedio de cada aventurero.
    """
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        puntajes = datos["puntajes"]
        total = sum(puntajes)
        if len(puntajes>0):
            promedio = total / len(puntajes) 
        else:
            puntajes = 0
        print(f"{nombre} ({codigo}) - Total: {total}, Promedio: {promedio:.2f}")

def	participantes_con_bajo_promedio(lst_aventureros: dict, umbral: float):
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        puntajes = datos["puntajes"]
        if puntajes:
            promedio = sum(puntajes) / len(puntajes)
            if promedio < umbral:
                print(f"{nombre} ({codigo} tiene un promedio de {promedio:.2f} que está bajo el umbral de {umbral})")

def listar_aventureros(lst_aventureros: dict):
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        edad = datos["edad"]
        puntajes = datos["puntajes"]  
        print(f"{nombre} ({codigo} - Edad: {edad} - Puntajes: {puntajes})")      

def obtener_aventureros_por_edad(lst_aventureros: dict, edad: int):
    print(f"Aventureros mayores a {edad}")
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        edad_aventurero = datos["edad"]
        puntajes = datos["puntajes"]  
        if edad_aventurero > edad:
            print(f"{nombre} ({codigo} - Edad: {edad} - Puntajes: {puntajes})")      

def main():
    aventureros = {}
  
    while True:
        print("-" * 55)
        print("Bienvenido al Sistema del Club de Aventureros")
        print("-" * 55)
        print("\n1. Registrar aventurero")
        print("2. Agregar puntaje de sesión")
        print("3. Modificar puntaje")
        print("4. Ver participación total y promedio")
        print("5. Ver aventureros con bajo promedio")
        print("6. Listar aventureros y puntajes")
        print("7. Listar aventureros por edad")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            codigo = input("Código del aventurero: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            if registrar_aventurero(aventureros, codigo, [nombre, edad]):
                print("Aventurero registrado con éxito")
            else:
                print("Código de aventurero ya registrado")
        elif opcion == "2":
            codigo = input("Código del aventurero: ")
            try:
                puntaje = int(input("Puntaje de la sesión: "))
                if registrar_puntaje(aventureros, codigo, puntaje):
                    print("Puntaje registrado con éxito")
                else:
                    print("Código no encontrado")
            except ValueError:
                print("Puntaje inválido")
        elif opcion == "3":
            codigo = input("Código del aventurero: ")
            try:
                sesion = int(input("Número de sesión (empezando desde 0): "))
                nuevo_puntaje = int(input("Nuevo puntaje: "))
                if modificar_puntaje(aventureros, codigo, sesion, nuevo_puntaje):
                    print("Puntaje actualizado")
                else:
                    print("No se pudo modificar (verifica código o sesión)")
            except ValueError:
                print("Entrada inválida")
        elif opcion == "4":
            mostrar_participacion(aventureros)
        elif opcion == "5":
            try:
                umbral = float(input("Ingresa el umbral de promedio: "))
                participantes_con_bajo_promedio(aventureros, umbral)
            except ValueError:
                print("Umbral inválido")
        elif opcion == "6":
            listar_aventureros(aventureros)
        elif opcion == "7":
            try:
                edad = int(input("Ingrese el umbral de edad: "))
                obtener_aventureros_por_edad(aventureros, edad)
            except ValueError:
               print("Edad inválida")     
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
  main()
