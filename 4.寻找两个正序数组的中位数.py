#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l == 1:return nums1[0] if len(nums1) == 1 else nums2[0]
        a = -1
        b = -1
        dic = {}
        for i in range(int(l/2)+1):
            if a<(len(nums1)-1) and b<(len(nums2)-1):
                if nums1[a+1]<=nums2[b+1]:
                    a+=1
                    dic[i] = nums1[a]
                elif nums1[a+1]>nums2[b+1]: 
                    b+=1
                    dic[i] = nums2[b]
            else:
                if a == len(nums1)-1:
                    b+=1
                    dic[i] = nums2[b]
                elif b== len(nums2)-1:
                    a+=1
                    dic[i] = nums1[a]
        if l%2 == 1:
            return dic[int(l/2)]
        else:
            return float(dic[int(l/2)]+dic[int(l/2)-1])/2

# @lc code=end
print(Solution().findMedianSortedArrays([1,2],[3,4]))
