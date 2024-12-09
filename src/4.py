import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from marimo import ui
    from marimo import md
    import numpy as np
    return md, mo, np, ui


@app.cell
def __(md):
    md("#Day 4: Ceres Search")
    return


@app.cell
def __(md):
    md("##Getting data")
    return


@app.cell
def __(ui):
    input_path = ui.text(
        value="data/input4.txt",
        label="Input text path: ")
    input_path
    return (input_path,)


@app.cell
def __(input_path, md, np):
    with open(input_path.value) as f:
        matrix = np.array([list(line.strip()) for line in f])
    cols = len(matrix[0])
    rows = len(matrix)
    md(f"Grid is {rows}x{cols}")
    return cols, f, matrix, rows


@app.cell
def __(matrix, mo):
    mo.vstack(
        mo.hstack(row) for row in matrix
    )
    return


@app.cell
def __(md):
    md("##Part 1")
    return


@app.cell
def __(mo, np):
    deltas = [
        np.array([x, y])
        for x in [-1, 0, 1]
        for y in [-1, 0, 1]
        if (x, y) != (0, 0)
    ]
    mo.hstack(deltas)
    return (deltas,)


@app.cell
def __(cols, deltas, matrix, np, rows):
    def num_xmas(pos: np.Array) -> int:
        count = 0
        for delta in deltas:
            _pos = pos.copy()
            for letter in "XMAS":
                row, col = _pos
                if row < 0 or row == rows or col < 0 or col == cols:
                    break
                if matrix[row][col] != letter:
                    break
                _pos += delta
            else:
                count += 1
        return count

    assert num_xmas(np.array([0, 3])) == 2
    return (num_xmas,)


@app.cell
def __(cols, md, np, num_xmas, rows):
    grid = np.indices((rows, cols)).reshape(2, -1).T
    result1 = sum(num_xmas(pos) for pos in grid)
    md(f"Answer = {result1}")
    return grid, result1


@app.cell
def __(md):
    md("##Part 2")
    return


@app.cell
def __(cols, matrix, rows):
    def is_xmas_a(row: int, col: int) -> bool:
        if matrix[row, col] != "A":
            return False

        if row == 0 or row + 1 == rows or col == 0 or col + 1 == cols:
            return False
        
        diagonal_1 = matrix[row-1, col-1] + matrix[row+1, col+1]
        diagonal_2 = matrix[row+1, col-1] + matrix[row-1, col+1]
        return diagonal_1 in ["MS", "SM"] and diagonal_2 in ["MS", "SM"]

    assert is_xmas_a(2, 1)
    return (is_xmas_a,)


@app.cell
def __(cols, is_xmas_a, md, rows):
    result2 = sum(1 for x in range(cols) for y in range(rows) if is_xmas_a(x, y))
    md(f"Answer = {result2}")
    return (result2,)


if __name__ == "__main__":
    app.run()
