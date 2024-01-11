class Solution:
    def isPalindrome(self, x: int):
        number = x
        reversed_number = 0
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x = x // 10

        isPalindrome = number == reversed_number and len(
            str(number)) == len(str(reversed_number))
        print(isPalindrome)


solution_instance = Solution()
solution_instance.isPalindrome(x=121)
