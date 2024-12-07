import marimo

__generated_with = "0.9.30"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    from marimo import ui
    from marimo import md

    import polars as pl
    from typing import TypeVar
    from collections import Counter
    return Counter, TypeVar, md, mo, pl, ui


@app.cell
def __(md):
    md("#Day 1: Historian Hysteria ")
    return


@app.cell
def __(md):
    md("##Getting data")
    return


@app.cell
def __(ui):
    input_path = ui.text(
        value="data/input1.txt",
        label="Input text path: ")
    input_path
    return (input_path,)


@app.cell
def __(input_path, md):
    with open(input_path.value) as f:
        lines = f.read().splitlines()
    md(f"Input contains **{len(lines)}** lines")
    return f, lines


@app.cell
def __(lines, md, ui):
    start_line_to_show = ui.slider(start=1, stop=len(lines), step=1)
    num_lines_to_show = ui.number(start=1, stop=len(lines), step=1)

    md(
        f"""
    Configure lines to show:

    - Start line {start_line_to_show}
    - Number of lines {num_lines_to_show}
    """
    )
    return num_lines_to_show, start_line_to_show


@app.cell
def __(TypeVar, num_lines_to_show, start_line_to_show):
    _T = TypeVar('T')
    def user_slice(iter: list[_T]) -> list[_T]:
        first = start_line_to_show.value - 1
        last = start_line_to_show.value + num_lines_to_show.value - 1
        return iter[first:last]
    return (user_slice,)


@app.cell
def __(lines, md, user_slice):
    md("### Section of the input data\n\n" + "\n\n".join(user_slice(lines)))
    return


@app.cell
def __(lines, md, user_slice):
    parsed_lines = [
        tuple(map(int, line.split("   ")))
        for line in lines
    ]
    left, right = map(sorted, zip(*parsed_lines))

    column1 = ", ".join(map(str, user_slice(left)))
    column2 = ", ".join(map(str, user_slice(right)))

    md(f"""
    **Ordered column 1:** {column1}

    **Ordered column 2:** {column2}
    """)
    return column1, column2, left, parsed_lines, right


@app.cell
def __(md):
    md("##Part 1")
    return


@app.cell
def __(left, md, right):
    result1 = sum(abs(l - r) for l, r in zip(left, right))
    md(f"Answer = {result1}")
    return (result1,)


@app.cell
def __(md):
    md("##Part 2")
    return


@app.cell
def __(Counter, left, md, right):
    _counter_right = Counter(right)
    result2 = sum(l * _counter_right[l] for l in left)
    md(f"Answer = {result2}")
    return (result2,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
