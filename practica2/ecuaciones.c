#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NMAX 50

/* =====================================================================
 * ECUACIÓN 7: Computación · Entrada n log2(n) con 10^6 operaciones
 * ===================================================================== */
static const double OPS7 = 1000000.0;
static const double A7 = 10000.0, B7 = 100000.0;
static const double X0_7 = 50000.0;
static const double DELTA7 = 1.0;
static const double TOL7 = 0.5;

static double f7(double x) {
    return x * log2(x) - OPS7;
}

static double fp7(double x) {
    return log2(x) + 1.0 / log(2.0);
}

static double g7(double x) {
    return OPS7 / log2(x);
}

/* =====================================================================
 * ECUACIÓN 8: Trazado de Rayos · Intersección con Cubo Redondeado
 * ===================================================================== */
static const double OX = -2.0, OY = -0.6, OZ = -0.8;
static const double DX = 0.8, DY = 0.36, DZ = 0.48;
static const double A8 = 0.0, B8 = 1.5;
static const double X0_8 = 0.5;
static const double DELTA8 = 0.01;
static const double TOL8 = 0.5;

static double f8(double x) {
    double t1 = OX + DX * x;
    double t2 = OY + DY * x;
    double t3 = OZ + DZ * x;
    return (t1*t1*t1*t1) + (t2*t2*t2*t2) + (t3*t3*t3*t3) - 1.0;
}

static double fp8(double x) {
    double t1 = OX + DX * x;
    double t2 = OY + DY * x;
    double t3 = OZ + DZ * x;
    return 4.0*DX*(t1*t1*t1) + 4.0*DY*(t2*t2*t2) + 4.0*DZ*(t3*t3*t3);
}

static double g8(double x) {
    return x + f8(x) / 4.0;
}

/* =====================================================================
 * ECUACIÓN 9: Canal Binario Simétrico · Capacidad de 0.5 bits
 * ===================================================================== */
static const double CAP = 0.5;
static const double A9 = 0.01, B9 = 0.4;
static const double X0_9 = 0.2;
static const double DELTA9 = 0.001;
static const double TOL9 = 0.5;

static double f9(double x) {
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x) - (1.0 - CAP);
}

static double fp9(double x) {
    return log2(1.0 - x) - log2(x);
}

static double g9(double x) {
    return (1.0 - CAP + (1.0 - x) * log2(1.0 - x)) / (-log2(x));
}

/* =====================================================================
 * MÉTODOS NUMÉRICOS
 * ===================================================================== */
void biseccion(double (*f)(double), double a, double b, double tol, int nmax) {
    double x_old = 0.0;
    double xr = 0.0, ea = 100.0;

    printf("%3s | %12s | %12s | %12s | %12s | %10s\n", "i", "a", "b", "xr", "f(xr)", "ea (%)");
    printf("------------------------------------------------------------------------\n");

    for (int i = 1; i <= nmax; i++) {
        xr = (a + b) / 2.0;
        if (i > 1) {
            ea = fabs((xr - x_old) / xr) * 100.0;
        }

        printf("%3d | %12.6f | %12.6f | %12.6f | %12.6f | %10.4f\n", i, a, b, xr, f(xr), ea);

        if (ea < tol && i > 1) {
            break;
        }

        if (f(a) * f(xr) < 0) {
            b = xr;
        } else {
            a = xr;
        }
        x_old = xr;
    }
}

void punto_fijo(double (*g)(double), double (*f)(double), double x0, double tol, int nmax) {
    double x = x0;
    double x_next = 0.0, ea = 0.0;

    printf("%3s | %12s | %12s | %12s | %10s\n", "i", "x_i", "x_{i+1}", "f(x_{i+1})", "ea (%)");
    printf("--------------------------------------------------------------\n");

    for (int i = 1; i <= nmax; i++) {
        x_next = g(x);
        ea = fabs((x_next - x) / x_next) * 100.0;

        printf("%3d | %12.6f | %12.6f | %12.6f | %10.4f\n", i, x, x_next, f(x_next), ea);

        if (ea < tol) {
            break;
        }
        x = x_next;
    }
}

void newton_raphson(double (*f)(double), double (*fp)(double), double x0, double tol, int nmax) {
    double x = x0;
    double x_next = 0.0, ea = 0.0;

    printf("%3s | %12s | %12s | %12s | %10s\n", "i", "x_i", "x_{i+1}", "f(x_{i+1})", "ea (%)");
    printf("--------------------------------------------------------------\n");

    for (int i = 1; i <= nmax; i++) {
        x_next = x - f(x) / fp(x);
        ea = fabs((x_next - x) / x_next) * 100.0;

        printf("%3d | %12.6f | %12.6f | %12.6f | %10.4f\n", i, x, x_next, f(x_next), ea);

        if (ea < tol) {
            break;
        }
        x = x_next;
    }
}

/* =====================================================================
 * MAIN
 * ===================================================================== */
int main(void) {
    printf("\n================ ECUACIÓN 7 (Newton-Raphson) ================\n");
    newton_raphson(f7, fp7, X0_7, TOL7, NMAX);

    printf("\n================ ECUACIÓN 8 (Bisección) ================\n");
    biseccion(f8, A8, B8, TOL8, NMAX);

    printf("\n================ ECUACIÓN 9 (Punto Fijo) ================\n");
    punto_fijo(g9, f9, X0_9, TOL9, NMAX);

    return 0;
}
