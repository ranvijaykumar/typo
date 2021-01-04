import random
import re
import datetime
from typo.keyboardlayouts import en_default


class StrErrer:
    def __init__(self, value, seed=None):
        random.seed(seed)
        self.result = value

    def __repr__(self):
        return self.result

    # Swap two small, word characters in a string
    def char_swap(self):
        strval = self.result
        # all the locations where there are two consecutive alpanumeric characters.
        locations = [m.start() for m in re.finditer(r'(?=[\w]{2})', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            # Preserving the cases.
            firstchar = strval[location].upper() if strval[location + 1].isupper() else strval[location].lower()
            secondchar = strval[location + 1].upper() if strval[location].isupper() else strval[location + 1].lower()
            self.result = strval[:location] + secondchar + firstchar + strval[location + 2:]
        return self

    # Randomly skip a small, word character in a string.
    def missing_char(self):
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'[\w]', strval)]
        if len(locations) > 1:
            location = locations[random.randint(0, len(locations) - 1)]
            self.result = strval[:location] + strval[location + 1:]
        return self

    # Add an extra, nearby letter next to a word character
    def extra_char(self):
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'[\w]', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            trigger_char = strval[location]
            char_to_add = en_default.get_random_neighbor(trigger_char)
            self.result = strval[:location] + char_to_add + strval[location:]
        return self

    # Replace a character with nearby letter on keyboard
    def nearby_char(self):
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'[\w]', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            char_to_replace = strval[location]
            replace_with = en_default.get_random_neighbor(char_to_replace)
            # preserve case of the replaced character
            replace_with = replace_with.upper() if char_to_replace.isupper() else replace_with.lower()
            self.result = strval[:location] + replace_with + strval[location + 1:]
        return self

    # Replace a character with visually similar character
    def similar_char(self):
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'\w', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            char_to_replace = strval[location]
            replace_with = en_default.get_random_visually_similar_char(char_to_replace)
            self.result = strval[:location] + replace_with + strval[location + 1:]
        return self

    # Skip space from a sentence
    def skipped_space(self):
        strval = self.result
        spaces = [m.start() for m in re.finditer(' ', strval)]
        if len(spaces) > 0:
            to_skip = random.choice(spaces)
            self.result = strval[:to_skip] + strval[to_skip + 1:]
        return self

    # Adds random space in a sentence
    def random_space(self):
        strval = self.result
        # all the locations where there are non-space characters.
        locations = [m.start() for m in re.finditer(r'[^\s]', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            self.result = strval[:location] + ' ' + strval[location:]
        return self

    # Randomly repeat a word character
    def repeated_char(self):
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'[\w]', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            char_to_repeat = strval[location]
            self.result = strval[:location] + char_to_repeat + strval[location:]
        return self

    # Randomly replace a repeated letter with a single letter
    def unichar(self):
        strval = self.result
        repeats = [m.start() for m in re.finditer(r'(.)\1', strval)]
        if len(repeats) > 0:
            to_skip = random.choice(repeats)
            self.result = strval[:to_skip] + strval[to_skip + 1:]
        return self


class IntErrer:
    def __init__(self, value, seed=None):
        self.originalseed = seed
        random.seed(seed)
        # parse the integer
        if not isinstance(value, int):
            raise Exception("value: '" + value + "' is not an integer")
        # set sign and absolute value
        self.sign = pow(-1, int(value < 0))
        self.magnitude = abs(value)

    def __repr__(self):
        return self.result

    @property
    def result(self):
        return self.sign * self.magnitude

    # Swaps random two digits, and returns a valid integer
    def digit_swap(self):
        strval = str(self.magnitude)
        self.magnitude = int(StrErrer(strval, seed=self.originalseed).char_swap().result)
        return self

    # Randomly skip a digit.
    def missing_digit(self):
        strval = str(self.magnitude)
        self.magnitude = int(StrErrer(strval, seed=self.originalseed).missing_char().result)
        return self

    # Add an extra, nearby digit
    def extra_digit(self):
        strval = str(self.magnitude)
        self.magnitude = int(StrErrer(strval, seed=self.originalseed).extra_char().result)
        return self

    # Replaces a digit with a nearby digit on keyboard.
    def nearby_digit(self):
        strval = str(self.magnitude)
        self.magnitude = int(StrErrer(strval, seed=self.originalseed).nearby_char().result)
        return self

    # replaces with another visually similar digit
    def similar_digit(self):
        strval = str(self.magnitude)
        location = random.randint(0, len(strval) - 1)
        digit_to_replace = strval[location]
        replace_with = en_default.get_random_visually_similar_digit(digit_to_replace)
        self.magnitude = int(strval[:location] + replace_with + strval[location + 1:])
        return self

    # Randomly repeats a digit.
    def repeated_digit(self):
        strval = str(self.magnitude)
        self.magnitude = int(StrErrer(strval, seed=self.originalseed).repeated_char().result)
        return self

    # Randomly replace a repeated digit with a single one
    def unidigit(self):
        strval = str(self.magnitude)
        self.magnitude = int(StrErrer(strval, seed=self.originalseed).unichar().result)
        return self


class DateErrer:
    def __init__(self, value, seed=None):
        random.seed(seed)
        # parse the DateTime
        if not isinstance(value, datetime.datetime):
            raise Exception("value: '" + value + "' is not an datetime")
        self.result = value

    def __repr__(self):
        return self.result

    # swaps month and date, and returns a valid date
    def date_month_swap(self):
        if self.result.month < 13:
            self.result = self.result.replace(month=self.result.day, day=self.result.month)
        return self
