import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from dataclasses import dataclass
    from itertools import groupby
    return dataclass, groupby, mo


@app.cell
def _(mo):
    mo.md(r"""# Day 12: Garden Groups""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Gettting data""")
    return


@app.cell
def _(mo):
    input_or_sample = mo.ui.dropdown(["file", "sample"], label="Input to use: ")
    input_or_sample
    return (input_or_sample,)


@app.cell
def _(List):
    def transpose(matrix: List[List[str]]) -> List[List[str]]:
         return [list(column) for column in zip(*matrix)]

    matrix = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"]
    ]

    expected_output = [
        ["a", "d", "g"],
        ["b", "e", "h"],
        ["c", "f", "i"]
    ]

    assert transpose(matrix) == expected_output
    return expected_output, matrix, transpose


@app.cell
def _(dataclass, groupby, transpose):
    @dataclass
    class Region:
        area: int
        perimeter: int

    @dataclass
    class Map:
        raw: list[list[str]]
        regions: list[Region]

        def __init__(self, raw_data: str):
            self.raw = [list(line.strip()) for line in self.raw.split("\n")]
        
            row_grouped_matrix = [groupby(row) for row in self.raw]
            column_grouped_matrix = [groupby(column) for column in transpose(self.raw)]

            marked = [[False for _ in range(self.width)] for __ in range(self.height)]
            for grouped_row in row_grouped_matrix:
                x = 0
                for plant, group in grouped_row:
                    marked = []
                    x += 1
                    
                

        @property
        def width(self) -> int:
            return len(self.raw[0])

        @property
        def height(self) -> int:
            return len(self.raw)

        
                
    return Map, Region


@app.cell
def _(input_or_sample):
    if input_or_sample.value == "sample":
        input = """
            RRRRIICCFF
            RRRRIICCCF
            VVRRRCCFFF
            VVRCCCJFFF
            VVVVCJJCFE
            VVIVCCJJEE
            VVIIICJJEE
            MIIIIIJJEE
            MIIISIJEEE
            MMMISSJEEE"""
    else:
        with open('data/input11.txt') as file:
            input = file.read()
    return file, input


if __name__ == "__main__":
    app.run()
