#-*- coding:utf-8 -*-
#########################################################################
# File Name: twoSum.py
# Author: Shen Bo
# mail: nichol_shen@yahoo.com
# Created Time: Wed, Mar 21, 2018  8:12:47 PM
#########################################################################
#!usr/bin/env python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            rList = []
            delt = target - nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    if nums[j] == delt:
                        rList.append(i)
                        rList.append(j)
                        return rList
        return 'Not Found'

    def twoSumD(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                return [res[nums[i]], i]
            else:
                res[target - nums[i]] = i
                




if '__main__' == __name__:

    arry = [1, 2, 5, 4, 3, 0]
    target = 9
    s = Solution()

    print('answer:', s.twoSum(arry, target))
    print('answer:', s.twoSumD(arry, target))
