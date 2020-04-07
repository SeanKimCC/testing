def search(nums, target):
        
        N = len(nums)
        if(N == 0):
            return -1
        
        
        leftMost = 0
        rightMost = N - 1
        mid = (rightMost - leftMost) // 2
        
        while(leftMost < rightMost):
            print(leftMost, rightMost)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                leftMost = mid + 1
            else: # elif(nums[mid] > target)
                rightMost = mid - 1
                
            mid = (rightMost + leftMost) // 2
        
        
        return -1

#print (search([-1,0,3,5,9,12], 9))


def bubbleSort(nums):
    N = len(nums)
    
    for j in range(0, N-1):
        for i in range(0,N-1):
            print(nums)
            if(nums[i] > nums[i+1]):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

bubbleSort([4,8,7,2,3,1])
O(N^2)



O(N * log(N))


Merge sort

nums.sort()


Quicksort


[-1,0,3,5,9,12]












        
