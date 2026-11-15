import unittest

from src.extract_markdown import extract_markdown_images, extract_markdown_links

class TestMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            "This is text with an ![image2](https://i.imgur.com/zjjcJKZ.png2)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://i.imgur.com/zjjcJKZ.png2")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is ext with a [link](http://www.google.com)!!"
        )
        self.assertListEqual([("link", "http://www.google.com")], matches)
