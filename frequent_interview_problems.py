def reverse_string_words(st: str):
    n = len(st)
    words = []
    
    i = 0
    while i < n and st[i] == " ":  # Remove leading spaces
        i += 1
    st = st[i:] 

    i = len(st) - 1
    while i >= 0 and st[i] == " ": # Remove trailing spaces
        i -= 1
    st = st[:i + 1]  

    n = len(st)
    i = 0
    while i < n:
        while i < n and st[i] == " ":  # Skip spaces b/w words
            i += 1

        if i >= n:
            break

        start = i
        while i < n and st[i] != " ":   # Skip spaces
            i += 1 

        words.append(st[start:i]) 

    res = ""
    for j in range(len(words) - 1, -1, -1):
        if res:
            res += " "
        res += words[j]

    return res

# print(reverse_string_words("the sky is blue"))     
# print(reverse_string_words("  hello world  "))     
# print(reverse_string_words("a good   example"))     
# print(reverse_string_words("My Name is ARUN  what is    yours"))

def reverse_string_character(st:str):
    res = ""
    for inx in range(len(st)-1,-1,-1):
        res += st[inx]
    return res

# print(reverse_string_character("python"))
# print(reverse_string_character("Go back"))
# print(reverse_string_character("room"))
# print(reverse_string_character("My First Time Coding"))

import heapq

def get_kth_number(arr: list, k: int, key="largest") -> int:
    """
    Get the kth largest or smallest number from the array Using Heapq.
    """
    if not arr or k <= 0 or k > len(arr):
        return -1

    if key == "largest":
        min_heap = arr[:k]
        heapq.heapify(min_heap)  

        for num in arr[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]

    elif key == "smallest":
        max_heap = [-num for num in arr[:k]]
        heapq.heapify(max_heap) 

        for num in arr[k:]:
            if -num > max_heap[0]:  
                heapq.heappushpop(max_heap, -num)
        return -max_heap[0] 

    else:
        raise ValueError("Invalid key. Use 'largest' or 'smallest'.")


def get_kth_number_2(arr,k,key="largest"):
    """
    Get kth number according key from list.
    """
    def quickselect(l,r,k):
        pivot,p = arr[r],l
        for i in range(l,r):
            if arr[i] < pivot:
                arr[p],arr[i] = arr[i],arr[p]
                p += 1

        arr[p],arr[r] = arr[r],arr[p]

        if p > k: return quickselect(l,p-1,k)
        elif p < k: return quickselect(p+1,r,k)
        else: return arr[p]
    
    n = len(arr)
    if key =="largest":
        return quickselect(0,n-1,n-k)
    if key == "smallest":
        return quickselect(0,n-1,k-1)

# print(get_kth_number([4,7,6,8,2,1],1)) # 8
# print(get_kth_number([4,7,6,8,2,1],2)) # 7
# print(get_kth_number([4,7,6,8,2,1],3)) # 6

# print(get_kth_number([4,7,6,8,2,1],1,'smallest')) # 1
# print(get_kth_number([4,7,6,8,2,1],2,'smallest')) # 2
# print(get_kth_number([4,7,6,8,2,1],3,'smallest')) # 4


print(get_kth_number_2([4,7,6,8,2,1],1)) # 8
print(get_kth_number_2([4,7,6,8,2,1],2)) # 7
print(get_kth_number_2([4,7,6,8,2,1],3)) # 6

print(get_kth_number_2([4,7,6,8,2,1],1,'smallest')) # 1
print(get_kth_number_2([4,7,6,8,2,1],2,'smallest')) # 2
print(get_kth_number_2([4,7,6,8,2,1],3,'smallest')) # 4



def subarray_sum_equal_to_k(nums, k):
    """
    Find the count of subarrays that sum to k.
    
    Args:
        nums (list): List of integers.
        k (int): Target sum.
        
    Returns:
        int: Count of subarrays with sum equal to k.
    """
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # Initialize with 0 to handle cases where subarray starts from index 0
    
    for num in nums:
        current_sum += num
        # Check if (current_sum - k) exists in the prefix_sums map
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        # Update the prefix_sums map
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count


def subarray_sum_greater_than_k(nums, k):
    """
    Find the count of subarrays whose sum is greater than k.
    
    Args:
        nums (list): List of integers.
        k (int): Target sum.
        
    Returns:
        int: Count of subarrays with sum greater than k.
    """
    count = 0
    start = 0
    current_sum = 0

    for end in range(len(nums)):
        current_sum += nums[end]
        
        # Shrink the window until the sum is less than or equal to k
        while current_sum > k and start <= end:
            count += len(nums) - end  # All subarrays from start to end are valid
            current_sum -= nums[start]
            start += 1

    return count


def quicksort(arr):
    """
    Sort the array using the QuickSort algorithm.
    """
    if len(arr) <= 1: 
        return arr
    
    pivot = arr[-1] 
    left = [x for x in arr[:-1] if x <= pivot]  # Elements smaller than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot    
    return quicksort(left) + [pivot] + quicksort(right)

def merge_sort(arr):
    """
    Sort the array using the MergeSort algorithm.
    """
    def merge(left, right):
        """
        Merge two sorted arrays into one sorted array.
        """
        merged = []
        i = j = 0
        
        # Compare elements from left and right and merge them
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)



def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        
        if arr[mid] == target:  
            return mid
        elif arr[mid] < target: 
            low = mid + 1  # Target is greater, search right half
        else: 
            high = mid - 1  # Target is smaller, search left half
    
    return -1

def twoSum( nums, target):
    #1. Bruteforce
    # n = len(nums)

    # for i in range(n):
    #     for x in range(i+1,n):
    #         if (nums[i] + nums[x]) == target:
    #             return [i,x]
    # return 
    #2. Hashmap
    validxHashMap = {}

    for idx,num in enumerate(nums):
        diffasval = target - num
        if diffasval in validxHashMap:
            return [validxHashMap[diffasval],idx]
        validxHashMap[num] = idx
    
    return

def containsDuplicate(nums):
    # approach 1 ---
    # counter = Counter(nums)
    # max_count = float("-inf")
    # for val,con in counter.items():
    #     if con > max_count:
    #         max_count = con
    
    # if max_count>=2:
    #     return True
    
    # return False

    # approach 2 ---
    # nums.sort()
    # n = len(nums)
    # for i in range(n):
    #     if i<n-1:
    #         if nums[i] == nums[i+1]:
    #             return True
    
    # return False

    # approach 3 ----
    # return False if len(set(nums)) == len(nums) else True

    # approcah 4----
    # nums.sort()
    # start = 0
    # end = 1

    # while start < len(nums)-1:
    #     if nums[start] == nums[end]:
    #         return True
        
    #     start +=1
    #     end += 1
    
    # return False

    # approach 5---
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False


