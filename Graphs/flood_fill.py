from typing import List

def flood_fill(image: List[List[int]], r:int, c:int, origColor:int, newColor:int):
    if not (0 <= r < len(image)) or not (0 <= c < len(image[0])):
        return

    if image[r][c] != origColor:
        return

    if image[r][c] == -1:
        return

    image[r][c] = -1    
    flood_fill(image, r - 1, c, origColor, newColor)
    flood_fill(image, r, c - 1, origColor, newColor)
    flood_fill(image, r + 1, c, origColor, newColor)
    flood_fill(image, r, c + 1, origColor, newColor)
    image[r][c] = newColor

def fill(image: List[List[int]], sr:int, sc:int, newColor:int) -> List[List[int]]:
    origColor = image[sr][sc]
    flood_fill(image, sr, sc, origColor, newColor)
    return image