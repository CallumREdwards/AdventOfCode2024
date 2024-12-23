import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from typing import Generator
    from functools import cache
    return Generator, cache, mo


@app.cell
def _(mo):
    mo.md("#Day 11: Plutonian Pebbles")
    return


@app.cell
def _(mo):
    mo.md("##Getting data")
    return


@app.cell
def _(mo):
    input_or_sample = mo.ui.dropdown(["file", "sample"], label="Input to use: ")
    input_or_sample
    return (input_or_sample,)


@app.cell
def _(input_or_sample, mo):
    if input_or_sample.value == "sample":
        input = "125 17"
    else:
        with open('data/input11.txt') as file:
            input = file.read().strip()

    start = [int(x) for x in input.split(" ")]
    mo.md(f"Starting state = {start}")
    return file, input, start


@app.cell
def _(mo):
    mo.md(r"""## Part 1""")
    return


@app.cell
def _(Generator):
    def next_blink(current: list[int]) -> Generator[int]:
        for stone in current:
            if stone == 0:
                yield 1
                continue
                
            str_stone = str(stone)
            if len(str_stone) % 2 == 0:
                mid = len(str_stone) // 2
                yield int(str_stone[:mid])
                yield int(str_stone[mid:])
            else:
                yield stone * 2024            
    return (next_blink,)


@app.cell
def _(mo):
    mo.md(r"""## Part 2""")
    return


@app.cell
def _(cache, start):
    @cache
    def count_stone(stone: int, blinks: int) -> int:
        if blinks == 0:
            return 1

        return sum(
            count_stone(new_stone, blinks - 1)
            for new_stone in next_blink2(stone)
        )

    @cache
    def next_blink2(stone: int) -> list[int]:
        match stone:
            case 0:
                return [1]
            case x if len(str(x)) % 2 == 0:
                str_stone = str(stone)
                mid = len(str_stone) // 2
                return [int(str_stone[:mid]), int(str_stone[mid:])]
            case _:
                return [stone * 2024]

    sum(count_stone(s, 75) for s in start)
    return count_stone, next_blink2


if __name__ == "__main__":
    app.run()
