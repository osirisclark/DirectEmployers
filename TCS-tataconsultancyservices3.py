"""
Write a program that prints the numbers from 1 to 100. But for multiples of three
print “FIZZ” instead of the number and for the multiples of five print “BUZZ”.
For numbers which are multiples of both three and five print “FIZZBUZZ”.
3 FIZZ , 5 BUZZ,  3 and 5 FIZZ_BUZZ.
"""

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(x, 'FIZZ_BUZZ')
    elif x % 3 == 0:
        print(x, 'FIZZ')
    elif x % 5 == 0:
        print(x, 'BUZZ')

    else:
        print(x)


"""
Using  List Comprehensions
"""

print([(x, 'FIZZ_BUZZ') if x % 3 == 0 and x % 5 == 0 else (x, 'FIZZ')
      if x % 3 == 0 else (x, 'BUZZ') if x % 5 == 0 else x for x in
      range(1, 101)]
      )
