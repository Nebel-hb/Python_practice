number = ['1', '2', 'three', '4']
sum = 0
for n in number:
    try:
        sum += int(n)
    except ValueError:
        pass
print(sum)
