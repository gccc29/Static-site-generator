from blocks import BlockType, block_to_block_type
import unittest

class TestBlocks(unittest.TestCase):

    def test_block_to_block_type(self):
        heading = "## Heading 2"
        quote = "> Quote"
        code = "```\nCode here\n```"
        unordered_list = "- first item\n- second item"
        ordered_list = "1. first item\n2. second item"
        paragraph = "This is just text"

        self.assertEqual(block_to_block_type(heading), BlockType.HEADING)
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)
