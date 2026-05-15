from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        q = deque()
        result = []
        
        for i in range(len(arr)):
            
            # Add negative elements index
            if arr[i] < 0:
                q.append(i)
            
            # Remove elements outside window
            if q and q[0] <= i - k:
                q.popleft()
            
            # Window formed
            if i >= k - 1:
                if q:
                    result.append(arr[q[0]])
                else:
                    result.append(0)
        
        return result