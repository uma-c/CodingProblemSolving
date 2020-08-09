class Solution:
    def twoSum(self, nums, target):
        cache_complements = {}
        index = 0
        for num in nums:
            complement_index = cache_complements.get(num)
            if complement_index == None:
                cache_complements[target - num] = index
            else:                
                return [complement_index, index]
            
            index += 1

        return [-1, -1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
        