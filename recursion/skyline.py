'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 

Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
'''

from typing import List

def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    def merge(l: List[List[int]], r: List[List[int]]) -> List[List[int]]:
        #print(l, r)
        nL, nR = len(l), len(r)
        cL = cR = 0
        currY = leftY = rightY = 0
        x = maxY = 0
        result = []
        while cL < nL and cR < nR:
            if l[cL][0] < r[cR][0]:
                x = l[cL][0]
                leftY = l[cL][1]
                cL += 1
            else:
                x = r[cR][0]
                rightY = r[cR][1]
                cR += 1
            maxY = max(leftY, rightY)
            if currY != maxY:
                if len(result) == 0 or result[-1][0] != x:
                    result.append([x, maxY])
                else:
                    result[-1][1] = maxY
                currY = maxY
        while cL < nL:
            if currY != l[cL][1]:
                if len(result) == 0 or result[-1][0] != l[cL][0]:
                    result.append([l[cL][0], l[cL][1]])
                else:
                    result[-1][1] = l[cL][1]
                currY = l[cL][1]
            cL += 1
        while cR < nR:
            if currY != r[cR][1]:
                if len(result) == 0 or result[-1][0] != r[cR][0]:
                    result.append([r[cR][0], r[cR][1]])
                else:
                    result[-1][1] = r[cR][1]
                currY = r[cR][1]
            cR += 1
        return result

    def get(i: int, j: int) -> List[List[int]]:
        if i == j: # one building only
            return [[buildings[i][0], buildings[i][2]], [buildings[i][1], 0]]

        m = i + (j - i) // 2
        print(i, m, j)
        left = get(i, m)
        right = get(m + 1, j)
        return merge(left, right)

    return get(0, len(buildings) - 1)

if __name__ == "__main__":
    buildings = [[0,2,3],[2,5,3]] #[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(getSkyline(buildings))