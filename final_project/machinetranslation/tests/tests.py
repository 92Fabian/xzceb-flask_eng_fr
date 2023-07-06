"""
Module: tests
Unit tests for translation functions.
"""

import unittest
from translator import englishToFrench, frenchToEnglish

class TranslationTests(unittest.TestCase):
    """
    Test cases for translation functions.
    """

    def test_english_to_french_translation(self):
        """
        Test the translation of English to French.
        """
        english_text = 'Hello'
        french_translation = englishToFrench(english_text)
        expected_translation = 'Bonjour'
        self.assertEqual(french_translation, expected_translation)

    def test_french_to_english_translation(self):
        """
        Test the translation of French to English.
        """
        french_text = 'Bonjour'
        english_translation = frenchToEnglish(french_text)
        expected_translation = 'Hi'
        self.assertEqual(english_translation, expected_translation)

if __name__ == '__main__':
    unittest.main()
