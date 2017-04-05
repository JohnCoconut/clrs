from math import log2, log10, sqrt, pow, modf, lgamma
import math

us = 1
s = 10 ** 6 * us
m = 60 * s
h = 60 * m
d = 24 * h
m = 30 * d
y = 365 * d
c = 100 * y

times = [s, m ,h, d, m, y, c]

def lgn(times):
    res = []
    for t in times:
        f, i = modf(t * log10(2))
        sci_notation = "{:.1f}e+{:.0f}".format(10**f, i)
        res.append(sci_notation)
    return res

def sqrtn(times):
    times = [t ** 2 for t in times]
    return ["{:.1e}".format(t) for t in times]

def n(times):
    return ["{:.1e}".format(t) for t in times]

def nlgn(times):
    '''
    nlgn = t. for large t, n is around t/lgt 
    set lower bound to t/lgt
    set upper bound to t
    '''
    res = []
    for t in times:
        l = t / log2(t)
        r = t
        while (r - l) / t >= 10 ** -3:
            mid = (l + r) / 2
            if mid * log2(mid) < t:
                l = mid
            else:
                r = mid
        res.append(mid)
    return ["{:.1e}".format(t) for t in res]
        

def nsqure(times):
    times = [sqrt(t) for t in times]
    return ["{:.1e}".format(t) for t in times]

def ncubic(times):
    times = [t ** (1/3) for t in times]
    return ["{:.1e}".format(t) for t in times]

def two_pow_n(times):
    times = [log2(t) for t in times]
    return ["{:.1e}".format(t) for t in times]

def factorial_n(times):
    res = []
    for t in times:
        if not res:
            i = 1
        else:
            i = res[-1]
        product = 1
        while product <= t:
            product *= i
            i += 1
        res.append(i-1)
    return ["{}".format(t) for t in res]


func = [lgn, sqrtn, n, nlgn, nsqure, ncubic, two_pow_n, factorial_n]

if __name__ == "__main__":
    for f in func:
        f_name = "{:15}".format(f.__name__)
        print(f_name , f(times))
