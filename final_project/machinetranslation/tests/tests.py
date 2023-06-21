import unittest
from translator import french_to_english, english_to_french

class test_english_to_french (unittest.TestCase):
    def test_e2f_correct(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_e2f_incorrect(self):
        self.assertNotEqual(english_to_french('Hello'), 'Pomme')

class test_french_to_english (unittest.TestCase):
    def test_f2e_correct(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_f2e_incorrect(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Apple')

unittest.main()