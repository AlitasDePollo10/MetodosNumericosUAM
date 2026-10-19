import math

# =====================================================================
# ECUACIÓN 7: Computación · Entrada n log2(n) con 10^6 operaciones
# =====================================================================
OPS7 = 1000000.0
A7, B7 = 10000.0, 100000.0
X0_7 = 50000.0
DELTA7 = 1.0
TOL7 = 0.5

def f7(x):
    return x * math.log2(x) - OPS7

def fp7(x):
    return math.log2(x) + 1.0 / math.log(2)

def g7(x):
    return OPS7 / math.log2(x)


# =====================================================================
# ECUACIÓN 8: Trazado de Rayos · Intersección con Cubo Redondeado
# =====================================================================
OX, OY, OZ = -2.0, -0.6, -0.8
DX, DY, DZ = 0.8, 0.36, 0.48
A8, B8 = 0.0, 1.5
X0_8 = 0.5
DELTA8 = 0.01
TOL8 = 0.5

def f8(x):
    return (OX + DX*x)**4 + (OY + DY*x)**4 + (OZ + DZ*x)**4 - 1.0

def fp8(x):
    return 4*DX*(OX + DX*x)**3 + 4*DY*(OY + DY*x)**3 + 4*DZ*(OZ + DZ*x)**3

def g8(x):
    return x + f8(x) / 4.0


# =====================================================================
# ECUACIÓN 9: Canal Binario Simétrico · Capacidad de 0.5 bits
# =====================================================================
CAP = 0.5
A9, B9 = 0.01, 0.4
X0_9 = 0.2
DELTA9 = 0.001
TOL9 = 0.5

def f9(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x) - (1 - CAP)

def fp9(x):
    return math.log2(1 - x) - math.log2(x)

def g9(x):
    return (1 - CAP + (1 - x) * math.log2(1 - x)) / (-math.log2(x))


# =====================================================================
# MÉTODOS NUMÉRICOS
# =====================================================================
def biseccion(f, a, b, tol, nmax=50):
    x_old = None
    print(f"{'i':>3} | {'a':>12} | {'b':>12} | {'xr':>12} | {'f(xr)':>12} | {'ea (%)':>10}")
    print("-" * 72)
    for i in range(1, nmax + 1):
        xr = (a + b) / 2.0
        ea = abs((xr - x_old) / xr) * 100.0 if x_old is not None else 100.0
        print(f"{i:3d} | {a:12.6f} | {b:12.6f} | {xr:12.6f} | {f(xr):12.6f} | {ea:10.4f}")
        if ea < tol and i > 1:
            break
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
        x_old = xr

def falsa_posicion(f, a, b, tol, nmax=50):
    x_old = None
    print(f"{'i':>3} | {'a':>12} | {'b':>12} | {'xr':>12} | {'f(xr)':>12} | {'ea (%)':>10}")
    print("-" * 72)
    for i in range(1, nmax + 1):
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        ea = abs((xr - x_old) / xr) * 100.0 if x_old is not None else 100.0
        print(f"{i:3d} | {a:12.6f} | {b:12.6f} | {xr:12.6f} | {f(xr):12.6f} | {ea:10.4f}")
        if ea < tol and i > 1:
            break
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
        x_old = xr

def punto_fijo(g, f, x0, tol, nmax=50):
    x = x0
    print(f"{'i':>3} | {'x_i':>12} | {'x_{i+1}':>12} | {'f(x_{i+1})':>12} | {'ea (%)':>10}")
    print("-" * 62)
    for i in range(1, nmax + 1):
        x_next = g(x)
        ea = abs((x_next - x) / x_next) * 100.0
        print(f"{i:3d} | {x:12.6f} | {x_next:12.6f} | {f(x_next):12.6f} | {ea:10.4f}")
        if ea < tol:
            break
        x = x_next

def newton_raphson(f, fp, x0, tol, nmax=50):
    x = x0
    print(f"{'i':>3} | {'x_i':>12} | {'x_{i+1}':>12} | {'f(x_{i+1})':>12} | {'ea (%)':>10}")
    print("-" * 62)
    for i in range(1, nmax + 1):
        x_next = x - f(x) / fp(x)
        ea = abs((x_next - x) / x_next) * 100.0
        print(f"{i:3d} | {x:12.6f} | {x_next:12.6f} | {f(x_next):12.6f} | {ea:10.4f}")
        if ea < tol:
            break
        x = x_next

def secante_modificada(f, x0, delta, tol, nmax=50):
    x = x0
    print(f"{'i':>3} | {'x_i':>12} | {'x_{i+1}':>12} | {'f(x_{i+1})':>12} | {'ea (%)':>10}")
    print("-" * 62)
    for i in range(1, nmax + 1):
        df = f(x + delta) - f(x)
        x_next = x - (delta * f(x)) / df
        ea = abs((x_next - x) / x_next) * 100.0
        print(f"{i:3d} | {x:12.6f} | {x_next:12.6f} | {f(x_next):12.6f} | {ea:10.4f}")
        if ea < tol:
            break
        x = x_next


# =====================================================================
# EJECUCIÓN PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    print("\n================ ECUACIÓN 7 (Newton-Raphson) ================")
    newton_raphson(f7, fp7, X0_7, TOL7)

    print("\n================ ECUACIÓN 8 (Bisección) ================")
    biseccion(f8, A8, B8, TOL8)

    print("\n================ ECUACIÓN 9 (Punto Fijo) ================")
    punto_fijo(g9, f9, X0_9, TOL9)