from fractions import Fraction

longer_count = 0
def run_frac(n):
    result, longer = Fraction(1, 2), False
    for _ in range(n):
        result = Fraction(1, 2+ result)
    result += 1
    if len(list(str(result.numerator))) > len(list(str(result.denominator))):
        longer = True
    return longer

for i in range(1, int(1e3) + 1):
    longer = run_frac(i)
    if longer:
        longer_count += 1
print(longer_count)
