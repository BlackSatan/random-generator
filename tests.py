import math


def moment_test(rseq):
    disp = 0
    avg = sum(rseq) / float(len(rseq))
    for i in range(0, len(rseq)):
        disp = math.pow(rseq[i] - avg, 2)
    disp /= float(len(rseq))
    z1 = avg - 0.5
    z2 = disp - 1.0 / 12
    t1 = math.sqrt(12 * len(rseq)) * abs(z1)
    t2 = ((len(rseq) - 1) / float(10 * len(rseq))) * float(abs(z2)) / math.sqrt(
        0.0056 * math.pow(len(rseq), -1) + 0.0028 * math.pow(len(rseq), -2) - 0.0083 * math.pow(len(rseq), -3))
    return t1 >= 1.67 and t2 >= 1.67


def period_test(rseq, n):
    for i in range(0, len(rseq) - n):
        for j in range(0, i):
            if rseq[i:(i + n)] == rseq[j:(j + n)]:
                return False
    return True


def frequency_test(rseq):
    count = 0
    for i in range(0, len(rseq)):
        if rseq[i] >= 0.2113 and rseq[i] <= 0.7887:
            count += 1
    count /= float(len(rseq))
    return count <= 0.5874 and count >= 0.5674
