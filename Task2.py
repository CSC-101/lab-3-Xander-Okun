def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total                         # total=0 then 4 then 13 then 15 then 16

result = tally([4, 9, 2, 1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.    [4,9,2,1] it goes from index 0,1,2,3
    return new_list                    # How does this loop differ from that above? instead of adding the items it just takes the value and recreates the list.
result = copy([4, 9, 2, 1])



def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. [5,10,3,2] its taking each value and increasing it by one then adding it to a new list.
    return new_list

result = increment_all([4, 9, 2, 1])