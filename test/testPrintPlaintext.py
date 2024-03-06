import unittest
import cipherCalcs.helper as helper

class TestPrintPlaintext(unittest.TestCase):
    def test_basic_string(self):
        text = "Hello, World!"
        punct_index_map = {',':[5], '!':[11]}
        expected_text = "Hello, World!"
        self.assertEqual(expected_text, helper.print_plaintext(text, punct_index_map))

    def test_nums_and_special_chars(self):
        text = "This is a test string with 123 and special characters !@#"
        punct_index_map = {'!':[41], '@':[42], '#':[43]}
        expected_text = "This is a test string with 123 and special characters !@#"
        self.assertEqual(expected_text, helper.print_plaintext(text, punct_index_map))

    def test_only_punctuation(self):
        text = "!@#$%^&*()"
        punct_index_map = {'!':[0], '@':[1], '#':[2], '$':[3], '%':[4], '^':[5], '&':[6], '*':[7], '(':[8], ')':[9]}
        expected_text = "!@#$%^&*()"
        self.assertEqual(expected_text, helper.print_plaintext(text, punct_index_map))

    def test_empty_string(self):
        text = ""
        punct_index_map = {}
        expected_text = ""
        self.assertEqual(expected_text, helper.print_plaintext(text, punct_index_map))

if __name__ == '__main__':
    unittest.main()