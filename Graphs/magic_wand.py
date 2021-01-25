from typing import List

def fill_edges(image:List[List[int]], r:int, c:int, visited:List[List[int]], origColor:int, newColor:int) -> int:
    if not (0 <= r < len(image)) or not (0 <= c < len(image[0])):
        return 0

    if visited[r][c] == 1:
        return 1

    if image[r][c] != origColor:
        return 0

    visited[r][c] = 1
    sorround = fill_edges(image, r, c - 1, visited, origColor, newColor) + \
            fill_edges(image, r - 1, c, visited, origColor, newColor) + \
            fill_edges(image, r, c + 1, visited, origColor, newColor) + \
            fill_edges(image, r + 1, c, visited, origColor, newColor)
    
    if sorround < 4:
        image[r][c] = newColor

    return 1

def magic_wand(image:List[List[int]], sr:int, sc:int):
    edge_color = 65535
    origColor = image[sr][sc]
    visited = [[0] * len(image[0]) for _ in range(len(image))]
    fill_edges(image, sr, sc, visited, origColor, edge_color, visited)

if __name__ == "__main__":
    nr, nc = 3, 3
    visited = [[0] * nc for _ in range(nr)]
    visited[1][1] = 1
    print(visited)