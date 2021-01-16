'''
621. Task Scheduler
Medium

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''
from typing import List
import collections

def least_interval(tasks:List[str], n:int) -> int:
    if len(tasks) < 1:
        return 0
    if n == 0:
        return len(tasks)
    count = collections.Counter(tasks)
    sorted_tasks = sorted(count, key=count.get, reverse=True)
    max_count = 0
    max_val = count[sorted_tasks[0]]
    for task in sorted_tasks:
        if count[task] == max_val:
            max_count += 1
        else:
            break
    part_len = n - max_count + 1
    part_count = max_val - 1
    available_slots_after_max_fills = part_len * part_count
    residual_tasks = len(tasks) - max_val * max_count
    idles = max(0, available_slots_after_max_fills - residual_tasks)
    return len(tasks) + idles

if __name__ == "__main__":
    print(least_interval(["A","A","A","B","B","B"], 2))
