class Solution:
    def getMinMax(self, arr):
        min=float("inf")
        max=float("-inf")
        for i in range(len(arr)):
            if arr[i]<min:
                min=arr[i]
            if arr[i]>max:
                max=arr[i]
        return [min,max]
            
        
   
        