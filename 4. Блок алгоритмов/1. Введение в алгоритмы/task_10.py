def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def get_least_primes(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or x > n:
                break
            lp[x] = p
    return primes


def factorization(n):
    if is_prime(n):
        return n
    primes = get_least_primes(int(n**0.5))
    result = []
    while True:
        updated = False
        if n == 1:
            result = map(int, result)
            result = sorted(result)
            result = map(str, result)
            return ' '.join(result)
        for prime in primes:
            if n % prime == 0:
                n = n // prime
                result.append(str(prime))
                updated = True
        if not updated:
            result.append(str(n))
            result = map(int, result)
            result = sorted(result)
            result = map(str, result)
            return ' '.join(result)


def main():
    n = int(input())
    result = factorization(n)
    print(result, end='')


if __name__ == '__main__':
    main()
