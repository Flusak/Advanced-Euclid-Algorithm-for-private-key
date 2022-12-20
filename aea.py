#Advanced Euclid Algorithm for private key
def CalcD(x, m):
    u = (x, 1)
    v = (m, 0)
    while v[0] != 0:
        q = u[0] // v[0]
        t = (u[0] % v[0], u[1] - q * v[1])
        u = v
        v = t
    if u[0] != 1: return 0
    return u[1] % m
