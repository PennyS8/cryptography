import unittest
import helper

class TestCleanText(unittest.TestCase):
    def test_basic_string():
        # Test case 1: Basic scenario with punctuation
        text = "Hello, World!"

        # Run function for actual results
        cleaned_text, punct_index_map = helper.clean_text(text)

        # Expected results
        expected_text = "HelloWorld"
        expected_index_map = {',':[5], '!':[11]}

        # assert expected, actual equality
        assert expected_text == cleaned_text, f'__Failed to clean text__\nexpected_text: {expected_text}\nactual_text: {cleaned_text}'
        assert expected_index_map == punct_index_map, f'__Failed to clean text__\nexpected_index_map: {expected_index_map}\nactual_index_map: {punct_index_map}'

    def test_nums_and_special_chars():
        # Test case 2: Scenario with numbers and special characters
        text_2 = "This is a test string with 123 and special characters !@#"
        expected_cleaned_text_2 = "Thisisateststringwithandspecialcharacters"
        expected_punctuation_list_2 = {'!':[41], '@':[42], '#':[43]}
        cleaned_text_2, punctuation_list_2 = helper.clean_text(text_2)
        assert cleaned_text_2 == expected_cleaned_text_2
        assert punctuation_list_2 == expected_punctuation_list_2

    def test_only_punctuation():
        # Test case 3: Scenario with only punctuation
        text_3 = "!@#$%^&*()"
        expected_cleaned_text_3 = ""
        expected_punctuation_list_3 = {'!':[0], '@':[1], '#':[2], '$':[3], '%':[4], '^':[5], '&':[6], '*':[7], '(':[8], ')':[9]}
        cleaned_text_3, punctuation_list_3 = helper.clean_text(text_3)
        assert cleaned_text_3 == expected_cleaned_text_3
        assert punctuation_list_3 == expected_punctuation_list_3

    def test_only_alphabets():
        # Test case 4: Scenario with only alphabets
        text_4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        expected_cleaned_text_4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        expected_punctuation_list_4 = {}
        cleaned_text_4, punctuation_list_4 = helper.clean_text(text_4)
        assert cleaned_text_4 == expected_cleaned_text_4
        assert punctuation_list_4 == expected_punctuation_list_4
'''
    def main():
        basic_string()
        nums_and_special_chars()
        only_punctuation()
        only_alphabets()
        
        print('All tests passed!')
'''
if __name__ == '__main__':
    unittest.main()