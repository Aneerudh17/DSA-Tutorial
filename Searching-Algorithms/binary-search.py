#implementation of binary search
class solution:
    def binarysearch(nums:list[int],x : int) -> int:
        n = len(nums)
        #initialise low to be first position
        low = 0

        #initialise high to be the last position
        high = n - 1

        #initialise mid
        mid = low + (low - high) // 2

        #loop until low <= high
        while low <= high:

            #if number if found at the mid, then return mid
            if nums[mid] == x:
                return mid
            
            #if number is greater than mid, then move to the right half
            elif nums[mid] < x:
                low = mid + 1

            #if number is smaller than mid, then move to the left half
            else:
                high = mid-1

        #if the element is not present then return -1                
        return -1
    