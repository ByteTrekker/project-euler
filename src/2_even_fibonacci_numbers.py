a, b = 0, 1

fib_sum = 0
even_sum = 0

while fib_sum < 4000000:
    fib_sum += a
    a, b = b, a + b

    if b % 2 == 0:
        even_sum += b

print(even_sum)