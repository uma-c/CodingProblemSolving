'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.
'''
from typing import List

def reorder_logs(logs: List[int]) -> List[str]:
    let_logs = []
    dig_logs = []
    for log in logs:
        if '0' <= log[-1] <= '9':
            dig_logs.append(log)
        else:
            ident_after_idx = log.index(' ')
            let_logs.append([log[(ident_after_idx+1):], log[0:ident_after_idx]])
    let_logs.sort()
    result = []
    for let_log in let_logs:
        result.append(let_log[1] + ' ' + let_log[0])
    result += dig_logs
    return result