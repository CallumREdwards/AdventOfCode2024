import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from marimo import ui
    from marimo import md
    from dataclasses import dataclass
    import numpy as np
    import copy
    return copy, dataclass, md, mo, np, ui


@app.cell
def __(md):
    md("Day 6: Guard Gallivant")
    return


@app.cell
def __(md):
    md("##Getting data")
    return


@app.cell
def __(copy, dataclass, np):
    @dataclass
    class Map:
        _data: list[list[bool]]

        def __init__(self, lines: list[str]):
            self._data = [[x == "#" for x in line] for line in lines]

        @property
        def width(self) -> int:
            return len(self._data[0])

        @property
        def height(self) -> int:
            return len(self._data)

        def is_blocked(self, pos: np.Array) -> bool:
            col, row = pos
            return self._data[row][col]

        def fill_cell(self, x: int, y: int) -> Map:
            new_map = copy.deepcopy(self)
            new_map._data[y][x] = True
            return new_map
    return (Map,)


@app.cell
def __(Map, md, np):
    with open("data/input6.txt") as f:
        lines = f.readlines()

    map = Map(lines)
    guard_position = next(
        np.array([x, y])
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "^")

    md(f"Map is {map.height}x{map.width} and guard is at {guard_position}")
    return f, guard_position, lines, map


@app.cell
def __(map, mo):
    mo.vstack(
        mo.hstack(line) for line in map._data
    )
    return


@app.cell
def __(md):
    md("##Part 1")
    return


@app.cell
def __(map, np):
    rotation_matrix = np.array([[0, -1], [1, 0]])

    def walk_count(position: np.ndarray) -> int:
        direction = np.array([0, -1])
        visited = {tuple(position)}
        updated_position = position + direction

        while -1 not in updated_position and \
           updated_position[0] != map.width and \
           updated_position[1] != map.height:

           if map.is_blocked(updated_position):
               direction = rotation_matrix @ direction
           else:
               position = updated_position
               visited.add(tuple(position))

           updated_position = position + direction

        return len(visited)
    return rotation_matrix, walk_count


@app.cell
def __(guard_position, md, walk_count):
    md(f"Answer = {walk_count(guard_position)}")
    return


@app.cell
def __(md):
    md("##Part 2")
    return


@app.cell
def __(guard_position, map, np, rotation_matrix):
    def creates_loop(x: int, y: int) -> bool:
        updated_map = map.fill_cell(x, y)
        
        direction = np.array([0, -1])
        position = guard_position
        visited = set()

        updated_position = position + direction

        while -1 not in updated_position and \
            updated_position[0] != map.width and \
            updated_position[1] != map.height:
            
            if (tuple(position), tuple(direction)) in visited:
               return True
            visited.add((tuple(position), tuple(direction)))
            
            if updated_map.is_blocked(updated_position):
               direction = rotation_matrix @ direction
            else:
               position = updated_position
            
            updated_position = position + direction

        return False

    return (creates_loop,)


@app.cell
def __(creates_loop, guard_position, map, md):
    result2 = sum(
        1
        for x in range(map.width)
        for y in range(map.height)
        if tuple(guard_position) != (x, y)
        and creates_loop(x, y)
    )
    md(f"Answer = {result2}")
    return (result2,)


if __name__ == "__main__":
    app.run()
