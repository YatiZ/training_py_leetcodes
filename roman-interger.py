#constraints 
# only 4, 9 start smallest to largest (left to right)
# others are written largest to smallest 

class Solution:
   
    def romanToInt(self, s: str):
        romanObj =  {'I': 1, 'V': 5, 'IV': 4,'IX': 9, 'X': 10,'XL': 40, 'L': 50,'XC': 90, 'C': 100,'CD': 400, 'D': 500,'CM': 900, 'M': 1000}
        
        numbers = 0
        i =0

        while i < len(s):
            if i+1 <len(s) and s [i:i+ 2] in romanObj:
                numbers += romanObj[s[i:i+ 2]]  #substring 
                i+=2
            else:
                numbers += romanObj[s[i]]
                i+=1
        return numbers
       
        
    def intToRoman(self, i: int):
        roman_obj = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ""

        for value, romanNum in  roman_obj.items():
            while i >= value:
                result += romanNum
                i -= value
        return result
            

solution_instance = Solution()
print(solution_instance.romanToInt(s = "III"))
print(solution_instance.romanToInt(s = "LVIII"))
print(solution_instance.romanToInt("MCMXCIV"))
print(solution_instance.intToRoman(i = 40))