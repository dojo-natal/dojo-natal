# https://leetcode.com/problems/palindrome-number/
import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        ex = math.log(x, 10)

        numero_algarismos = int(math.ceil(ex)


        for i in range(numero_algarismos, 0, -1):
            print(i)

        return ex

                