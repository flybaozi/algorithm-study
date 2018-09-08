class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        new_list = []
        for i in A:
            new_list.append([1 - val for val in i[::-1]])
        return new_list
