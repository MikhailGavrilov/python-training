cubs = []
for val in (range(1, 1000, 2)):
    cubs.append(val ** 3)
#print(cubs)

b = []
sum1 = 0
for num in cubs:
    i = num
    while num != 0:
        sum1 += num % 10
        num = num // 10
    if sum1 % 7 == 0:
        b.append(i)
    sum1 = 0
print(sum(b))

sum_num_plus = 0
for num in cubs:
    summ = 0
    i = num
    num += 17
    while num != 0:
        summ += num % 10
        num = num // 10
    if summ % 7 == 0:
        sum_num_plus += i
print (sum_num_plus)

