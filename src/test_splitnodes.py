import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
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

    # Testing image and link splitters
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAINTEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.PLAINTEXT),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", TextType.PLAINTEXT),
                    TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ],
                new_nodes,
            )

    def test_split_nodes_link(self):
            node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and another [to youtube](http://www/youtube.com/@bootdotdev).",
                TextType.PLAINTEXT
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                    [
                        TextNode("This is text with a link ", TextType.PLAINTEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and another ", TextType.PLAINTEXT),
                        TextNode("to youtube", TextType.LINK, "http://www/youtube.com/@bootdotdev"),
                        TextNode(".", TextType.PLAINTEXT),
                    ],
                    new_nodes,
                )

    def test_split_nodes(self):
        test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test_nodes = text_to_textnodes(test_text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAINTEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAINTEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAINTEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAINTEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAINTEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            test_nodes
        )
