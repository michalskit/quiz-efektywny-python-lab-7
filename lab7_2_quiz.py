# Napisz generator perfect_numbers() bez żadnych argumentów,
# który generuje kolejne liczby doskonałe. Liczba doskonała to taka,
# która jest równa sumie wszystkich swoich dzielników właściwych
# (tj. wszystkich dzielników oprócz samej siebie).
# Na przykład, 6 jest liczbą doskonałą (1 + 2 + 3 = 6).

def perfect_numbers():
    """Generator function for perfect numbers."""
    pass

def is_perfect(number):
    """Check if a number is perfect."""
    pass

# Testing the generator function
gen = perfect_numbers()
perfects = [next(gen) for _ in range(3)]
print(perfects == [6, 28, 496])
