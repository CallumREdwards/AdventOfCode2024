import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    from dataclasses import dataclass
    return dataclass, mo, np


@app.cell
def _(mo):
    mo.md("#Day 8: Resonant Collinearity")
    return


@app.cell
def _(mo):
    mo.md("##Getting data")
    return


@app.cell
def _(dataclass, np):
    Frequency = str
    Coordinates = np.ndarray

    @dataclass
    class Map:
        frequencies: dict[Frequency, list[Coordinates]]
        _data: list[list[bool]]

        def __init__(self, lines: list[str]):
            self._data = []
            self.frequencies = {}

            for y, line in enumerate(lines):
                row = []
                for x, char in enumerate(line.strip()):
                    if char == '.':
                        row.append(None)
                        continue
                    row.append(char)
                    if char not in self.frequencies:
                        self.frequencies[char] = []
                    self.frequencies[char].append(np.array([x, y]))
                self._data.append(row)

        @property
        def width(self) -> int:
            return len(self._data[0])

        @property
        def height(self) -> int:
            return len(self._data)

        def __contains__(self, coord: Coordinates) -> bool:
            x, y = coord
            return 0 <= x < self.width and \
                   0 <= y < self.height
    return Coordinates, Frequency, Map


@app.cell
def _(mo):
    input_or_sample = mo.ui.dropdown(["file", "sample"], label="Input to use: ")
    input_or_sample
    return (input_or_sample,)


@app.cell
def _():
    return


@app.cell
def _(Map, input_or_sample, mo):
    if input_or_sample.value == "file":
        with open("data/input8.txt") as f:
            lines = f.readlines()
    else:
        sample = """............
                    ........0...
                    .....0......
                    .......0....
                    ....0.......
                    ......A.....
                    ............
                    ............
                    ........A...
                    .........A..
                    ............
                    ............"""
        lines = sample.split("\n")

    map = Map(lines)

    mo.md(f"Map is {map.height}x{map.width}")
    return f, lines, map, sample


@app.cell
def _(mo):
    mo.md("##Part 1")
    return


@app.cell
def _(Coordinates, map, mo, np):
    def antinodes(coords: Coordinates) -> set[tuple[int, int]]:
        return {
            tuple(new)
            for start in coords
            for end in coords
            if not np.array_equal(start, end) and \
                (new := end + (end - start)) in map
        }

    result1 = len({
         coord
         for coords in map.frequencies.values()
         for coord in antinodes(coords)
     })

    mo.md(f"Answer is {result1}")
    return antinodes, result1


@app.cell
def _(mo):
    mo.md("##Part 2")
    return


@app.cell
def _(Coordinates, map, mo, np):
    def antinodes2(coords: Coordinates) -> set[tuple[int, int]]:
        return {
            tuple(new)
            for start in coords
            for end in coords
            for step in range(0, max(map.width, map.height))
            if not np.array_equal(start, end) and \
                (new := end + step * (end - start)) in map
        }

    result2 = len({
         coord
         for coords in map.frequencies.values()
         for coord in antinodes2(coords)
     })

    mo.md(f"Answer is {result2}")
    return antinodes2, result2


if __name__ == "__main__":
    app.run()
