from itertools import pairwise, chain


def canPlaceFlowers(flowerbed, n: int):

    a = 0
    for b, c in pairwise(chain(flowerbed, (0,))):
        k = a == b == c == 0
        a = 1 if k else b
        if n <= 0:
            return True
        n -= k
    return n <= 0


# Input: flowerbed = [1,0,0,0,1], n = 1
# Input: flowerbed = [1,0,0,0,1], n = 2
''' 
The purpose of adding the trailing 0 is to ensure that the last element
of the flowerbed list is paired with a 0 in the iteration. This is because the loop
in the code uses consecutive pairs of elements (b and c) to determine if there
is an empty spot for placing a flower. By adding 
the trailing 0, the loop can consider the last element of flowerbed in the iteration.
'''

flowerbed = [0, 0, 1, 0, 1]
flowerbed = [1, 0,0,0,1]

print(canPlaceFlowers(flowerbed, 2))
