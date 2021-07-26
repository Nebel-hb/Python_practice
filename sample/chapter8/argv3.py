import sys
total = 0
for price in sys.argv[1:]:
    total += int(price)
print('合計', total, '円')
