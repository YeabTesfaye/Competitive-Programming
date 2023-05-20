from itertools import pairwise, chain

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        a = 0
        for b, c in pairwise(chain(flowerbed, (0,))):
            k = a == b == c == 0
            a = 1 if k else b
            if n <= 0: return True
            n -= k
        return n <= 0


        


''' 
The purpose of adding the trailing 0 is to ensure that the last element
of the flowerbed list is paired with a 0 in the iteration. This is because the loop
in the code uses consecutive pairs of elements (b and c) to determine if there
is an empty spot for placing a flower. By adding 
the trailing 0, the loop can consider the last element of flowerbed in the iteration.
'''

