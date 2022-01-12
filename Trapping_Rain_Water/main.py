class Solution:
    def trap(height):
        water = 0
        dic = {}
        for i, order in enumerate(height):
            dic[i] = order
        max_height = max(dic.values())
        current_max = 0
        current_max_t = 0
        
        for i in dic:
            if dic[i] < current_max:
                water += current_max - dic[i]
            
            
            
            if dic[i] > current_max:
                current_max = dic[i]
                
            if dic[i] == max_height:
                break
            
        for j in range(len(dic)-1, 0, -1):     
            if dic[j] > current_max_t:
                current_max_t = dic[j]
            
            if dic[j] < current_max_t:
                water += current_max_t - dic[j]
            
            if j == i : break
            
            
        return water
    
    print(trap([4,2,0,3,2,5]))