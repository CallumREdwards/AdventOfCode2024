import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from marimo import ui
    from marimo import md
    from typing import TypeVar
    return TypeVar, md, mo, ui


@app.cell
def __(md):
    md("#Day 2: Red-Nosed Reports")
    return


@app.cell
def __(md):
    md("##Getting data")
    return


@app.cell
def __(ui):
    input_path = ui.text(
        value="data/input2.txt",
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
    def user_slice(iter: iter[_T]) -> iter[_T]:
        iter = list(iter)
        first = start_line_to_show.value - 1
        last = start_line_to_show.value + num_lines_to_show.value - 1
        return iter[first:last]
    return (user_slice,)


@app.cell
def __(lines, md, user_slice):
    md("### Section of the input data\n\n" + "\n\n".join(user_slice(lines)))
    return


@app.cell
def __(lines, mo, user_slice):
    reports = [
        [int(level) for level in report.split(" ")]
        for report in lines
    ]
    mo.hstack(user_slice(reports))
    return (reports,)


@app.cell
def __(md):
    md("##Part 1")
    return


@app.cell
def __():
    def is_safe(report: list[int]) -> bool:
        if len(report) < 2:
            return True

        previous_level = report[0]
        order = "ASC" if report[1] > report[0] else "DESC"

        for current_level in report[1:]:

            step = current_level - previous_level

            if order == "ASC" and step <= 0:
                return False
            if order == "DESC" and step >= 0:
                return False
            if abs(step) > 3:
                return False

            previous_level = current_level

        return True
    return (is_safe,)


@app.cell
def __(is_safe):
    assert is_safe([7, 6, 4, 2, 1])
    assert not is_safe([1, 2, 7, 8, 9])
    assert not is_safe([9, 7, 6, 2, 1])
    assert not is_safe([1, 3, 2, 4, 5])
    assert not is_safe([8, 6, 4, 4, 1])
    assert is_safe([1, 3, 6, 7, 9])
    return


@app.cell
def __(is_safe, md, reports):
    result1 = sum(1 for l in reports if is_safe(l))
    md(f"Answer = {result1}")
    return (result1,)


@app.cell
def __(md):
    md("##Part 2")
    return


@app.cell
def __(is_safe):
    def is_safe_tolerable(report: list[int]) -> bool:
         return any( 
            True
            for i in range(len(report))
            if is_safe(report[:i] + report[i+1:])
         )
    return (is_safe_tolerable,)


@app.cell
def __(is_safe_tolerable):
    assert is_safe_tolerable([7, 6, 4, 2, 1])
    assert not is_safe_tolerable([1, 2, 7, 8, 9])
    assert not is_safe_tolerable([9, 7, 6, 2, 1])
    assert is_safe_tolerable([1, 3, 2, 4, 5])
    assert is_safe_tolerable([8, 6, 4, 4, 1])
    assert is_safe_tolerable([1, 3, 6, 7, 9])
    return


@app.cell
def __(is_safe_tolerable, md, reports):
    result2 = sum(1 for l in reports if is_safe_tolerable(l))
    md(f"Answer = {result2}")
    return (result2,)


if __name__ == "__main__":
    app.run()
