# siglo21-ia-tp2-busquedaexhaustiva

"""
Trabajo Práctico 2 – Inteligencia Artificial
Búsqueda Exhaustiva – Simulación en Python
Autor: Julián Nicolás Ottonello Constantinidis
"""

# Parámetros del problema
posicion_real_A = 3.0  # La posición real está a 3 mm a la derecha de B
posicion_inicial_B = 0.0  # Posición teórica inicial del brazo robotizado
tolerancia = 0.1  # Margen de error aceptado en mm
delta = 0.5  # Paso de búsqueda en mm

# Función de palpación: compara la posición actual con la real
def palpar(posicion):
    """
    Devuelve True si la posición está dentro del margen de tolerancia respecto a la meta.
    """
    return abs(posicion - posicion_real_A) <= tolerancia

# Implementación de búsqueda exhaustiva (tipo anchura alternando izquierda y derecha)
def busqueda_exhaustiva():
    """
    Ejecuta una búsqueda alternando pasos hacia la izquierda y derecha hasta encontrar la posición correcta.
    Retorna: posición encontrada, cantidad de pasos, historial de movimientos.
    """
    movimientos = [(0, posicion_inicial_B)]  # historial de (iteración, posición)
    pasos = 0
    i = 1
    while True:
        pasos += 1
        # Verifica si la última posición palpada es la correcta
        if palpar(movimientos[-1][1]):
            return movimientos[-1][1], pasos, movimientos
        # Genera nuevas posiciones a izquierda y derecha
        izquierda = posicion_inicial_B - (i * delta)
        derecha = posicion_inicial_B + (i * delta)
        movimientos.append((-i, izquierda))
        movimientos.append((i, derecha))
        i += 1
        movimientos = movimientos[1:]  # se mantiene solo la última posición para palpación

# Ejecución del algoritmo
if __name__ == "__main__":
    posicion_encontrada, pasos_necesarios, historial = busqueda_exhaustiva()
    
    print("Posición encontrada (A):", posicion_encontrada)
    print("Cantidad de pasos necesarios:", pasos_necesarios)
    print("\nHistorial de posiciones:")
    for paso, posicion in historial:
        print(f"Iteración {paso}: {posicion:.2f} mm")
