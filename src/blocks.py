from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "text paragraph"
    HEADING = "# Heading"
    CODE = r"```\nCode```"
    QUOTE = ">Quote"
    UNORDERED_LIST = "- unordered list"
    ORDERED_LIST = "1. ordered list"

def block_to_block_type(markdown: str) -> BlockType:
    if markdown.startswith(("#", "##", "###", "####", "#####", "######")) == True:
        return BlockType.HEADING
    elif markdown.startswith("```\n") == True and markdown.endswith("```"):
        return BlockType.CODE
    elif markdown.startswith(">") == True:
        return BlockType.QUOTE
    elif markdown.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif markdown.startswith("1. "):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
