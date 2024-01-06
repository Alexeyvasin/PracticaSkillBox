def gen(to_max):
    x = 2
    while True:
        if x > to_max:
            return
        if x == 2 or x == 3:
            yield x
            x += 1
        else:
            x += 1 if not x % 2 else 2
            for div in range(3, x // 2, 2):
                if not x % div:
                    break
            else:
                if x > to_max:
                    return
                yield x


prime_num = gen(11234567)

for i in prime_num:
    print(i)
