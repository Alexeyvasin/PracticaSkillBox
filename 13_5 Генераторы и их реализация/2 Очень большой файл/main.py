def gen_read_file(path_to_file):
    with open(path_to_file) as f_hand:
        for line in f_hand:
            numbers = line.strip().split()
            for number in numbers:
                yield float(number)


gen_numbers = gen_read_file('numbers.txt')
print(sum(gen_numbers))
