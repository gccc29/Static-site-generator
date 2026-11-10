import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    node = HTMLNode("p", "hello world")
    node2 = HTMLNode("a", props={"href": "https://www.boot.dev"})
    node3 = HTMLNode("h1", "This is a heading", children=[node, node2])

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
        self.assertIn("HTML Node(Tag: a,", f"{self.node2}")

    # LeafNode tests:
    leafnode = LeafNode("p", "Hello, world!")
    leafnode2 = LeafNode("a", "Link description", {"href": "https://www.boot.dev"})
    def test_leaf_to_html(self):
        self.assertEqual(self.leafnode.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(self.leafnode2.to_html(), '<a href="https://www.boot.dev">Link description</a>')

    def test_leaf_output(self):
        self.assertIn("Leaf Node(Tag:", f"{self.leafnode}")

    #Parent and child node tests:
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_nested_parents_only(self):
        parent1 = ParentNode("div", [])
        parent2 = ParentNode("span", [parent1])
        with self.assertRaises(ValueError) as cm:
            parent2.to_html()

    def test_to_html_multiple_children(self):
        child1 = LeafNode("b", "Child1")
        child2 = LeafNode("i", "Child2")
        child3 = LeafNode("a", "Child3", {"href": "https://www.boot.dev"})
        parent_inner = ParentNode("span", [child1, child2])
        parent_outer = ParentNode("div", [parent_inner, child3])
        self.assertEqual(parent_outer.to_html(),
            '<div><span><b>Child1</b><i>Child2</i></span><a href="https://www.boot.dev">Child3</a></div>')


if __name__ == "__main__":
    unittest.main()
