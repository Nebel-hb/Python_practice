import sys
with open(sys.argv[1], 'r', encoding='utf_8') as file:
    count = 1
    for line in file:
        print('{0:03d} {1}'.format(count, line), end='')
        count += 1
