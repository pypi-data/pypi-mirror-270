# DinarLib #
## What is this? ##

This library simplifies the code

## Intersec ##

A method for finding intersections of an array

    def intersec(a,b):
    c = []
    for element in a:
        if element in b:
            c.append(element)
    return len(c)

## Quick_sort ##

The most optimized array sorting

    def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin+1, end+1):
        if int(sort_nums[i][4]) <= int(sort_nums[begin][4]):
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part
    def quick_sort(sort_nums, begin=0, end=None):
        if end is None:
            end = len(sort_nums) - 1
        def quick(sort_nums, begin, end):
            if begin >= end:
                return
            part = partition(sort_nums, begin, end)
            quick(sort_nums, begin, part-1)
            quick(sort_nums, part+1, end)
        return quick(sort_nums, begin, end)

## Random_sum ##

The maximum and the sum of the numbers are accepted as input
Allows you to randomly collect numbers in an array that will equal the amount specified in the parameter

    def random_sum(n, num_terms = None):
        num_terms = (num_terms or random.randint(2, n)) - 1
        a = random.sample(range(1, abs(n)), num_terms) + [0, abs(n)]
        list.sort(a)
        return [a[i+1] - a[i] for i in range(len(a) - 1)]

## Developer ##

https://github.com/ShakhmametovDinar