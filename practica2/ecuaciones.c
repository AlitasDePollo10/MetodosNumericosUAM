#include <math.h>

/* ===================================================================== */
/* SELECCIÓN DE ECUACIÓN                                                 */
/* Cambia el número a 7, 8 o 9 para elegir la ecuación a procesar:      */
/* ===================================================================== */
#ifndef ECUACION
#define ECUACION 7   /* Valor por defecto: 7, 8 o 9 */
#endif


#if ECUACION == 7
/* ======================== ECUACIÓN 7 ======================== */
/* Entrada que un algoritmo n log₂ n procesa con 10⁶ operaciones */

#define DESCRIPCION "f(n) = n log2(n) - 1e6"
#define DESCR_G     "g(n) = 1e6 / log2(n)"

static const double OPS = 1000000.0;
static const double A = 10000.0, B = 100000.0;
static const double X0    = 50000.0;
static const double DELTA = 1.0;
static const double TOL   = 0.5;
#define NMAX 50

static double f(double x) {
    return x * log2(x) - OPS;
}

static double fp(double x) {
    return log2(x) + 1.0 / log(2.0);
}

static double g(double x) {
    return OPS / log2(x);
}


#elif ECUACION == 8
/* ======================== ECUACIÓN 8 ======================== */
/* Trazado de rayos: dónde choca un rayo con un cubo redondeado */

#define DESCRIPCION "f(t) = X^4 + Y^4 + Z^4 - 1"
#define DESCR_G     "g(t) = t + f(t) / 4"

static const double OX = -2.0, OY = -0.6, OZ = -0.8;
static const double DX = 0.8, DY = 0.36, DZ = 0.48;

static const double A = 0.0, B = 1.5;
static const double X0    = 0.5;
static const double DELTA = 0.01;
static const double TOL   = 0.5;
#define NMAX 50

static double f(double x) {
    return (OX + DX*x)*(OX + DX*x)*(OX + DX*x)*(OX + DX*x) +
           (OY + DY*x)*(OY + DY*x)*(OY + DY*x)*(OY + DY*x) +
           (OZ + DZ*x)*(OZ + DZ*x)*(OZ + DZ*x)*(OZ + DZ*x) - 1.0;
}

static double fp(double x) {
    return 4.0*DX*(OX + DX*x)*(OX + DX*x)*(OX + DX*x) +
           4.0*DY*(OY + DY*x)*(OY + DY*x)*(OY + DY*x) +
           4.0*DZ*(OZ + DZ*x)*(OZ + DZ*x)*(OZ + DZ*x);
}

static double g(double x) {
    return x + f(x) / 4.0;
}


#elif ECUACION == 9
/* ======================== ECUACIÓN 9 ======================== */
/* Canal binario simétrico: probabilidad de error con capacidad de 0.5 */

#define DESCRIPCION "f(p) = -p log2(p) - (1-p) log2(1-p) - 0.5"
#define DESCR_G     "g(p) = (1 - C + (1 - p) log2(1 - p)) / (-log2(p))"

static const double CAP = 0.5;

static const double A = 0.01, B = 0.4;
static const double X0    = 0.2;
static const double DELTA = 0.001;
static const double TOL   = 0.5;
#define NMAX 50

static double f(double x) {
    return -x*log2(x) - (1.0 - x)*log2(1.0 - x) - (1.0 - CAP);
}

static double fp(double x) {
    return log2(1.0 - x) - log2(x);
}

static double g(double x) {
    return (1.0 - CAP + (1.0 - x)*log2(1.0 - x)) / (-log2(x));
}

#endif
