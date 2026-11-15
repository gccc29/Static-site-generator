
def markdown_to_blocks(markdown) -> list[str]:
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        new_block = block.strip('\n')
        if new_block.strip() != "":
            new_blocks.append(new_block)
    return new_blocks
