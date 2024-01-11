class Solution:
    def isPalindrome(self,x:int):
       
        listForReverse = str(x)
        reversedLists = listForReverse[::-1]
        print(reversedLists)
        if x > 0:
            if x == int(reversedLists):
                print(True)
            else:
                print(False)
        elif listForReverse[0] == '-':
            print(False)

            
solution_instance = Solution()
solution_instance.isPalindrome(x=-121)
  
