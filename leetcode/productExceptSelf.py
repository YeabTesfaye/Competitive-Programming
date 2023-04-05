

def productExceptSelf(nums):
    res = [1]*len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
    #bruet force 
    # leftProduct = 1
    # rightProduct = 1
    # productNums = []
    # for i in range(len(nums)):
    #     lefti = i
        
    #     while True:
    #         lefti -= 1
    #         if lefti < 0:
    #             break
    #         else:
    #             leftProduct *= nums[lefti]
    #     righti = i 
    #     while True:
    #         righti += 1
    #         if righti >= len(nums):
    #             break
    #         else:
    #             rightProduct *= nums[righti]
    #     productNums.append(rightProduct*leftProduct)
    #     leftProduct = 1
    #     rightProduct = 1
    # return productNums
    
    
    

nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
