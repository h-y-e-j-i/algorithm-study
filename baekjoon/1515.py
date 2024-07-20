import sys

nums = [int(n) for n in sys.stdin.readline().strip()]
increase_num = 0

while True:
    increase_num += 1

    for n in str(increase_num):
        if int(n) == nums[0]:
            nums.pop(0)
        else:
            pass

        if len(nums) == 0:
            break

    if len(nums) == 0:
        break

print(increase_num)