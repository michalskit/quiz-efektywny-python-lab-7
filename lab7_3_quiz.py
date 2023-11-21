# Napisz dekorator @TotalExecutionTime, który mierzy i sumuje czas wykonania
# każdego wywołania dekorowanej funkcji. Dekorator powinien posiadać metodę
# get_total_execution_time(), która zwraca łączny czas wszystkich wykonanych
# dotychczas wywołań funkcji.

import time

def TotalExecutionTime(func):
    pass


# Testowanie dekoratora
@TotalExecutionTime
def some_heavy_computation(a, b):
    time.sleep(a * b)
    return a * b

# Wywołanie funkcji
some_heavy_computation(1, 2)
some_heavy_computation(2, 3)

# Sprawdzenie sumy czasów wykonania
total_time = some_heavy_computation.get_total_execution_time()
print(total_time)  # Zwraca łączny czas wykonania dwóch wywołań funkcji.
