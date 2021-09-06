#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row = -1
        col = 1
        res = []
        to = -1
        if numRows==1:return s
        for n,i in enumerate(s):
            if col >= 0 and col <= numRows-1:
                col += to
                if to == -1:
                    res.append(['']*numRows)
                    row += 1
            res[row][col] = i
            if col == 0 or col == numRows-1: 
                to = (0-to)
        output=""
        for i in range(numRows):
            for j in range(len(res)):
                output+=res[j][i]
        return output
class Solution2(object):    #直接分成 numrows堆，往返将s的元素加到每一堆中，最后直接按顺序输出每一堆即可，巧妙
                            #不需要先写成矩阵再按特定顺序去读取了
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        a =  ["" for _ in range(numRows)]

        flag = 0
        j = 0
        for i in s:
            a[j] += i

            if j == 0:
                flag = 0
            if j == numRows - 1:
                flag = 1

            if(flag == 0):
                j += 1
            else:
                j -= 1


        return "".join(a)


# @lc code=end
print(Solution2().convert('PAYPALISHIRING',3))