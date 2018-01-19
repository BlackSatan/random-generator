from matplotlib import pyplot as plt
import tests
import dist
import generators


def draw_hist(_rseq, _title):
    plt.title(_title)
    plt.hist(_rseq)
    plt.show()

rseq = generators.seq_multiplicative(1000,  2 ** 31 - 1, 0, 630360016)
# rseq = generators.seq_wichmannhill(100)

print('Random sequence', rseq)
print('Period tests result is', tests.period_test(rseq, 34))
print('Frequency tests result is', tests.frequency_test(rseq))
print('Moment result is', tests.moment_test(rseq))

r_rexp = [dist.exp_dist(rseq[i], lambd=5) for i in range (0, len(rseq)-1)]
print('Exponential sequence', r_rexp)
draw_hist(r_rexp, 'Експоненційний розподіл')

r_norm = dist.norm_dist(rseq)
print('Normal sequence', r_norm)
draw_hist(r_norm, 'Нормальний розподіл')

r_veib = dist.veib_dist(rseq, alpha=1, k=1.5)
print('Weibull sequence', r_veib)
draw_hist(r_veib, 'Розподіл Вейбулла')
