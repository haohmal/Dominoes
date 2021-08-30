sum = 0
i = 0
while True:
    number = input()
    if number == '.':
        break
    sum += int(number)
    i += 1

print(sum / i)
