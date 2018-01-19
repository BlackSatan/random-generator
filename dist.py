import math


def norm_dist(x_seq):
    i = 0
    result = []
    max_index = len(x_seq) - 1
    while i < max_index:
        new_i = min(max_index, i + 12)
        result.append(sum(x_seq[i:new_i]) / 12)
        i = new_i
    return result


def exp_dist(x, lambd):
    return -math.log(x) / float(lambd)


def veib_dist(x, k, alpha):
    return [(
        (- math.log(i) / alpha) ** k
    ) for i in x]
