import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from marimo import ui
    from marimo import md
    import re
    return md, mo, re, ui


@app.cell
def __(md):
    md("#Day 3: Mull It Over")
    return


@app.cell
def __(md):
    md("##Getting data")
    return


@app.cell
def __(ui):
    input_path = ui.text(
        value="data/input3.txt",
        label="Input text path: ")
    input_path
    return (input_path,)


@app.cell
def __(input_path):
    with open(input_path.value) as f:
        data = f.read()
    data[:100]
    return data, f


@app.cell
def __(md):
    md("##Part 1")
    return


@app.cell
def __(re):
    def sum_mults(input: str) -> int:
        matches = re.findall(r'mul\((\d+),(\d+)\)', input)
        return sum(int(m[0]) * int(m[1]) for m in matches)
    return (sum_mults,)


@app.cell
def __(data, md, sum_mults):
    md(f"Answer = {sum_mults(data)}")
    return


@app.cell
def __(md):
    md("##Part 2")
    return


@app.cell
def __(data, mo):
    def split_text(text: str) -> list[str]:
        import re
        pattern = r"do\(\)|don't\(\)"
        return re.split(pattern, text)

    mo.vstack(split_text(data)[:3])
    return (split_text,)


@app.cell
def __(data, re):
    def take_enabled(text: str) -> str:
        result = ""
        enabled = True

        for part in re.split(r"(do\(\)|don't\(\))", text):
            if part == "do()":
                enabled = True
            elif part == "don't()":
                enabled = False
            elif enabled:
                result += part

        return result

    take_enabled(data)[:100]
    return (take_enabled,)


@app.cell
def __(data, md, sum_mults, take_enabled):
    result2 = sum_mults(take_enabled(data))
    md(f"Answer = {result2}")
    return (result2,)


if __name__ == "__main__":
    app.run()
