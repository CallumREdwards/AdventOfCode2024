import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from marimo import md
    from dataclasses import dataclass
    import numpy as np
    from typing import Generator
    from functools import cache
    return Generator, cache, dataclass, md, mo, np


@app.cell
def _(md):
    md("#Day 10: Hoof It")
    return


@app.cell
def _(md):
    md("##Getting data")
    return


@app.cell
def _(mo):
    input_or_sample = mo.ui.dropdown(["file", "sample"], label="Input to use: ")
    input_or_sample
    return (input_or_sample,)


@app.cell
def _():
    sample = """89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732"""
    return (sample,)


@app.cell
def _(Generator, Optional, dataclass):
    Coordinates = tuple[int, int]
    Height = int

    @dataclass
    class Map:
        raw: list[list[int]]

        def __init__(self, text: list[str]):
            self.raw = [
                [int(char) for char in row.strip()]
                for row in text.split("\n")
                if row
            ]

        @property
        def width(self) -> int:
            return len(self.raw[0])

        @property
        def height(self) -> int:
            return len(self.raw)

        @property
        def positions(self) -> Generator[(Coordinates, Height)]:
            return (
                ((x, y), height)
                for y, row in enumerate(self.raw)
                for x, height in enumerate(row)
            )

        def positions_at_height(self, height: int) -> list[Coordinates]:
            return [pos for pos, h in self.positions if h == height]

        @property
        def trailheads(self) -> list[Coordinates]:
            return self.positions_at_height(0)

        @property
        def peaks(self) -> list[Coordinates]:
            return self.positions_at_height(9)

        def __contains__(self, coord: Coordinates) -> bool:
            x, y = coord
            return 0 <= x < self.width and \
                   0 <= y < self.height

        def __getitem__(self, coord: Coordinates) -> Optional[Height]:
            x, y = coord
            return self.raw[y][x] if coord in self else None
    return Coordinates, Height, Map


@app.cell
def _(Map, input_or_sample, md, sample):
    if input_or_sample.value == "sample":
        _input = sample
    else:
        with open("data/input10.txt") as file:
            _input = file.read()

    map = Map(_input)

    md(f"Map is {map.height}x{map.width}, there are {len(map.trailheads)} trailheads and {len(map.peaks)} peaks")
    return file, map


@app.cell
def _(md):
    md("##Part 1")
    return


@app.cell
def _(Coordinates, cache, map):
    @cache
    def peaks(coord: (int, int), height: int) -> set[Coordinates]:
        if height == 9:
            return {coord}

        peaks_seen = set()    
        x, y = coord
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_coord = ((x + dx), (y + dy))
            if (new_height := map[new_coord]) and new_height == height + 1:
                scores |= peaks(new_coord, new_height)

        return peaks_seen
    return (peaks,)


@app.cell
def _(map, peaks):
    sum(len(peaks(coord, 0)) for coord in map.trailheads)
    return


@app.cell
def _(md):
    md("##Part 2")
    return


@app.cell
def _(cache, map):
    @cache
    def rating(coord: (int, int), height: int) -> int:
        if height == 9:
            return 1

        rating_sum = 0 
        x, y = coord
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_coord = ((x + dx), (y + dy))
            if (new_height := map[new_coord]) and new_height == height + 1:
                rating_sum += rating(new_coord, new_height)

        return rating_sum
    return (rating,)


@app.cell
def _(map, rating):
    sum(rating(coord, 0) for coord in map.trailheads)
    return


if __name__ == "__main__":
    app.run()
