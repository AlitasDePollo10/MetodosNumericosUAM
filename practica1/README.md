# Práctica 1 · La serie de Maclaurin y el criterio de paro

**UEA 1151039 · Métodos Numéricos en Ingeniería · Trimestre 26-O · UAM Azcapotzalco**
**Profesor:** M. en C. Gabriel Hurtado Avilés

| Equipo | |
| --- |---|
| Integrantes (nombre y matrícula) | Christian Ali Najera Mayorga, 2252005719 |
| Licenciatura | Ingeniería en Computación |
| Repositorio de la Tarea 1 de | Christian Ali Najera Mayorga|
| Fecha | 12 de octubre de 2026 |


### Tabla 1. Valores de aproximación y error verdadero con 6 y 17 cifras.

| Cifras | Criterio de Scarborough | Términos necesarios | Aproximación | Error verdadero | 
| ----- | ----- | ----- | ----- | ----- | 
| 6 | 0.0005% | 9 | 1.648721265035962 | 3.43549e-07% | 
| 17 | 5X10^-14% | 16 | 1.648721270700128 | 2.69354e-14% | 


*Figura 1. Ejecución con 6 cifras significativas.*
<img width="1409" height="490" alt="Captura de pantalla 2026-10-12 185349" src="https://github.com/user-attachments/assets/8555498f-ba63-4922-9c73-a4d001b3cd50" />

*Figura 2. Ejecución con 17 cifras significativas.*
<img width="1639" height="559" alt="Captura de pantalla 2026-10-12 185647" src="https://github.com/user-attachments/assets/36fcde4c-fc41-4c1f-88e0-1125caf4d615" />


### 1.- ¿Cuántos términos hacen falta con 3, 6 y 17 cifras?

Con 3 cifras hacen falta 6 términos ($n = 6$).

Con 6 cifras faltan 9 términos ($n = 9$).

Con 17 cifras faltan 16 términos ($n = 16$).

### 2.- En cada fila, ¿$e_a$ es mayor o menor que $e_t$? ¿Por qué conviene detenerse con $e_a$?

En cada una de las ejecuciones puede observarse que $e_a$ es mayor que $e_t$. Y la razón por la cual conviene detenerse es porque en diversos problemas reales de ingeniería el valor de una función es desconocido y por ello es imposible calcular un error verdadero de manera 100% efectiva. Aquí aplicamos el criterio de paro (Chapra & Canale, 2015) que se fundamenta con la regla de Scarborough y el error aproximado.

### 3.- Con 17 cifras el programa termina. ¿Cuántas cifras del resultado son correctas en realidad? Relaciónenlo con $0.1 + 0.2$ de la Tarea 1.

El programa (Figura 2) nos muestra que en realidad son correctas de 15 a 16 cifras significativas, esto debido a que existe una limitación en el almacenamiento de entre 15 y 17 dígitos en memoria. Por ejemplo, vemos que con 16 cifras las cifras son tan pequeñas que no se altera el valor acumulado, por lo que el error aproximado es de prácticamente 0%. El programa termina no porque sean 17 cifras exactas, sino porque se alcanzó el límite de redondeo.

Por otro lado, $0.1 + 0.2 = 0.30000000000000004$ porque la memoria guarda los números en binario, no en base 10.
## Referencias
* Chapra, S. C., & Canale, R. P. (2015). Métodos Numéricos para Ingenieros (7a ed.). McGraw-Hill. Capítulo 3,
ejemplo 3.2, y capítulo 4.
* Burden, R. L., & Faires, J. D. (2011). Análisis Numérico (9a ed.). Cengage Learning. Capítulo 1.
