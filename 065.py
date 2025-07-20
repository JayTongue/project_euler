from fractions import Fraction

def continued_fraction_e_terms(n):
    """Generate the first n terms of the continued fraction for e."""
    terms = [2]
    k = 1
    while len(terms) < n:
        terms += [1, 2*k, 1]
        k += 1
    return terms[:n]

def convergents(cf_terms):
    """Generate convergents from continued fraction terms."""
    p0, p1 = 0, 1
    q0, q1 = 1, 0
    convergents_list = []

    for a in cf_terms:
        p = a * p1 + p0
        q = a * q1 + q0
        convergents_list.append(Fraction(p, q))
        p0, p1 = p1, p
        q0, q1 = q1, q

    return convergents_list


terms = continued_fraction_e_terms(100)
convs = convergents(terms)


for i, frac in enumerate(convs):
    print(sum(map(int, list(str(frac.numerator)))))