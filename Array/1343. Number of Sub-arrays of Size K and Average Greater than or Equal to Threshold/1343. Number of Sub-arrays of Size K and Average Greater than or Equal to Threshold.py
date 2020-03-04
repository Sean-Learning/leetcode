class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        #print(arr)
        #arr.sort()
        # 0 1 2 3 4
        # 2 4 6 8 13 18
        #     6 6 9
        #Prefix Sum:
        threshold*=k
        ans=0
        '''
        arr.insert(0,0)
        for i in range(k):
            print(arr)
            arr[i] +=arr[i-1]
        for i in range(k,len(arr)):
            print(arr)
            arr[i] +=arr[i-1]
            if (arr[i]-arr[i-k]) >= threshold:
                ans+=1
        '''
        
        #sliding window
        low, window = -1, 0
        for high, value in enumerate(arr):
            #print(arr)
            window += value
            if high - low == k: #when the high is far enough from low
                if window >= threshold:
                    ans += 1
                low += 1  #low starting to walk
                window -= arr[low]
            #print(high,low,window,value,end=" ")
            #print(" ")
        return ans