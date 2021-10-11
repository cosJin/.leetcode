class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch (arr, l, r, x): 
            if r >= l: 
                mid = int(l + (r - l)/2)
                if arr[mid] == x: 
                    return mid 
                elif arr[mid] > x: 
                    return binarySearch(arr, l, mid-1, x) 
                else: 
                    return binarySearch(arr, mid+1, r, x) 
            else: 
                return -1
        start = binarySearch(nums,0,len(nums)-1,target)
        if start == -1: return 0
        if start != 0:
            while(nums[start-1] == target):
                start = start-1
                if start == 0:break
        result = 1
        if (start!=len(nums)-1):
            while(nums[start+1]==target):
                start += 1
                result += 1
                if start==len(nums)-1:break
        return result

    #    优秀范例：
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(target):
            i,j = 0,len(nums)-1
            while i<=j:
                mid = (i+j)//2
                if nums[mid] <= target:
                    i = mid+1
                else:
                    j = mid-1
            return i 
        return(helper(target)-helper(target-1))

    def helper(nums,target):
            i,j = 0,len(nums)-1
            while i<=j:
                mid = (i+j)//2
                if nums[mid] <= target:
                    i = mid+1
                else:
                    j = mid-1
            return i             
print(Solution.helper([0,1,2,3,4],4))



