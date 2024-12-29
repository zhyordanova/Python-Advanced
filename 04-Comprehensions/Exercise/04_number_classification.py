numbers = [int(nums) for nums in input().split(", ")]

print(f"Positive: {', '.join([str(nums) for nums in numbers if nums >= 0])}")
print(f"Negative: {', '.join([str(nums) for nums in numbers if nums < 0])}")
print(f"Even: {', '.join([str(nums) for nums in numbers if nums % 2 == 0])}")
print(f"Odd: {', '.join([str(nums) for nums in numbers if not nums % 2 == 0])}")