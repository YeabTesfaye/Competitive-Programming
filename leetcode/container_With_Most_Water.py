
def container_With_Most_Water(height):
    
    #brute force with O(n^2) solution
    # maxArea = 0
    # for l in range(len(height)):
    #     for r in range(l + 1,  len(height)):
    #         area =(r-l)*min(height[l],height[r])
    #         maxArea = max(maxArea, area) 
    # return maxArea
    
    #effecent o(n) algorithm
    
    l,r = 0, len(height) - 1
    maxArea  = 0
    while l < r:
        area = (r-l)*min(height[l], height[r])
        maxArea = max(area,maxArea)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea
            




height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
result = (container_With_Most_Water(height))
print(result)