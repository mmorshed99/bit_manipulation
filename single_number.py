#Given an array of integers, every element appears twice except for one. Find that single one.
#
#Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#Example :
#
#Input : [1 2 2 3 1]
#Output : 3
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 0:
            return 0
        temp = 0
        for i in range(0,len(A)):
            temp = temp ^ A[i]
        return temp
