def find_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes
n_value = int(input("Enter the value of N: "))
result = find_n_primes(n_value)
print(f"The first {n_value} prime numbers are:")
print(*(result))