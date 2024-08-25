#palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        cleared_numbers  = []
        number = str(x)
        for num in number:
            if num:
                cleared_numbers.append(num)
        cleaned_integer = ''.join(cleared_numbers)

        if cleaned_integer == cleaned_integer[::-1]:
            return True
        return False
    
#add- binary
class Solution:
    def addBinary(self, a: str, b: str):
        if a.isnumeric() and b.isnumeric():
            a = int(a,2)
            b = int(b,2)
            result = a + b
            binary_value = bin(result)[2:]
            return binary_value

#Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dict = {}
        unique = [] 
        for num in arr:
            if num in dict:
                dict[num] +=1
            else:
                dict[num] = 1

        for key in dict.keys():
            unique.append(dict[key])

        if len(set(unique)) == len(unique):
            return True
        return False

#Third Maximum Number
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)
        if len(sorted_nums) < 3:
            return max(sorted_nums)
        else:
            return sorted_nums[2]

# Move Zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for num in range(len(nums)):
            if nums[num] !=0:
                nums[left], nums[num] = nums[num],nums[left]
                left +=1
        return nums

# Detect Capital
def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 0:
            return False

        elif word.isupper():
            return True

        elif word.islower():
            return True
        
        elif word[0:].isupper() or word[1:].islower():
            return True
        return False

# Power of 4
def isPowerOfFour(self, n: int) -> bool:
    if n <= 0:
        return False
    while n % 4 == 0:
        n = n / 4
    return n == 1

# power of 3
def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n = n / 3
    return n == 1

# reverse string III
class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_string = []
        for words in s.split():
            reverse = words[::-1]
            reverse_string.append(reverse)

        format  = ' '.join(reverse_string)
        return format     
       
#First Unique Character in a String
class Solution:
    def firstUniqChar(self, string: str) -> int:
        unique_characters = {}
        for s in string:
            characters = s
            if characters in unique_characters:
                unique_characters[characters] +=1
            else:
                unique_characters[characters] = 1

        for index,value in enumerate(string):
            if unique_characters[value] == 1:
                return index
        return -1

#First Letter to Appear Twice
class Solution:
    def repeatedCharacter(self, string: str) -> str:
        first_seen = set()
        for s in string:
            if s in first_seen:
                return s
            first_seen.add(s)
        return -1

#fizz buzz
class Solution:
    def fizzBuzz(self, n: int):
        fizz_buzz = []
        for i in range(1,n +1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_buzz.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_buzz.append("Fizz")
            elif i % 5 == 0:
                fizz_buzz.append("Buzz")
            else:
                fizz_buzz.append(str(i))
        return fizz_buzz

#Convert the temperature
class Solution:
    def convertTemperature(self, celsius: float):
        Temperature  = []
        if celsius < 0:
            return False
        kelvin = celsius + 273.15
        fahenreheit =  celsius * 1.80 + 32.00
        Temperature.append(kelvin)
        Temperature.append(fahenreheit)
        return Temperature
    
# add digit
class Solution:

    def addDigits(self, num: int) -> int:
        """
        while num >=10:
            digits = str(num)
            total = 0
            for digit in digits:
                if digit.isnumeric():
                    total += int(digit)
        num = total
        return num
        """
        if num == 0:
            return num
        else:
            if num % 9 == 0:
                return 9
        return num % 9 
    
# Majority Element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        numbers_dict = {}
        for num in nums:
            if num in numbers_dict:
                numbers_dict[num] +=1
            else:
                numbers_dict[num] = 1

        majority = None
        major = 0
        for key, value in numbers_dict.items():
            if value > major:
                majority = key
                major = value

        if major > len(nums) /2:
            return majority
        return -1
    
#  Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_list = []
        for num in nums:
            squared_list.append(num ** 2)
        return sorted(squared_list)

# Binary Search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        starting_index = 0
        ending_index = len(nums) - 1

        while starting_index <= ending_index:
            middle = int(starting_index + (ending_index - starting_index) / 2)
            value = nums[middle]
            print("Middle: ", value)

            if target > value:
                starting_index = middle + 1
            elif target < value: 
                ending_index = middle -1
            else:
                return middle
        return -1

#Number of Segments in a String
class Solution:
    def countSegments(self, s: str) -> int:
        string_str = s.split()
        return len(string_str)
    
# Find all Numbers Disappeared
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        range_lists = set(range(1,len(nums) +1))
        missing = list(range_lists - set(nums))
        return missing