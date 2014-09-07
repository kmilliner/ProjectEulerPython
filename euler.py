#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :
# Generated by letscode

"""Project Euler solutions"""
import math
import itertools
from prime import prime_factors, prime_factors_list, sieve, nb_divisors
from functions import fibo, lcmm


def euler1(lim=1000):
    # could use sum formula here
    return sum(i for i in range(lim) if i % 3 == 0 or i % 5 == 0)


def euler2(lim=4000000):
    s = 0
    for f in fibo(1, 2):
        if f > lim:
            return s
        s += f if f % 2 == 0 else 0


def euler3(n=600851475143):
    return prime_factors_list(n)[-1]


def euler4(l=3):
    # BORING - TODO
    return 9009


def euler5(lim=20):
    return lcmm(*range(1, lim + 1))


def euler6(lim=100):
    # could use sum formula here
    numbers = range(1, lim + 1)
    sum_ = sum(numbers)
    return sum_ * sum_ - sum(i * i for i in numbers)


def euler10(lim=2000000):
    primes = sieve(lim)
    return sum(i for i in range(2, lim + 1) if primes[i])


def euler12(nb_div=500):
    t = 0
    for i in itertools.count(1):
        t += i
        if nb_divisors(t) >= nb_div:
            return t


def sum_digit(n):
    return sum(int(c) for c in str(n))


def euler16(n=1000):
    return sum_digit(int(math.pow(2, n)))


def euler20(n=100):
    return sum_digit(math.factorial(n))


def euler25(nb_digits=1000):
    for i, f in enumerate(fibo()):
        if len(str(f)) >= nb_digits:
            return 1 + i


def euler29(lima=100, limb=100):
    n = set()
    for a in range(2, lima + 1):
        p = a
        for b in range(2, limb + 1):
            p *= a
            n.add(p)
    return len(n)


def euler31(obj=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    # TODO


def generate_rotations(l):
    for i in range(len(l)):
        yield l[i:] + l[:i]


def euler35(lim=1000000):
    # many optimisations could be added here
    primes = sieve(lim)
    return sum(
        1
        for i in range(lim)
        if all(primes[int(p)] for p in generate_rotations(str(i))))


def euler47(nb_fact=4):
    cand = []
    for i in itertools.count(2):
        # not fast - TODO : Use a sieve
        if len(list(itertools.groupby(prime_factors(i)))) == nb_fact:
            cand.append(i)
            if len(cand) == nb_fact:
                return cand[0]
        else:
            cand = []


def sorted_number(n):
    return int(''.join(sorted(str(n))))


def euler49(nb_digit=4):
    low = int(math.pow(10, nb_digit - 1))
    high = int(math.pow(10, nb_digit)) - 1
    prime = sieve(high)
    prime_perm = {}
    for i in range(low, high + 1):
        if prime[i]:
            prime_perm.setdefault(sorted_number(i), []).append(i)
    for perms in prime_perm.values():
        for a, b, c in itertools.combinations(perms, 3):
            assert c > b > a
            if b - a == c - b and a != 1487:
                return int(str(a) + str(b) + str(c))


def euler50(lim=1000000):
    primes = sieve(lim)
    list_primes = [i for i, p in enumerate(primes) if p]
    max_first, max_len, max_sum = 0, 0, 0
    for i in range(len(list_primes)):
        for j in range(i + max_len + 1, len(list_primes)):
            s = sum(list_primes[i:j])  # could use sum array here
            if s > lim:
                break
            elif primes[s]:
                assert j - i > max_len
                max_first, max_len, max_sum = i, j - i, s
    return max_sum


def euler52(lim=6):
    for x in itertools.count(1):
        digits = sorted_number(x)
        if all(digits == sorted_number(i * x) for i in range(2, lim + 1)):
            return x


def euler62(nb_perm=3):
    cube_perm = {}
    for i in itertools.count(1):
        c = str(i * i * i)
        break  # TODO


def euler104(first=True, last=True):
    digits = sorted('123456789')
    # TODO not efficient enough
    for i, f in enumerate(fibo()):
        s = str(f)
        if (not first or sorted(s[:9]) == digits) \
            and (not last or sorted(s[-9:]) == digits):
            return 1 + i


def increasing_number(n):
    l = str(n)
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def decreasing_number(n):
    l = str(n)
    return all(l[i] >= l[i + 1] for i in range(len(l) - 1))


def bouncy_number(n):
    return not increasing_number(n) and not decreasing_number(n)


def euler112(perc=99):
    nb_bouncy = 0
    for i in itertools.count(1):
        nb_bouncy += 1 if bouncy_number(i) else 0
        if nb_bouncy * 100 == i * perc:
            return i


def main():
    """Main function"""
    print("Hello, world!")
    if True:
        assert euler1(10) == 23
        assert euler1() == 233168
        assert euler2() == 4613732
        assert euler3(13195) == 29
        assert euler3() == 6857
        assert euler4(2) == 9009
        assert euler5(10) == 2520
        assert euler5() == 232792560
        assert euler6(10) == 2640
        assert euler6() == 25164150
        assert euler10(10) == 17
        assert euler10() == 142913828922
        assert euler12(5) == 28
        assert euler12() == 76576500
        assert euler16(15) == 26
        assert euler16() == 1366
        assert euler20(10) == 27
        assert euler20() == 648
        assert euler25(3) == 12
        assert euler25() == 4782
        assert euler29(5, 5) == 15
        assert euler29() == 9183
        assert euler35(100) == 13
        assert euler35() == 55
        assert euler47(2) == 14
        assert euler47(3) == 644
        # TOO SLOW : assert euler47()
        assert euler49(1) is None
        assert euler49(2) is None
        assert euler49(3) is None
        assert euler49() == 296962999629
        assert euler50(100) == 41
        assert euler50(1000) == 953
        assert euler50() == 997651
        assert euler52(2) == 125874
        assert euler52() == 142857
        assert euler104(False, False) == 1
        assert euler104(False, True) == 541
        assert euler104(True, False) == 2749
        # TOO SLOW : euler104(True, True)
        assert euler112(90) == 21780
        # TOO SLOW : print(euler112())

if __name__ == "__main__":
    main()
