import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from marimo import md
    from abc import ABC, abstractmethod
    from dataclasses import dataclass
    from typing import Optional
    return ABC, Optional, abstractmethod, dataclass, md, mo


@app.cell
def _(md):
    md("#Day 9: Disk Fragmenter")
    return


@app.cell
def _(md):
    md("## Getting data")
    return


@app.cell
def _(mo):
    input_or_sample = mo.ui.dropdown(["file", "sample"], label="Input to use: ")
    input_or_sample
    return (input_or_sample,)


@app.cell
def _(input_or_sample):
    if input_or_sample.value == "file":
        with open('data/input9.txt') as file:
            _lines = file.readlines()
        assert len(_lines) == 1
        input = _lines[0].strip()
    else:
        input = "2333133121414131402"
        
    input[:100]
    return file, input


@app.cell
def _(ABC, dataclass):
    class Chunk(ABC):
        pass

    @dataclass
    class FreeChunk(Chunk):
        count: int

    @dataclass
    class FileChunk(Chunk):
        id: int
        count: int
    return Chunk, FileChunk, FreeChunk


@app.cell
def _(Chunk, FileChunk, FreeChunk, input):
    def parse_input(input: str) -> list[Chunk]:
        id = 0
        is_file = True
        chunks = []
        
        for count in map(int, input):
            if is_file:
                chunks.append(FileChunk(id, count))
                id += 1
            else:
                chunks.append(FreeChunk(count))        
            is_file = not is_file

        return chunks

    uncompacted_chunks = parse_input(input)
    uncompacted_chunks
    return parse_input, uncompacted_chunks


@app.cell
def _(FreeChunk, uncompacted_chunks):
    uncompacted_blocks = [
        None if isinstance(chunk, FreeChunk) else chunk.id
        for chunk in uncompacted_chunks
        for _ in range(chunk.count)
    ]
    uncompacted_blocks[:10]
    return (uncompacted_blocks,)


@app.cell
def _(md):
    md("##Part 1")
    return


@app.cell
def _(Optional):
    def compact(uncompacted: list[Optional[int]]) -> list[int]:
        uncompacted = uncompacted.copy()
        compacted = []

        while len(uncompacted) > 0:
            if not uncompacted[-1]:
                uncompacted.pop()
                continue
            
            first = uncompacted.pop(0)

            if first is not None:
                compacted.append(first)
                continue
            
            if uncompacted:
                last = uncompacted.pop()
                if last is not None:
                    compacted.append(last)
        
        return compacted

    assert compact([1, None, 2, None, 3]) == [1, 3, 2]
    return (compact,)


@app.cell
def _(compact, md, uncompacted_blocks):
    compacted_blocks = compact(uncompacted_blocks)
    md("".join(map(str, compacted_blocks))[:100])
    return (compacted_blocks,)


@app.cell
def _():
    def checksum(blocks: list[int]) -> int:
        return sum(id * index for index, id in enumerate(blocks))

    assert checksum([1, 3, 2]) == 7
    return (checksum,)


@app.cell
def _(checksum, compacted_blocks, md):
    md(f"Answer is {checksum(compacted_blocks)}")
    return


@app.cell
def _(md):
    md("##Part 2")
    return


@app.cell
def _(Chunk, FreeChunk, uncompacted_chunks):
    def compact2(uncompacted: list[Chunk]) -> list[Chunk]:
        uncompacted = uncompacted.copy()
        compacted = []

        while len(uncompacted) > 0:        
            last = uncompacted.pop()

            if isinstance(last, FreeChunk):
                compacted.insert(0, last)
                continue
            
            for i, block in enumerate(uncompacted):
                if isinstance(block, FreeChunk) and block.count >= last.count:
                    new_blocks = [last]
                    if block.count != last.count:
                        new_blocks.append(FreeChunk(block.count - last.count))
                    uncompacted = uncompacted[:i] + new_blocks + uncompacted[i+1:]
                    compacted.insert(0, FreeChunk(last.count))
                    break
            else:
                compacted.insert(0, last)
        
        return compacted

    compacted_chunks = compact2(uncompacted_chunks)
    compacted_chunks[:10]
    return compact2, compacted_chunks


@app.cell
def _(Chunk, FileChunk):
    def checksum2(chunks: list[Chunk]) -> int:
        pos = 0
        sum = 0
        
        for chunk in chunks:
            if isinstance(chunk, FileChunk):
                for _ in range(chunk.count):
                    sum += pos * chunk.id
                    pos += 1
            else:
                pos += chunk.count

        return sum
    return (checksum2,)


@app.cell
def _(checksum2, compacted_chunks, md):
    md(f"Answer is {checksum2(compacted_chunks)}")
    return


if __name__ == "__main__":
    app.run()
