import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAINTEXT)
        node3 = TextNode("This is a different text node", TextType.ITALIC, "https://www.boot.dev")
        node4 = TextNode("This is boot.dev", TextType.CODE, "https://www.boot.dev")
        node5 = TextNode("This is boot.dev", TextType.CODE, "https://www.google.com")
        self.assertNotEqual(node, node2, node3)


if __name__ == "__main__":
    unittest.main()
