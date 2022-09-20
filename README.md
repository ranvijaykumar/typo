# typo
typo is a python package to simulate typographical errors in English language. 

### Usage

```python
import typo
import datetime

myStrErrer = typo.StrErrer('Hello World! Happy new year 2021.', seed=2)
print(myStrErrer.missing_char().result)
# Should print 'Hllo World! Happy new year 2021.'

myStrErrer = typo.StrErrer('Hello World! Happy new year 2021.', seed=2)
print(myStrErrer.missing_char().char_swap().result)
# Should print 'Hlol World! Happy new year 2021.'

myIntErrer = typo.IntErrer(34343, seed=1)
print(myIntErrer.similar_digit().result)
# Should print 39343

myDateErrer = typo.DateErrer(datetime.datetime.strptime("8 Mar 95", "%d %b %y"))
print(myDateErrer.date_month_swap().result)
# Should print 1995-08-03 00:00:00
```
Currently, following types of typos can be simulated:

**String typos:** 

Given the input _Hello World! Happy new year 2021._, different error types produce the following errors.

| Error type    | Description                                                               | Output                             |
|---------------|---------------------------------------------------------------------------|------------------------------------|
| char_swap     | Swaps two random consecutive word characters in the string.               | Hello World! Ahppy new year 2021.  |
| missing_char  | Skips a random word character in the string.                              | Hllo World! Happy new year 2021.   |
| extra_char    | Adds an extra, keyboard-neighbor, letter next to a random word character. | Hrello World! Happy new year 2021. |
| nearby_char   | Replaces a random word character with keyboard-neighbor letter.           | Hello World! Happy new ysar 2021.  |
| similar_char  | Replaces a random word character with another visually similar character. | Hell0 world! Happy new year 2021.  |
| skipped_space | Skips a random space from the string.                                     | Hello world! Happy new year2021.   |
| random_space  | Adds a random space in the string.                                        | Hell o world! Happy new year 2021. |
| repeated_char | Repeats a random word character.                                          | Hello worrld! Happy new year 2021. |
| unichar       | Replaces a random consecutive repeated letter with a single letter.       | Hello world! Hapy new year 2021.   |

**Integer typos:** 

| Method         | Description                                                                    | Input         | Output       |
|----------------|--------------------------------------------------------------------------------|---------------|--------------|
| digit_swap     | Swaps two random consecutive digits in the integer.                            | 1234567890    | 1324567890   |
| missing_digit  | Skips a random digit in the integer.                                           | -1234567890   | -123457890   |
| extra_digit    | Adds an extra, keyboard-neighbor, digit next to a random digit in the integer. | 1234567890    | 12345678920  |
| nearby_digit   | Replaces a random digit in the integer with a keyboard-neighbor digit.         | 1234567890    | 1234567892   |
| similar_digit  | Replaces a random digit with another visually similar digit.                   | 1234567890    | 1234567896   |
| repeated_digit | Repeats a random digit in the integer.                                         | 1234567890    | 12345678900  |
| unidigit       | Replaces a random consecutive repeated digit with a single digit.              | -112233445566 | -11233445566 |

**Datetime typos:** 

| Method          | Description                                                                              | Input    | Output   |
|-----------------|------------------------------------------------------------------------------------------|----------|----------|
| date_month_swap | Swaps the day and month of the date if the value of the day is less than or equal to 12. | 8 Mar 95 | 3 Aug 95 |
