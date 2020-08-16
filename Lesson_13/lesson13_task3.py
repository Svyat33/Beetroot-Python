nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(i):
    res = i ** 2
    return (res)

# def choose_func(nums: list, func1, func2):
#     def funk1(n):
#         res = [i ** 2 for i in nums]
#         return (res)
print(list(map(square_nums, nums1 )))
print(dict(zip(nums2, nums1 )))