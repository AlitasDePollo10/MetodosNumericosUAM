import math

# =====================================================================
# MÉTODOS NUMÉRICOS REUTILIZABLES
# =====================================================================

def resolver_metodos(f, fp, g, A, B, X0, DELTA, TOL, NMAX):
    """Ejecuta los 5 métodos numéricos para el bloque actual."""
    
    print("\nBISECCIÓN")
    print(f"{'Iter':<6}{'a':<14}{'b':<14}{'xr':<14}{'ea (%)':<12}")
    print("-" * 60)
    a, b, xr_old = A, B, 0.0
    for i in range(1, NMAX + 1):
        xr = (a + b) / 2.0
        ea = abs((xr - xr_old) / xr) * 100.0 if i > 1 else 100.0
        print(f"{i:<6}{a:<14.6f}{b:<14.6f}{xr:<14.6f}{ea:<12.4f}")
        if ea <= TOL and i > 1:
            break
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
        xr_old = xr

    print("\nREGULA FALSI")
    print(f"{'Iter':<6}{'a':<14}{'b':<14}{'xr':<14}{'ea (%)':<12}")
    print("-" * 60)
    a, b, xr_old = A, B, 0.0
    for i in range(1, NMAX + 1):
        fa, fb = f(a), f(b)
        xr = b - (fb * (a - b)) / (fa - fb)
        ea = abs((xr - xr_old) / xr) * 100.0 if i > 1 else 100.0
        print(f"{i:<6}{a:<14.6f}{b:<14.6f}{xr:<14.6f}{ea:<12.4f}")
        if ea <= TOL and i > 1:
            break
        if fa * f(xr) < 0:
            b = xr
        else:
            a = xr
        xr_old = xr

    print("\nPUNTO FIJO")
    print(f"{'Iter':<6}{'xi':<14}{'xi+1':<14}{'ea (%)':<12}")
    print("-" * 46)
    xi = X0
    for i in range(1, NMAX + 1):
        try:
            xi1 = g(xi)
        except Exception as e:
            print(f"Divergencia/Error en Punto Fijo: {e}")
            break
        ea = abs((xi1 - xi) / xi1) * 100.0 if xi1 != 0 else 0.0
        print(f"{i:<6}{xi:<14.6f}{xi1:<14.6f}{ea:<12.4f}")
        if ea <= TOL:
            break
        xi = xi1

    print("\nNEWTON-RAPHSON")
    print(f"{'Iter':<6}{'xi':<14}{'xi+1':<14}{'ea (%)':<12}")
    print("-" * 46)
    xi = X0
    for i in range(1, NMAX + 1):
        f_val, fp_val = f(xi), fp(xi)
        if fp_val == 0:
            print("Error: Derivada nula.")
            break
        xi1 = xi - f_val / fp_val
        ea = abs((xi1 - xi) / xi1) * 100.0 if xi1 != 0 else 0.0
        print(f"{i:<6}{xi:<14.6f}{xi1:<14.6f}{ea:<12.4f}")
        if ea <= TOL:
            break
        xi = xi1

    print("\nSECANTE MODIFICADA")
    print(f"{'Iter':<6}{'xi':<14}{'xi+1':<14}{'ea (%)':<12}")
    print("-" * 46)
    xi = X0
    for i in range(1, NMAX + 1):
        f_val = f(xi)
        f_delta = f(xi + DELTA * xi)
        denom = f_delta - f_val
        if denom == 0:
            print("Error: Divisor nulo.")
            break
        xi1 = xi - (DELTA * xi * f_val) / denom
        ea = abs((xi1 - xi) / xi1) * 100.0 if xi1 != 0 else 0.0
        print(f"{i:<6}{xi:<14.6f}{xi1:<14.6f}{ea:<12.4f}")
        if ea <= TOL:
            break
        xi = xi1

# ======================== BLOQUE DEL PROBLEMA ========================
# Ecuación 7 · Computación · Entrada que un algoritmo n log₂ n procesa con 10⁶ operaciones

DESCRIPCION = 'f(n) = n log2(n) - 1e6'
DESCR_G = 'g(n) = 1e6 / log2(n)'

OPS = 1000000.0   # operaciones disponibles

A, B = 10000.0, 100000.0   # intervalo de los métodos cerrados
X0 = 50000.0         # inicio de los métodos abiertos
DELTA = 1.0      # incremento de la secante modificada
TOL = 0.5           # tolerancia: ea en %
NMAX = 50           # máximo de iteraciones


def f(x):
    """La función cuya raíz se busca."""
    return x*math.log2(x) - OPS


def fp(x):
    """Su derivada, para Newton-Raphson."""
    return math.log2(x) + 1/math.log(2)


def g(x):
    """Despeje x = g(x) para punto fijo."""
    return OPS/math.log2(x)

# =====================================================================

print("\n======================================================================")
print(f"Ecuación 7 · Computación · Entrada que un algoritmo n log₂ n procesa con 10⁶ operaciones")
print("======================================================================")
resolver_metodos(f, fp, g, A, B, X0, DELTA, TOL, NMAX)


# ======================== BLOQUE DEL PROBLEMA ========================
# Ecuación 8 · Computación · Trazado de rayos: dónde choca un rayo con un cubo redondeado

DESCRIPCION = 'f(t) = X^4 + Y^4 + Z^4 - 1,  (X, Y, Z) = (-2, -0.6, -0.8) + t (0.8, 0.36, 0.48)'
DESCR_G = 'g(t) = t + f(t) / 4'

OX = -2.0   # origen del rayo
OY = -0.6
OZ = -0.8
DX = 0.8   # dirección del rayo, unitaria
DY = 0.36
DZ = 0.48

A, B = 0.0, 1.5   # intervalo de los métodos cerrados
X0 = 0.5         # inicio de los métodos abiertos
DELTA = 0.01      # incremento de la secante modificada
TOL = 0.5           # tolerancia: ea en %
NMAX = 50           # máximo de iteraciones


def f(x):
    """La función cuya raíz se busca."""
    return (OX + DX*x)*(OX + DX*x)*(OX + DX*x)*(OX + DX*x) + (OY + DY*x)*(OY + DY*x)*(OY + DY*x)*(OY + DY*x) + (OZ + DZ*x)*(OZ + DZ*x)*(OZ + DZ*x)*(OZ + DZ*x) - 1


def fp(x):
    """Su derivada, para Newton-Raphson."""
    return 4*DX*(OX + DX*x)*(OX + DX*x)*(OX + DX*x) + 4*DY*(OY + DY*x)*(OY + DY*x)*(OY + DY*x) + 4*DZ*(OZ + DZ*x)*(OZ + DZ*x)*(OZ + DZ*x)


def g(x):
    """Despeje x = g(x) para punto fijo."""
    return x + f(x)/4

# =====================================================================

print("\n======================================================================")
print(f"Ecuación 8 · Computación · Trazado de rayos: dónde choca un rayo con un cubo redondeado")
print("======================================================================")
resolver_metodos(f, fp, g, A, B, X0, DELTA, TOL, NMAX)


# ======================== BLOQUE DEL PROBLEMA ========================
# Ecuación 9 · Computación · Canal binario simétrico: probabilidad de error con capacidad de 0.5 bits

DESCRIPCION = 'f(p) = -p log2(p) - (1 - p) log2(1 - p) - (1 - C),  C = 0.5'
DESCR_G = 'g(p) = (1 - C + (1 - p) log2(1 - p)) / (-log2(p))'

CAP = 0.5   # capacidad del canal, bits por uso

A, B = 0.01, 0.4   # intervalo de los métodos cerrados
X0 = 0.2         # inicio de los métodos abiertos
DELTA = 0.001      # incremento de la secante modificada
TOL = 0.5           # tolerancia: ea en %
NMAX = 50           # máximo de iteraciones


def f(x):
    """La función cuya raíz se busca."""
    return -x*math.log2(x) - (1 - x)*math.log2(1 - x) - (1 - CAP)


def fp(x):
    """Su derivada, para Newton-Raphson."""
    return math.log2(1 - x) - math.log2(x)


def g(x):
    """Despeje x = g(x) para punto fijo."""
    return (1 - CAP + (1 - x)*math.log2(1 - x))/(-math.log2(x))

# =====================================================================

print("\n======================================================================")
print(f"Ecuación 9 · Computación · Canal binario simétrico: probabilidad de error con capacidad de 0.5 bits")
print("======================================================================")
resolver_metodos(f, fp, g, A, B, X0, DELTA, TOL, NMAX)