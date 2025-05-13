
# TP2 – Inteligencia Artificial  
Universidad Siglo 21  
Licenciatura en Informática 
Alumno: Julián Nicolás Ottonello Constantinidis  
Materia: Inteligencia Artificial  
Cuatrimestre: 1/25  
Docente: María Paula González  

---

Objetivo

Implementar y evaluar dos algoritmos de búsqueda en el espacio de estados (búsqueda exhaustiva y heurística) para resolver una situación problemática real en una línea de montaje automatizada de motores. El objetivo es dotar a un brazo robotizado de la autonomía necesaria para corregir pequeñas desviaciones en la posición de montaje, sin intervención humana.

---

Contenido del repositorio

| Archivo                          | Descripción |
|----------------------------------|-------------|
| `busqueda_exhaustiva_tp2.py`     | Implementación en Python de la búsqueda exhaustiva (alternancia izquierda/derecha) para encontrar la posición correcta de montaje. |
| `busqueda_heuristica_tp2.py`     | Implementación en Python de la búsqueda heurística (greedy) basada en una estimación de distancia hacia el objetivo. |

---

Cómo ejecutar los archivos

1. Asegurate de tener Python 3 instalado. Podés verificarlo con:
```bash
python --version
```

2. Cloná este repositorio o descargá los archivos `.py`.

3. Ejecutá cada archivo desde la terminal o desde un entorno como IDLE o VS Code:
```bash
python busqueda_exhaustiva_tp2.py
python busqueda_heuristica_tp2.py
```

Los resultados mostrarán el número de pasos necesarios para alcanzar la meta y un historial de las posiciones exploradas.

---

Enfoque didáctico

Este trabajo práctico forma parte del Módulo 2 de la materia Inteligencia Artificial. Aplica conceptos teóricos a una problemática realista mediante algoritmos simples pero efectivos, con el fin de desarrollar habilidades analíticas y de programación.

---
Referencias

 -Rich, E., & Knight, K. (1996). Inteligencia artificial. McGraw-Hill.
 -Russell, S., & Norvig, P. (2021). Inteligencia artificial: Un enfoque moderno (4.ª ed.). Pearson.
 -Nilsson, N. J. (1998). Inteligencia artificial: Una nueva síntesis. Morgan Kaufmann.
