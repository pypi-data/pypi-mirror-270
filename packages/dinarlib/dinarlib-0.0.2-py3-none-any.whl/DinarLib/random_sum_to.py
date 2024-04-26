from random import *
def random_sum(n, num_terms = None):
    num_terms = (num_terms or random.randint(2, n)) - 1
    a = random.sample(range(1, abs(n)), num_terms) + [0, abs(n)]
    list.sort(a)
    return [a[i+1] - a[i] for i in range(len(a) - 1)]