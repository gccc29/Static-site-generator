

from blocks import BlockType, block_to_block_type
from split_blocks import markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    heading = ""
    for block in blocks:
        if block.startswith("# "):
            heading = block
            break

    if heading == "":
        raise Exception("No H1 Heading")

    return heading.strip("# ")
