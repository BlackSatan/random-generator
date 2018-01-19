import os
import math
import random


def multiplicatives(x, a, c, m):
    return (a * x + c) % m


def multiplicativer(x, a, c, m):
    return (multiplicatives(x, a, c, m)) / float(m)


def wichmannhill(lastr):  # lastr = [r, s1, s2, s3]
    s1 = multiplicatives(lastr[1], 171, 0, 30269)
    s2 = multiplicatives(lastr[2], 172, 0, 30307)
    s3 = multiplicatives(lastr[3], 170, 0, 30323)
    r = (float(s1) / 30269 + float(s2) / 30307 + float(s3) / 30323) % 1
    return [r, s1, s2, s3]


def seq_multiplicative(n, a, c, m):  # return array of randoms
    rseq = []
    x = 5
    for i in range(1, n):
        x = multiplicativer(x, a, c, m)
        rseq.append(x)
    return rseq


def seq_wichmannhill(n):  # return array of randoms
    rseq = []
    rsarr = [0, 5, 4, 3]
    for i in range(1, n):
        rsarr = wichmannhill(rsarr)
        rseq.append(rsarr[0])
    return rseq


def memory_usage(times):
    import psutil
    process = psutil.Process(os.getpid())
    result = []
    for i in range(times):
        u_t = process.cpu_times().user
        c_t = process.cpu_times().system
        num = (to_0_1_range(u_t, 100000) + to_0_1_range(c_t, 1000)) % 1 if simple_test() > .5 else abs((to_0_1_range(u_t, 10000) - to_0_1_range(c_t, 10))) % 1
        result.append(num)
    return result


def to_0_1_range(u_t, power):
    return (u_t * power) % 1


def simple_test():
    return random.random()
