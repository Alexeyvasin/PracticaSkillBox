import time


def gen(to_max):
    x = 2
    while True:
        for div in range(3, x // 2, 2):
            if not x % div:
                break
        else:
            if x > to_max:
                return
            yield x
        x += 1 if not x % 2 else 2


start = time.time()
primes = gen(111678)
for i in primes:
    print(i)
print(time.time() - start)
