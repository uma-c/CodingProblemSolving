from typing import List

class Robot:
    def __init__(self, room: List[List[int]], active_pos: List[int]):
        self.room = room
        self.direction = active_pos[2] # 0 : up, 1 : left, 2 : bottom, 3 : right
        self.active_pos = [active_pos[0], active_pos[1]]

    '''
    Returns true if the cell in front is open and robot moves into the cell
    Return false if the cell inf ront is blocked and robot stays in same cell
    '''
    def move(self):
        r, c = 0, 0
        if self.direction == 0:
            r = 1
        elif self.direction == 1:
            c = -1
        elif self.direction == 2:
            r = -1
        else:
            c = 1

        new_pos = [self.active_pos[0] + r, self.active_pos[1] + c]
        if (0 <= new_pos[0] < len(self.room)) and (0 <= new_pos[1] < len(self.room[0])) and self.room[new_pos[0]][new_pos[1]]:
            self.active_pos = new_pos
            return True
        return False

    '''
    Robot will stay in same cell aftre calling turnLeft/turnRight. Each turn will be 90 degrees
    '''
    def turnLeft(self):
        self.direction += 1
        self.direction %= 4

    '''
    Robot will stay in same cell aftre calling turnLeft/turnRight. Each turn will be 90 degrees
    '''
    def turnRight(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction += 4

    '''
    Clean current cell
    '''
    def clean(self):
        self.room[self.active_pos[0]][self.active_pos[1]] = -1 # -1 : Cleaned

def cleanRoom(room: List[List[int]], active_pos: List[int]):
    # right rule, go forward and at obstacle take right. Consider cleaned cell as virtual obstacle
    # once all possible directions are blocked, then reverse original direction with which it entered the cell
    robot = Robot(room, active_pos)
    def backtrack(new_cell, new_direction):
        pass

    

if __name__ == "__main__":
    room = [[1, 1, 1, 1, 1, 0, 1, 1], 
            [1, 1, 1, 1, 1, 0, 1, 1], 
            [1, 0, 1, 1, 1, 1, 1, 1], 
            [0, 0, 0, 1, 0, 0, 0, 0], 
            [1, 1, 1, 1, 1, 1, 1, 1]]
    active_pos = [1, 3, 0]
    cleanRoom(room, active_pos)