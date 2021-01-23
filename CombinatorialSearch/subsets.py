from typing import List

def __get_subsets(nums: List[int], subsets: List[List[int]]):
    if not nums:
        return

    __get_subsets(nums[0:len(nums) - 1], subsets)
    num = nums[-1]
    subsets_with_num = []
    for s in subsets:
        s_c = s.copy()
        s_c.append(num)
        subsets_with_num.append(s_c)
    subsets += subsets_with_num    

def get_subsets(nums:List[int]) -> List[List[int]]:
    subsets = [[]]
    __get_subsets(nums, subsets)
    return subsets

if __name__ == "__main__":
    print(get_subsets([1,2,3]))