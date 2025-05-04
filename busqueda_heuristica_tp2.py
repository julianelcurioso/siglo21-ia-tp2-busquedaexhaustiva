"""
Trabajo Práctico 2 – Inteligencia Artificial
Búsqueda Heurística – Simulación en Python
Autor: Julián Nicolás Ottonello Constantinidis
"""

# Parámetros del problema
posicion_real_A = 3.0  # La posición real del punto de montaje
posicion_inicial_B = 0.0  # Posición teórica inicial del brazo robotizado
tolerancia = 0.1  # Margen de error permitido en mm
delta = 0.5  # Paso de movimiento en mm

# Función de palpación: detecta si se alcanzó la meta
def palpar(posicion):
    """
    Verifica si la posición actual se encuentra dentro del margen de tolerancia respecto al objetivo.
    """
    return abs(posicion - posicion_real_A) <= tolerancia

# Función heurística: estima la distancia a la meta
def heuristica(posicion):
    """
    Retorna la distancia estimada entre la posición actual y la posición real del punto de montaje.
    """
    return abs(posicion - posicion_real_A)

# Implementación de la búsqueda heurística (greedy)
def busqueda_heuristica():
    """
    Ejecuta la búsqueda guiada por heurística.
    En cada paso, el robot decide avanzar a la izquierda o derecha, eligiendo la opción con menor estimación.
    """
    posicion_actual = posicion_inicial_B
    historial = [(0, posicion_actual)]
    pasos = 0

    while not palpar(posicion_actual):
        pasos += 1
        izquierda = posicion_actual - delta
        derecha = posicion_actual + delta
        # Se elige la dirección con menor heurística
        if heuristica(izquierda) < heuristica(derecha):
            posicion_actual = izquierda
        else:
            posicion_actual = derecha
        historial.append((pasos, posicion_actual))

    return posicion_actual, pasos, historial

# Ejecución del algoritmo
if __name__ == "__main__":
    posicion_final, pasos_usados, historia = busqueda_heuristica()

    print("Posición encontrada (A):", posicion_final)
    print("Cantidad de pasos:", pasos_usados)
    print("\nHistorial de búsqueda:")
    for paso, pos in historia:
        print(f"Paso {paso}: {pos:.2f} mm")
