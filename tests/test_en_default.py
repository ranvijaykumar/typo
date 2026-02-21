from unittest import TestCase
from typo.keyboardlayouts import en_default


class Test(TestCase):
    def test_get_random_neighbor(self):
        self.assertEqual(en_default.get_random_neighbor('a', seed=1), 'w')
        self.assertEqual(en_default.get_random_neighbor('A', seed=2), 'Q')
        # Digit neighbors
        self.assertEqual(en_default.get_random_neighbor('5', seed=1), '8')
        self.assertEqual(en_default.get_random_neighbor('0', seed=1), '1')
        # Character not in the neighboring-letters map is returned unchanged
        self.assertEqual(en_default.get_random_neighbor('!', seed=1), '!')
        # Multi-character input raises an exception
        with self.assertRaises(Exception):
            en_default.get_random_neighbor('ab')

    def test_get_random_visually_similar_char(self):
        self.assertEqual(en_default.get_random_visually_similar_char('a', seed=1), 'a')
        self.assertEqual(en_default.get_random_visually_similar_char('B', seed=2), '8')
        # Character not in the similarity map is returned unchanged
        self.assertEqual(en_default.get_random_visually_similar_char('!', seed=1), '!')
        # Multi-character input raises an exception
        with self.assertRaises(Exception):
            en_default.get_random_visually_similar_char('ab')

    def test_get_random_visually_similar_digit(self):
        self.assertEqual(en_default.get_random_visually_similar_digit('0', seed=1), '6')
        self.assertEqual(en_default.get_random_visually_similar_digit('4', seed=2), '9')
        # Non-digit input raises an exception
        with self.assertRaises(Exception):
            en_default.get_random_visually_similar_digit('a')
        # Multi-character input raises an exception
        with self.assertRaises(Exception):
            en_default.get_random_visually_similar_digit('12')
