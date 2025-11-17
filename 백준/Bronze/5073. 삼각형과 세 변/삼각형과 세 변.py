import sys ; input = sys.stdin.readline

def solution(nums: list) :
    nums.sort()
    maxl = nums.pop()
    
    if   sum(nums) <= maxl :            return "Invalid"
    elif nums[0]   == nums[1] == maxl : return "Equilateral"
    elif nums[0]   == nums[1] \
      or nums[1]   == maxl :            return "Isosceles"
    else :                              return "Scalene"
    
while True:
    nums = list(map(int, input().split(' ')))
    if not sum(nums) : break
    
    print(solution(nums))