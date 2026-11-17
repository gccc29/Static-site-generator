import unittest

from src.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_one_heading(self):
        md = "# Heading 1\n\nWriting here"
        self.assertEqual(extract_title(md), "Heading 1")

    def test_two_headings(self):
        md = "# Heading 1\n\n## Heading 2\nSome writing here"
        self.assertEqual(extract_title(md), "Heading 1")

    def test_two_first_headings(self):
        md = "# Heading 1\n\n# Heading 2"
        self.assertEqual(extract_title(md), "Heading 1")
