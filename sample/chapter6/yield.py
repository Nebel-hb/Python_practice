def fizzbuzz(n):
    for x in range(1, n):
        if x % 15 == 0:
            yield 'FizzBuzz'
        elif x % 5 == 0:
            yield 'Buzz'
        elif x % 3 == 0:
            yield 'Fizz'
        else:
            yield x


print(list(fizzbuzz(16)))
