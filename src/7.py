import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
