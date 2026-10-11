# Tarea 1 · Introducción a los métodos numéricos y entorno de trabajo.

UEA 1151039 · Métodos Numéricos en Ingeniería · Trimestre 26-O ·

---
| **Licenciatura** | Ingeniería en Computación |  
| --- | --- |
| **Nombre** | Christian Ali Najera Mayorga |
| **Matrícula** | 2252005719 |
| **Profesor** | Gabriel Hurtado Avilés |
| **Fecha** | 10 de octubre de 2026 |

---

## 1. ¿Qué son los métodos numéricos?

Los métodos numéricos son algoritmos que nos permiten resolver problemas matemáticos complejos utilizando operaciones aritméticas elementales (Chapra & Canale, 2015) y proporcionan soluciones cuantitativas aproximadas cuando no existe una fórmula exacta.

Debido a que solamente existen representaciones finitas de los números reales en la memoria, pueden surgir 2 tipos de errores (Kincaid & Cheney, 2012):

* **Error de redondeo:** Ocurre debido a que la computadora no puede almacenar dígitos significativos de manera ilimitada.
* **Error de truncamiento:** Surge al aproximar un proceso matemático infinito mediante un número finito de pasos.

---

## 2. ¿Cómo se aplican en la ingeniería en computación?

Son útiles en la optimización de la inteligencia artificial y *Machine Learning*, ya que las funciones de costo en el aprendizaje profundo involucran millones de parámetros acoplados. Es imposible despejar los parámetros analíticamente mediante álgebra tradicional, por lo que se emplean métodos numéricos de optimización basados en aproximación de derivadas (Nieves & Domínguez, 2014).

También pueden ser aplicados en la robótica en el cálculo de cinemática inversa y cálculo de posición, ya que están dadas por ecuaciones trigonométricas no lineales. Para que el robot pueda moverse en tiempo real, es necesario resolver el sistema numéricamente en cada instante de tiempo.

---

## 3. ¿Qué herramientas se usan para trabajar con métodos numéricos?

| Lenguajes compilados (C, C++, Fortran) | Lenguajes interpretados y entornos matriciales (Python, MATLAB, Octave) | Sistemas CAS y librerías (SymPy, BLAS/LAPACK) |
| --- | --- | --- |
| Alto rendimiento computacional y control directo de memoria. | Desarrollo rápido y tratamiento nativo de matrices (Quarteroni & Saleri, 2009). | Soluciones simbólicas exactas y rutinas optimizadas de álgebra lineal. |

* **Burden & Faires (2011):** Pseudocódigo, C, Fortran y MATLAB.
* **Chapra & Canale (2015):** VBA, MATLAB y C/C++.
* **Kincaid & Cheney (2012):** C, C++ y Fortran.
* **Nieves & Domínguez (2014):** Pseudocódigo y C/C++.
* **Quarteroni & Saleri (2009):** MATLAB y GNU Octave.

---

## 4. ¿Qué herramientas usamos en este curso?

*(Uso de una inteligencia artificial generativa (Gemini) para este apartado en comandos principales y entorno del contenedor).*

* **Docker:** Plataforma que empaqueta aplicaciones en entornos aislados e idénticos llamados contenedores.
* **Diferencia con una Máquina Virtual (VM):** Una VM virtualiza hardware y requiere un sistema operativo completo, mientras que Docker comparte el kernel del sistema operativo anfitrión, siendo mucho más ligero y rápido.
* **Ecosistema Docker:** Se configura mediante `Dockerfile` e instrucciones de orquestación en `compose.yaml`.

### Comandos principales:

* docker compose up -d --build: Construye la imagen e inicia el contenedor en segundo plano.
* docker compose ps: Revisa el estado del contenedor.
* docker compose exec bash: Inicia la terminal interactiva.
* docker compose stop: Apaga el contenedor conservando sus datos.
* docker compose down: Elimina el contenedor y la red creada.
* docker compose logs: Muestra la bitácora de procesos.

*Diferencia apagar vs. borrar:* `stop` pausa el contenedor; `down` elimina la instancia por completo.

### Entorno del contenedor:

* **GNU Octave:** Versión 7.3.0 (Cálculo matricial).
* **Python:** Versión 3.11.2 (Librerías científicas y prototipado).
* **GCC (C):** Versión 12.2.0 (Compilación de alto desempeño).

---

## Referencias bibliograficas

* Burden, R. L., & Faires, J. D. (2011). *Análisis Numérico* (9a ed.). Cengage Learning.
* Chapra, S. C., & Canale, R. P. (2015). *Métodos Numéricos para Ingenieros* (7a ed.). McGraw-Hill.
* Kincaid, D., & Cheney, W. (2012). *Análisis Numérico y Computación* (6a ed.). Cengage Learning.
* Nieves, A., & Domínguez, F. C. (2014). *Métodos Numéricos Aplicados a la Ingeniería*. Grupo Editorial Patria.
* Quarteroni, A., & Saleri, F. (2009). *Cálculo Científico con MATLAB y Octave*. Springer.
