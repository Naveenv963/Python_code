import unittest
from justify_paragraph_text import justify_paragraph_string

class TestJustifyParagraph(unittest.TestCase):

    def test_justify_paragraph_string(self):
        paragraph = "This is a simple text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        page_width = 20
        expected_output = [
            "This is a simple",
            "text     but    a",
            "complicated  problem",
            "to be solved, so we",
            "are adding more text",
            "to     see    that   it",
            "actually     works."
        ]

        self.assertEqual(justify_paragraph_string(paragraph, page_width), expected_output)

    def test_single_word(self):
        paragraph = "Hello"
        page_width = 10
        expected_output = ["Hello"]
        self.assertEqual(justify_paragraph_string(paragraph, page_width), expected_output)

    def test_exact_fit(self):
        paragraph = "This fits exactly"
        page_width = 17
        expected_output = ["This fits exactly"]
        self.assertEqual(justify_paragraph_string(paragraph, page_width), expected_output)

    def test_long_word(self):
        paragraph = "Supercalifragilisticexpialidocious"
        page_width = 30
        expected_output = ["Supercalifragilisticexpialidocious"]
        self.assertEqual(justify_paragraph_string(paragraph, page_width), expected_output)

if __name__ == '__main__':
    unittest.main()
