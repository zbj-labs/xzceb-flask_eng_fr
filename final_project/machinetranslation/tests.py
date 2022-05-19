import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), None, 'None should return None')
        self.assertEqual(englishToFrench("Hello"), "Bonjour", "Hello should be translated to Bonjour")
        self.assertEqual(englishToFrench("Goodbye"), "Au revoir", "Goodbye should be translated to Au revoir")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), None, 'None should return None')
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello", "Bonjour should be translated to Hello")
        self.assertEqual(frenchToEnglish("Au revoir"), "Goodbye", "Au revoir should be translated to Goodbye")

unittest.main()

