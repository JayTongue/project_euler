def triange(n):
    return int((n*(n+1))/2)

def pentagonal(n):
    return int((n*(3*n-1))/2)

def hexagonal(n):
    return int(n*(2*n-1))

limit = int(5e5)
triangles = set(triange(n) for n in range(limit))
pentagons = set(pentagonal(n) for n in range(limit))
hexagons = set(hexagonal(n) for n in range(limit))

print(triangles.intersection(pentagons, hexagons))