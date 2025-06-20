# To run the file, simply call "python [Filename].py" by using the "cmd Terminal".

# -------------------------------------------------------------------------------------------------------------------------------

# Climbing Stairs Problem:
# You are climbing a staircase. It takes 'n' steps to reach the top.
# Each time you can either climb '1' or '2' steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        # Base cases:
        # if n <= 2:
            # return n
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # return self.climbStairs(n - 2) + self.climbStairs(n - 1)          # Recursive approach (not efficient for large n)

        two_back = 1
        one_back = 2
        for i in range(3, n + 1):
            ret = two_back + one_back
            two_back = one_back
            one_back = ret
        
        return ret
        """
        :type n: int
        :rtype: int
        """

# -------------------------------------------------------------------------------------------------------------------------------