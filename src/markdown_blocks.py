#markdown_blocks.py


def markdown_to_blocks(markdown: str) -> list:
    blocks : list = markdown.split("\n\n")
    filtered_blocks: list = []
    for block in blocks:
        if block == "":
            continue
        block : str = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks