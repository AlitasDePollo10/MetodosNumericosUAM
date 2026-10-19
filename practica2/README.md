# Práctica 2 · Raíces de ecuaciones no lineales

**UEA 1151039 · Métodos Numéricos en Ingeniería · Trimestre 26-O · UAM Azcapotzalco**
**Profesor:** M. en C. Gabriel Hurtado Avilés

| Equipo | |
|---|---|
| Integrantes | Christian Ali Najera Mayorga |
| Matricula | 2252005719 |
| Ecuación asignada | 7, 8 y 9 (Computación)|
| Fecha | 16 de octubre de 2026|

---

## 1. Octave y Python con el paracaidista

<img width="1920" height="1140" alt="02-python" src="https://github.com/user-attachments/assets/8d2cc1a7-1866-412e-82cd-03192ea11325" />
<img width="1920" height="1140" alt="01-octave" src="https://github.com/user-attachments/assets/1996af31-f1ba-4dd1-8572-0437bae2e9de" />


## 2. Las cinco líneas que completamos en `raices.c`
<img width="1920" height="1140" alt="03-c-compilacion" src="https://github.com/user-attachments/assets/4202739c-8926-46af-9be4-c6e6b915dd8d" />
<img width="1920" height="1140" alt="04-c-ejecucion" src="https://github.com/user-attachments/assets/29c8dc4b-995a-4283-802a-6b6bf09557f8" />


¿Coinciden las tablas de C con las de Octave y Python? Sí / No, y en qué.
Si coinciden debido a que presentan los mismos valores de gravedad, masa, tiempo y velocidad, solo cambia el lenguaje de programación en el que
se esta ejecutando.

## 3. Las gráficas de Python

<img width="2400" height="1500" alt="convergencia" src="https://github.com/user-attachments/assets/1c4eb73d-d64c-4bdb-bdc5-066a3f48d138" />
<img width="2400" height="1500" alt="funcion" src="https://github.com/user-attachments/assets/4b433632-44f1-4e41-b8b1-8e35d3b19142" />

## 4. Nuestra ecuación

<img width="1920" height="1140" alt="05-c-ecuaciones" src="https://github.com/user-attachments/assets/d8ca2100-9c60-47d7-9842-6453c0cd35cd" />
<img width="1920" height="1140" alt="06-python-ecuacion" src="https://github.com/user-attachments/assets/a38824d4-2c69-4322-8e31-5227c2325c10" />


### Tablas (salida de C)
(Obtenidas de 26-O_1151039_Unidad_II_Raices_de_ecuaciones.pdf)

#### Bisección

| k | a | b | x | f(x) | εa (%) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 12.000000 | 16.000000 | 14.000000 | 1.568699e+00 | — |
| 2 | 14.000000 | 16.000000 | 15.000000 | -4.248409e-01 | 6.6667 |
| 3 | 14.000000 | 15.000000 | 14.500000 | 5.523185e-01 | 3.4483 |
| 4 | 14.500000 | 15.000000 |14.750000 | 5.895351e-02 | 1.6949 |
| 5 | 14.750000 | 15.000000 | 14.875000 | -1.841257e-01 | 0.8403 |
| 6 | 14.7500000 | 14.875000 | 14.812500 | -6.288337e-02 | 0.4219 |

#### Falsa posición

| k | a | b | x | f(x) | εa (%) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 12.000000 | 16.000000 | 14.911303 | -2.542778e-01 | — |
| 2 | 12.000000 | 14.911303 | 14.794193 | -2.725719e-02 | 0.7916 |
| 3 | 12.000000 | 14.794193 | 14.781695 | -2.907592e-03 | 0.0845 |

#### Punto fijo

| k | x | f(x) | εa (%) |
| :-: | :-: | :-: | :-: |
| 0 | 12.500000 | 4.873138e+00 | — |
| 1 | 14.022855 | 1.521357e+00 | 10.8598 |
| 2 | 14.556200 | 4.405649e-01 | 3.6640 |
| 3 | 14.716523 | 1.244581e-01 | 1.0894 |
| 4 | 14.762313 | 3.490305e-02 | 0.3102 |

#### Newton-Raphson

| k | x | f(x) | εa (%) |
| :-: | :-: | :-: | :-: |
| 0 | 12.500000 | 4.873138e+00 | — |
| 1 | 14.583293 | 3.868663e-01 | 14.2855 |
| 2 | 14.778690 | 2.951832e-03 | 1.3222 |
| 3 | 14.780204 | 1.749853e-07 | 0.0102 |

#### Secante modificada

| k | x | f(x) | εa (%) |
| :-: | :-: | :-: | :-: |
| 0 | 12.500000 | 4.873138e+00 | — |
| 1 | 14.587538 | 3.784618e-01 | 14.3104 |
| 2 | 14.779130 | 2.093380e-03 | 1.2964 |
| 3 | 14.780206 | -4.011741e-06 | 0.0073 |

#### Resumen

| Método | Raíz | Iteraciones | εa (%) | f(raíz) | Error verdadero (%) |
| :--- | :-: | :-: | :-: | :-: | :-: |
| **Bisección** | 14.812500 | 6 | 0.2794% | 0.4219 | -6.288337e-02 |
| **Falsa posición** | 14.781695 | 3 | 0.0539% | 0.0845 | -2.907592e-03 |
| **Punto fijo** | 14.762313 | 4 | 0.2046% | 0.3102 | 3.490305e-02 |
| **Newton-Raphson** | 14.780204 | 3 | 0.2025% | 0.0102 | 1.749853e-07 |
| **Secante modificada** | 14.780206 | 3 | 0.2025% | 0.0073 | -4.011741e-06 |

### Análisis
¿Qué método necesitó menos iteraciones y cuál más? ¿Por qué los cinco no dan
exactamente el mismo número? ¿Alguno no alcanzó la tolerancia o tardó mucho más que
los otros? ¿Por qué?
* El que menos interaciones tuvo fue Newton-Raphson, Falsa posición y Secante modificada con 3 interacciones cada una.
* Los cinco no dan exactamente el mismo resultado debido al crtierio de paro por error aproximado y a la velocidad de 
convergencia de cada algortimo.
* Todos alcanzaron la tolerancia del 0.5% en donde la bisección fue la que tardó mucho más que los otros.

## 5. Cada integrante en su computadora
La práctica se realizó de manera individual.
 
## Uso de inteligencia artificial

Se utilizó inteligencia artificial generativa (Gemini) para la compilación y ejecucion 
de los programas "ecuaciones.py" y "ecuaciones.c" debido a que el codigo por si solo no 
mostraba ningún resultado al momento de invocarlo a través de la ventana de comandos.

