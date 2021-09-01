#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_dic = {}
        for n,i in enumerate(nums):
            if tmp_dic.get(target-i) is not None:
                return [n,tmp_dic[target-i]]
            else:tmp_dic[i] = n
        return []
        
        
# @lc code=end

a = Solution()
print(a.twoSum([2,7,8],9))