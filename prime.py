#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Functions related to prime numbers decomposition in prime factors."""
import math
import collections
import itertools
import operator
import functools


def mult(iterable, start=1):
    """Returns the product of an iterable - like the sum builtin."""
    return functools.reduce(operator.mul, iterable, start)


def prime_factors(n):
    """Yields prime factors of a positive number."""
    assert n > 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            yield d
        d += 1
    if n > 1:  # to avoid 1 as a factor
        assert d <= n
        yield n


def prime_factors_list(n):
    """Returns the prime factors of a positive number as a list."""
    l = list(prime_factors(n))
    assert mult(l) == n
    return l


def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    return all(n % i for i in range(2, int(math.sqrt(n)) + 1))


def yield_primes(beg=0):
    """Yields prime number by checking them individually - not efficient."""
    for i in itertools.count(beg):
        if is_prime(i):
            yield i


def sieve(lim):
    """Computes the sieve of Eratosthenes for values up to lim included."""
    primes = [True] * (lim + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(lim)) + 1):
        if primes[i]:
            for j in range(i * i, lim + 1, i):
                primes[j] = False
    return primes


def divisors_sieve(lim):
    """Computes the list of divisors for values up to lim included."""
    div = [[1] for i in range(lim + 1)]
    for i in range(2, 1 + lim // 2):
        for j in range(2 * i, lim + 1, i):
            div[j].append(i)
    return div


def prime_divisors_sieve(lim):
    """Computes the list of prime divisors for values up to lim included."""
    # Pretty similar to totient
    div = [set() for i in range(lim + 1)]
    for i in range(2, lim + 1):
        if not div[i]:
            for j in range(i, lim + 1, i):
                div[j].add(i)
    return div


def totient(lim):
    """Computes Euler's totient for values up to lim included."""
    # http://en.wikipedia.org/wiki/Euler%27s_totient_function
    tot = list(range(lim + 1))
    tot[0] = -1
    for i in range(2, lim + 1):
        if tot[i] == i:
            for j in range(i, lim + 1, i):
                tot[j] = (tot[j] * (i - 1)) // i
    return tot


def primes_up_to(lim):
    """Uses a sieve to return primes up to lim included."""
    return (i for i, p in enumerate(sieve(lim)) if p)


def yield_divisors_using_primes_factorisation(n):
    """Yields distinct divisors of n.

    This uses the prime factorisation to generate the different divisors.
    It is faster than yield_divisors_using_divisions on most big inputs
    but the complexity is hard to guarantee on all inputs and it is slower
    on small inputs."""
    elements = ([p**power for power in range(c + 1)]
                for p, c
                in collections.Counter(prime_factors(n)).items())
    return (mult(it) for it in itertools.product(*elements))


def yield_divisors_using_divisions(n):
    """Yields distinct divisors of n.

    This uses sucessive divisions so it can be slower than
    yield_divisors_using_primes_factorisation on big inputs but it is easier
    to understand, the upper bound of O(sqrt(n)) is guarantee and faster on
    small inputs."""
    assert n > 0
    yield 1
    if n > 1:
        yield n
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                j = n // i
                yield i
                if i != j:
                    yield j


def yield_divisors(n):
    """Yields distinct divisors of n."""
    return yield_divisors_using_primes_factorisation(n)


def nb_divisors(n):
    """Returns the number of divisors of n."""
    return mult(c + 1
                for c in collections.Counter(
                    prime_factors(n)).values())


def nb_prime_divisors(n):
    """Returns the number of prime divisors of n."""
    return len(list(itertools.groupby(prime_factors(n))))


def main():
    limit = 1000
    primes = list(primes_up_to(limit))
    primes2 = []
    for p in yield_primes():
        if p > limit:
            break
        primes2.append(p)
    assert primes == primes2

    prime_set = set(primes)

    def test_divisors_func(n):
        nb_prime_div = nb_prime_divisors(n)
        nb_div = nb_divisors(n)
        assert 0 <= nb_prime_div <= nb_div
        prime_div = prime_factors_list(n)
        divisors1 = sorted(yield_divisors_using_primes_factorisation(n))
        divisors2 = sorted(yield_divisors_using_divisions(n))
        assert nb_div == len(divisors1)
        assert divisors1 == divisors2
        assert 1 in divisors1
        assert n in divisors1
        assert all(p in divisors1 for p in prime_div)
        if n in prime_set:
            assert nb_prime_div == 1
            assert nb_div == 2
            assert prime_div == [n]
            assert divisors1 == [1, n]
        elif n == 1:
            assert nb_prime_div == 0
            assert nb_div == 1
            assert prime_div == []
            assert divisors1 == [1]
        else:
            assert nb_prime_div >= 1
            assert nb_div >= 3

    for n in range(1, limit):
        test_divisors_func(n)


if __name__ == "__main__":
    main()
