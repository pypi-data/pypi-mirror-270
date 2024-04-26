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