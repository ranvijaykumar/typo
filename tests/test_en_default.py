from unittest import TestCase
from typo.keyboardlayouts import en_default


class Test(TestCase):
    def test_get_random_neighbor(self):
        self.assertEqual(en_default.get_random_neighbor('a', seed=1), 'w')
        self.assertEqual(en_default.get_random_neighbor('A', seed=2), 'Q')

    def test_get_random_visually_similar_char(self):
        self.assertEqual(en_default.get_random_visually_similar_char('a', seed=1), 'a')
        self.assertEqual(en_default.get_random_visually_similar_char('B', seed=2), '8')

    def test_get_random_visually_similar_digit(self):
        self.assertEqual(en_default.get_random_visually_similar_digit('0', seed=1), '6')
        self.assertEqual(en_default.get_random_visually_similar_digit('4', seed=2), '9')
