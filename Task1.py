more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. step 1:1, step 2:2, step 3:3 step 4:4
print(more)                               # What is the value of more at this point? [2,3,4,5]



def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. 1,1   2,4   3,9   4,16

squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print(squares)                                    # values recorded above?  squares is [1,4,9,16] and it is just the list from before but each item in the list was squared



def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0 False, 1 False, 2 False, 3 True, 4 True

answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print(answer)



def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. not evalutated, not evaluated, not evaluated, 3+1=4, 4+1=5

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0 false, 1 false, 2 false, 3 true, 4 true

answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5]
print(answer)


