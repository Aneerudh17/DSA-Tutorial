class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        
        #initialise result list
        result = []

        #find current and remaining from the list
        for i in range(len(nums)):
            current = nums[i]

            #extracting the numbers other than i from the list
            remaining = nums[:i] + nums[i+1:]

            #recursion to add the remamining numbers to the result list
            for p in self.permute(remaining):
                
                #appending the remaining numbers to get the remaining permutations
                result.append([current]+p)
        
        #return the list
        return result