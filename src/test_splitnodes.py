import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_1(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAINTEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIsInstance(new_nodes, list)
        for item in new_nodes:
            self.assertIsInstance(item, TextNode)

    def test_2(self):
        node1 = TextNode("This is text with a **bold** word", TextType.PLAINTEXT)
        node2 = TextNode("This is text with another **bold** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)

        self.assertIsInstance(new_nodes, list)
        self.assertTrue(len(new_nodes) == 4)
        for item in new_nodes:
            self.assertIsInstance(item, TextNode)

    def test_3(self):
        node1 = TextNode("This is text with a **bold** word", TextType.PLAINTEXT)
        node2 = TextNode("This is text with another **bold** word", TextType.PLAINTEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)

        self.assertIsInstance(new_nodes, list)
        self.assertTrue(len(new_nodes) == 6)
        for item in new_nodes:
            self.assertIsInstance(item, TextNode)

    def test_4(self):

        with self.assertRaises(Exception) as context:
            node1 = TextNode("This is text with a **bold** word", TextType.PLAINTEXT)
            node2 = TextNode("This is text with another **bold word", TextType.PLAINTEXT)
            new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)

        self.assertEqual(str(context.exception), "Missing a delimiter")
