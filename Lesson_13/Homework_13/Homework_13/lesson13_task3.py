#     Task 3
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
#     If all nums inside the list are positive, execute the first function on that list and return the result of it.
#     Otherwise, return the result of the second one

def choose_func(nums: list, *args):

    for i in args:
        nums = i(nums)
    return nums

def square_nums(num):
    res = [i ** 2 for i in num]
    return res

def remove_negatives(num):
    #     ты же умеешь в компрехенсион. Развивай мысль даьлше.
    return [i for i in num if i > 0]
    # или используя фильтр, хотя лямбда несколько усложняет.
    return list( filter( lambda i: i>0, num) )
#     и конечно традиционный цикл имеет право на жизнь я не спорю но он немного громоздко выглядит
    res = []
    for i in num:
        if i > 0:
            res.append(i)
    return res

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
