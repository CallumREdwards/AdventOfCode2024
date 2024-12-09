import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from marimo import ui
    from marimo import md
    return md, mo, ui


@app.cell
def __(md):
    md("#Day 5: Print Queue")
    return


@app.cell
def __(md):
    md("##Getting data")
    return


@app.cell
def __(md):
    with open("data/input5.txt") as f:
        rules_raw, updates_raw = [part.split("\n") for part in f.read().split("\n\n")]
    md(f"There were {len(rules_raw)} rules and {len(updates_raw)} updates")
    return f, rules_raw, updates_raw


@app.cell
def __(mo, rules_raw, updates_raw):
    rules = [list(map(int, r.split("|"))) for r in rules_raw]
    updates = [[int(x) for x in u.split(",") if x] for u in updates_raw if u]
    mo.hstack([rules[0], updates[0]])
    return rules, updates


@app.cell
def __(md):
    md("##Part 1")
    return


@app.cell
def __(rules):
    def all_before(update: int) -> set[int]:
        return {before for before, after in rules if after == update}

    assert 99 in all_before(31)
    return (all_before,)


@app.cell
def __(all_before):
    def is_correctly_ordered(updates: list[int]) -> bool:
        banned = set()
        for u in updates:
            if u in banned:
                return False
            banned.update(all_before(u))
        return True

    assert not is_correctly_ordered([31, 99])
    assert is_correctly_ordered([99, 31])
    return (is_correctly_ordered,)


@app.cell
def __(updates):
    assert not sum(1 for u in updates if len(u) % 2 == 0)
    return


@app.cell
def __():
    def get_middle_element(lst: list) -> any:
        return lst[len(lst) // 2]
    return (get_middle_element,)


@app.cell
def __(is_correctly_ordered, md, updates):
    result1 = sum(u[len(u) // 2] for u in updates if is_correctly_ordered(u))
    md(f"Answer = {result1}")
    return (result1,)


@app.cell
def __(md):
    md("##Part 2")
    return


@app.cell
def __(all_before):
    # [3, 2, 1, 4]

    # 3 ->
    #     [2, 1] 3 [4]
    #         -> [1] 2 []
    #         -> [1, 2]
    #     [1, 2, 3, 4]

    def correct_order(updates: list[int]) -> list[int]:
        if len(updates) <= 1:
            return updates

        all_before_first = all_before(updates[0])
        
        before, after = [], []
        for u in updates[1:]:
             (before if u in all_before_first else after).append(u)

        return correct_order(before) + [updates[0]] + correct_order(after)

    assert correct_order([31, 99]) == [99, 31]
    return (correct_order,)


@app.cell
def __(correct_order, is_correctly_ordered, md, updates):
    result2 = sum(
        correct_order(u)[len(u) // 2]
        for u in updates if not is_correctly_ordered(u)
    )
    md(f"Answer = {result2}")
    return (result2,)


if __name__ == "__main__":
    app.run()
