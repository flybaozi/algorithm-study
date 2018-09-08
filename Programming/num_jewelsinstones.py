# leetcode 771 宝石与石头
class Solution(object):
    def numjewelsinstones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        list_j = list(J)
        list_s = list(S)
        num = 0
        for i in range(len(list_j)):
            while list_j[i] in list_s:
                list_s.remove(list_j[i])
                num = num + 1
            else:
                continue
        return num
