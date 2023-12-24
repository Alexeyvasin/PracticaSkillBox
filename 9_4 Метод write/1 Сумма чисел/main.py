
with open('numbers.txt', 'r') as file:
    sum_from_f = 0
    for i_num in file:
        i_num = i_num.strip()
        if i_num.isdigit():
            sum_from_f += int(i_num)
with open('answer.txt', 'w') as file:
    file.write(str(sum_from_f))