import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    node = HTMLNode("<p>", "hello world")
    node2 = HTMLNode("<a>", props={"href": "https://www.boot.dev"})
    node3 = HTMLNode("<h1>", "This is a heading", children=[node, node2])

    def test_to_html(self):
        self.assertRaises(NotImplementedError)

    def test_values(self):
        self.assertEqual("hello world", self.node.value)
        self.assertEqual("This is a heading", self.node3.value)

    def test_props_to_html(self):
        html_node = self.node.props_to_html()
        html_node2 = self.node2.props_to_html()
        self.assertIn("", html_node)
        self.assertIn("href", html_node2)

    def test_output(self):
        self.assertIn("HTML Node(Tag: <a>,", f"{self.node2}")


if __name__ == "__main__":
    unittest.main()
