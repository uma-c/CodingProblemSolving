import unittest
from typing import List, Tuple

def can_attend_all_meetings(meetings:List[Tuple[int, int]]) -> bool:
    sorted_meetings = sorted(meetings)
    current_meeting_end = sorted_meetings[0][1]
    for i in range(1, len(sorted_meetings)):
        next_meeting = sorted_meetings[i]
        if current_meeting_end > next_meeting[0]:
            return False
        else:
            current_meeting_end = next_meeting[1]

    return True

class Tests(unittest.TestCase):
    def test_ex1(self):
        meetings = [(6,7),(2,4),(8,12)]
        result = can_attend_all_meetings(meetings)
        self.assertEqual(True, result)

    def test_ex2(self):
        meetings = [(1,4),(2,5),(7,9)]
        result = can_attend_all_meetings(meetings)
        self.assertEqual(False, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)