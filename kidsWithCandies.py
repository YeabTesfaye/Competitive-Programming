def kidsWithCandies(candies, extraCandies: int):
    

    return [c+ extraCandies >= max(candies) for c in candies]


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))