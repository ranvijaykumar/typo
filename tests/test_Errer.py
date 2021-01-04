from unittest import TestCase
import typo
import datetime


class TestStrErrer(TestCase):
    def test_char_swap(self):
        self.assertEqual(typo.StrErrer('', seed=1).char_swap().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).char_swap().result, ' ')
        self.assertEqual(typo.StrErrer('a', seed=1).char_swap().result, 'a')
        self.assertEqual(typo.StrErrer('ab', seed=1).char_swap().result, 'ba')
        self.assertEqual(typo.StrErrer('abc', seed=1).char_swap().result, 'bac')
        self.assertEqual(typo.StrErrer('2021', seed=1).char_swap().result, '0221')
        self.assertEqual(typo.StrErrer('Hello World! Happy new year 2021.', seed=13).char_swap().result,
                         'Hello World! Ahppy new year 2021.')

    def test_missing_char(self):
        self.assertEqual(typo.StrErrer('', seed=1).missing_char().result, '')
        self.assertEqual(typo.StrErrer('  ', seed=1).missing_char().result, '  ')
        self.assertEqual(typo.StrErrer('a', seed=1).missing_char().result, 'a')
        self.assertEqual(typo.StrErrer('ab', seed=1).missing_char().result, 'b')
        self.assertEqual(typo.StrErrer('abcdefgh', seed=1).missing_char().result, 'abdefgh')
        self.assertEqual(typo.StrErrer('2021', seed=1).missing_char().result, '221')
        self.assertEqual(typo.StrErrer('Hello World! Happy new year 2021.', seed=2).missing_char().result,
                         'Hllo World! Happy new year 2021.')
        self.assertEqual(typo.StrErrer('Hello World! Happy new year 2021.', seed=7).missing_char().result,
                         'Hello World! appy new year 2021.')

    def test_extra_char(self):
        self.assertEqual(typo.StrErrer('', seed=1).extra_char().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).extra_char().result, ' ')
        self.assertEqual(typo.StrErrer('a', seed=1).extra_char().result, 'qa')
        self.assertEqual(typo.StrErrer('gh', seed=2).extra_char().result, 'fgh')
        self.assertEqual(typo.StrErrer('2021', seed=2).extra_char().result, '02021')
        self.assertEqual(typo.StrErrer('Hello World! Happy new year 2021.', seed=2).extra_char().result,
                         'Hrello World! Happy new year 2021.')
        self.assertEqual(typo.StrErrer('Hello World! Happy new year 2021.', seed=7).extra_char().result,
                         'Hello World! BHappy new year 2021.')

    def test_nearby_char(self):
        self.assertEqual(typo.StrErrer('', seed=1).nearby_char().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).nearby_char().result, ' ')
        self.assertEqual(typo.StrErrer('w', seed=1).nearby_char().result, 'e')
        self.assertEqual(typo.StrErrer('$fghh', seed=1).nearby_char().result, '$fbhh')
        self.assertEqual(typo.StrErrer('happy', seed=2).nearby_char().result, 'nappy')
        self.assertEqual(typo.StrErrer('Hello World! Happy new year 2021.', seed=5).nearby_char().result,
                         'Hello World! Happy new ysar 2021.')

    def test_similar_char(self):
        self.assertEqual(typo.StrErrer('', seed=1).similar_char().result, '')
        self.assertEqual(typo.StrErrer('Z', seed=1).similar_char().result, '2')
        self.assertEqual(typo.StrErrer('2021', seed=1).similar_char().result, '2D21')
        self.assertEqual(typo.StrErrer('Hello world! Happy new year 2021.', seed=1).similar_char().result,
                         'Hell0 world! Happy new year 2021.')
        self.assertEqual(typo.StrErrer('To be or not to be that is the question.', seed=2).similar_char().result,
                         'To be or not to be that is the questIon.')

    def test_skipped_space(self):
        self.assertEqual(typo.StrErrer('', seed=1).skipped_space().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).skipped_space().result, '')
        self.assertEqual(typo.StrErrer('  ', seed=1).skipped_space().result, ' ')
        self.assertEqual(typo.StrErrer('Hello world!', seed=1).skipped_space().result, 'Helloworld!')
        self.assertEqual(typo.StrErrer('Hello world! Happy new year 2021.', seed=5).skipped_space().result,
                         'Hello world! Happy new year2021.')

    def test_random_space(self):
        self.assertEqual(typo.StrErrer('', seed=1).random_space().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).random_space().result, ' ')
        self.assertEqual(typo.StrErrer('a', seed=1).random_space().result, ' a')
        self.assertEqual(typo.StrErrer('ab', seed=5).random_space().result, 'a b')
        self.assertEqual(typo.StrErrer('abcdefgh', seed=6).random_space().result, 'a bcdefgh')
        self.assertEqual(typo.StrErrer('2021', seed=5).random_space().result, '20 21')
        self.assertEqual(typo.StrErrer('Hello world! Happy new year 2021.', seed=634).random_space().result,
                         'Hell o world! Happy new year 2021.')

    def test_repeated_char(self):
        self.assertEqual(typo.StrErrer('', seed=1).repeated_char().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).repeated_char().result, ' ')
        self.assertEqual(typo.StrErrer('a', seed=1).repeated_char().result, 'aa')
        self.assertEqual(typo.StrErrer('ab', seed=2).repeated_char().result, 'aab')
        self.assertEqual(typo.StrErrer('abcdefgh', seed=5).repeated_char().result, 'abcdeefgh')
        self.assertEqual(typo.StrErrer('Hello world! Happy new year 2021.', seed=4).repeated_char().result,
                         'Hello worrld! Happy new year 2021.')

    def test_unichar(self):
        self.assertEqual(typo.StrErrer('', seed=1).unichar().result, '')
        self.assertEqual(typo.StrErrer(' ', seed=1).unichar().result, ' ')
        self.assertEqual(typo.StrErrer('  ', seed=1).unichar().result, ' ')
        self.assertEqual(typo.StrErrer('aa', seed=1).unichar().result, 'a')
        self.assertEqual(typo.StrErrer('apple', seed=1).unichar().result, 'aple')
        self.assertEqual(typo.StrErrer('aaabbbccc', seed=5).unichar().result, 'aaabbbcc')
        self.assertEqual(typo.StrErrer('Hello world! Happy new year 2021.', seed=1).unichar().result,
                         'Helo world! Happy new year 2021.')
        self.assertEqual(typo.StrErrer('Hello world! Happy new year 2021.', seed=5).unichar().result,
                         'Hello world! Hapy new year 2021.')


class TestIntErrer(TestCase):
    def test_digit_swap(self):
        self.assertEqual(typo.IntErrer(0, seed=1).digit_swap().result, 0)
        self.assertEqual(typo.IntErrer(1, seed=2).digit_swap().result, 1)
        self.assertEqual(typo.IntErrer(-1, seed=3).digit_swap().result, -1)
        self.assertEqual(typo.IntErrer(12, seed=4).digit_swap().result, 21)
        self.assertEqual(typo.IntErrer(-12, seed=5).digit_swap().result, -21)
        self.assertEqual(typo.IntErrer(1234567890, seed=6).digit_swap().result, 1324567890)
        self.assertEqual(typo.IntErrer(-1234567890, seed=7).digit_swap().result, -1234576890)

    def test_missing_digit(self):
        self.assertEqual(typo.IntErrer(0, seed=1).missing_digit().result, 0)
        self.assertEqual(typo.IntErrer(1, seed=2).missing_digit().result, 1)
        self.assertEqual(typo.IntErrer(-1, seed=3).missing_digit().result, -1)
        self.assertEqual(typo.IntErrer(12, seed=4).missing_digit().result, 2)
        self.assertEqual(typo.IntErrer(-12, seed=5).missing_digit().result, -1)
        self.assertEqual(typo.IntErrer(1234567890, seed=6).missing_digit().result, 123456789)
        self.assertEqual(typo.IntErrer(-1234567890, seed=7).missing_digit().result, -123457890)

    def test_extra_digit(self):
        self.assertEqual(typo.IntErrer(0, seed=1).extra_digit().result, 20)
        self.assertEqual(typo.IntErrer(1, seed=2).extra_digit().result, 41)
        self.assertEqual(typo.IntErrer(-1, seed=3).extra_digit().result, -21)
        self.assertEqual(typo.IntErrer(12, seed=4).extra_digit().result, 212)
        self.assertEqual(typo.IntErrer(-12, seed=5).extra_digit().result, -132)
        self.assertEqual(typo.IntErrer(1234567890, seed=6).extra_digit().result, 12345678920)
        self.assertEqual(typo.IntErrer(-1234567890, seed=7).extra_digit().result, -12345267890)

    def test_nearby_digit(self):
        self.assertEqual(typo.IntErrer(0, seed=1).nearby_digit().result, 2)
        self.assertEqual(typo.IntErrer(1, seed=2).nearby_digit().result, 4)
        self.assertEqual(typo.IntErrer(-1, seed=3).nearby_digit().result, -2)
        self.assertEqual(typo.IntErrer(12, seed=4).nearby_digit().result, 22)
        self.assertEqual(typo.IntErrer(-12, seed=5).nearby_digit().result, -13)
        self.assertEqual(typo.IntErrer(1234567890, seed=6).nearby_digit().result, 1234567892)
        self.assertEqual(typo.IntErrer(-1234567890, seed=7).nearby_digit().result, -1234527890)

    def test_similar_digit(self):
        self.assertEqual(typo.IntErrer(0, seed=1).similar_digit().result, 9)
        self.assertEqual(typo.IntErrer(1, seed=2).similar_digit().result, 7)
        self.assertEqual(typo.IntErrer(-1, seed=3).similar_digit().result, -7)
        self.assertEqual(typo.IntErrer(12, seed=4).similar_digit().result, 72)
        self.assertEqual(typo.IntErrer(-12, seed=5).similar_digit().result, -17)
        self.assertEqual(typo.IntErrer(1234567890, seed=6).similar_digit().result, 1234567896)
        self.assertEqual(typo.IntErrer(-1234567890, seed=7).similar_digit().result, -1234507890)

    def test_repeated_digit(self):
        self.assertEqual(typo.IntErrer(0, seed=1).repeated_digit().result, 0)
        self.assertEqual(typo.IntErrer(1, seed=2).repeated_digit().result, 11)
        self.assertEqual(typo.IntErrer(-1, seed=3).repeated_digit().result, -11)
        self.assertEqual(typo.IntErrer(12, seed=4).repeated_digit().result, 112)
        self.assertEqual(typo.IntErrer(-12, seed=5).repeated_digit().result, -122)
        self.assertEqual(typo.IntErrer(1234567890, seed=6).repeated_digit().result, 12345678900)
        self.assertEqual(typo.IntErrer(-1234567890, seed=7).repeated_digit().result, -12345667890)

    def test_unidigit(self):
        self.assertEqual(typo.IntErrer(0, seed=1).unidigit().result, 0)
        self.assertEqual(typo.IntErrer(1, seed=2).unidigit().result, 1)
        self.assertEqual(typo.IntErrer(-1, seed=3).unidigit().result, -1)
        self.assertEqual(typo.IntErrer(11, seed=4).unidigit().result, 1)
        self.assertEqual(typo.IntErrer(-11, seed=5).unidigit().result, -1)
        self.assertEqual(typo.IntErrer(111111, seed=6).unidigit().result, 11111)
        self.assertEqual(typo.IntErrer(112233445566, seed=7).unidigit().result, 11223445566)
        self.assertEqual(typo.IntErrer(-112233445566, seed=8).unidigit().result, -11233445566)


class TestDateErrer(TestCase):
    def test_date_month_swap(self):
        self.assertEqual(typo.DateErrer(datetime.datetime.strptime("8 Mar 95", "%d %b %y"),
                                        seed=1).date_month_swap().result, datetime.datetime(1995, 8, 3, 0, 0))
        self.assertEqual(typo.DateErrer(datetime.datetime.strptime("18 Mar 95", "%d %b %y"),
                                        seed=1).date_month_swap().result, datetime.datetime(1995, 3, 18, 0, 0))