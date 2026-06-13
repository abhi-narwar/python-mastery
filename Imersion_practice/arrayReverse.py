class Solution:
    def reverseArray(self, arr):
        i=0
        n=len(arr)-1
        
        
        while i<n:
            arr[i],arr[n]=arr[n],arr[i]
            i+=1
            n-=1
        
            
            
        
            
        
        