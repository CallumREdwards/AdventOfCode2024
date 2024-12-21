import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from dataclasses import dataclass
    return dataclass, mo


@app.cell
def _(mo):
    mo.md("#Day 7: Bridge Repair")
    return


@app.cell
def _(mo):
    mo.md("## Get data")
    return


@app.cell
def _():
    with open("data/input7.txt") as f:
        lines = f.readlines()
    lines[:3]
    return f, lines


@app.cell
def _(dataclass):
    @dataclass
    class Equation:
        values: list[int]
        result: int
    return (Equation,)


@app.cell
def _(Equation, lines):
    equations = [Equation([int(value) for value in right.strip().split(" ")], int(left))
                 for line in lines
                 for left, right in [line.split(":", 1)]]
    equations[0]
    return (equations,)


@app.cell
def _(mo):
    mo.md("## Part 1")
    return


@app.cell
def _():
    def is_valid_equation(values: list[int], result: int) -> bool:
        if len(values) == 1:
            return values[0] == result

        sumFirstTwo = sum(values[:2])
        if is_valid_equation([sumFirstTwo] + values[2:], result):
            return True

        productFirstTwo = values[0] * values[1]
        return is_valid_equation([productFirstTwo] + values[2:], result)

    assert is_valid_equation([11, 6, 16, 20], 292)
    return (is_valid_equation,)


@app.cell
def _(equations, is_valid_equation, mo):
    result1 = sum(e.result for e in equations if is_valid_equation(**e.__dict__))
    mo.md(f"Result 1 is {result1}")
    return (result1,)


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md("## Part 2")
    return


@app.cell
def _():
    def is_valid_equation_2(values: list[int], result: int) -> bool:
        if len(values) == 1:
            return values[0] == result

        sumFirstTwo = sum(values[:2])
        if is_valid_equation_2([sumFirstTwo] + values[2:], result):
            return True

        productFirstTwo = values[0] * values[1]
        if is_valid_equation_2([productFirstTwo] + values[2:], result):
            return True

        concactFirstTwo = int(str(values[0]) + str(values[1])) 
        return is_valid_equation_2([concactFirstTwo] + values[2:], result)

    assert is_valid_equation_2([6, 8, 6, 15], 7290) # 6 * 8 || 6 * 15
    return (is_valid_equation_2,)


@app.cell
def _(equations, is_valid_equation_2, mo):
    result2 = sum(e.result for e in equations if is_valid_equation_2(**e.__dict__))
    mo.md(f"Result 1 is {result2}")
    return (result2,)


if __name__ == "__main__":
    app.run()
