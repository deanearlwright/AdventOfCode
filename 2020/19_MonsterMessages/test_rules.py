# ======================================================================
# Monster Messages
#   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r u l e s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 19, Monster Messages"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import rules

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""
EXAMPLE_TWO = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 2
PART_TWO_RESULT = 12

# ======================================================================
#                                                              TestRules
# ======================================================================


class TestRules(unittest.TestCase):  # pylint: disable=R0904
    "Test Rules object"

    def test_empty_init(self):
        "Test the default Rules creation"

        # 1. Create default Rules object
        myobj = rules.Rules()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rules, {})
        self.assertEqual(myobj.messages, [])

    def test_text_init(self):
        "Test the Rules object creation from text"

        # 1. Create Rules object from text
        myobj = rules.Rules(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.rules), 6)
        self.assertEqual(len(myobj.messages), 5)

    def test_try_rules(self):
        "Test the Rules try_rules() method"

        # 1. Create Rules object from text
        myobj = rules.Rules(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.rules), 6)

        # 3. Check method
        self.assertEqual(myobj.try_rules('', 'a'), ['a'])
        self.assertEqual(myobj.try_rules('4', 'a'), [''])
        self.assertEqual(myobj.try_rules('4', 'b'), [])
        self.assertEqual(myobj.try_rules('4 4', 'aa'), [''])
        self.assertEqual(myobj.try_rules('4 4', 'aaa'), ['a'])
        self.assertEqual(myobj.try_rules('4 4', 'aab'), ['b'])
        self.assertEqual(myobj.try_rules('4 4', 'abb'), [])
        self.assertEqual(myobj.try_rules('5', 'a'), [])
        self.assertEqual(myobj.try_rules('5', 'b'), [''])
        self.assertEqual(myobj.try_rules('2', 'a'), [])
        self.assertEqual(myobj.try_rules('2', 'aa'), [''])
        self.assertEqual(myobj.try_rules('2', 'bbb'), ['b'])
        self.assertEqual(myobj.try_rules('2', 'ab'), [])
        self.assertEqual(myobj.try_rules('3', 'bb'), [])
        self.assertEqual(myobj.try_rules('3', 'ab'), [''])
        self.assertEqual(myobj.try_rules('1', 'a'), [])
        self.assertEqual(myobj.try_rules('1', 'aa'), [])
        self.assertEqual(myobj.try_rules('1', 'ab'), [])
        self.assertEqual(myobj.try_rules('1', 'aaaa'), [])
        self.assertEqual(myobj.try_rules('1', 'aaab'), [''])
        self.assertEqual(myobj.try_rules('1', 'bbaba'), ['a'])
        self.assertEqual(myobj.try_rules('1', 'abbb'), [''])
        self.assertEqual(myobj.try_rules('2 3', 'a'), [])
        self.assertEqual(myobj.try_rules('2 3', 'aa'), [])
        self.assertEqual(myobj.try_rules('2 3', 'bb'), [])
        self.assertEqual(myobj.try_rules('2 3', 'ab'), [])
        self.assertEqual(myobj.try_rules('2 3', 'aaaa'), [])
        self.assertEqual(myobj.try_rules('2 3', 'aaab'), [''])
        self.assertEqual(myobj.try_rules('2 3', 'bbaba'), ['a'])
        self.assertEqual(myobj.try_rules('2 3', 'abbb'), [])
        self.assertEqual(myobj.try_rules('3 2', 'abbb'), [''])
        self.assertEqual(myobj.try_rules('3 2', 'abaaa'), ['a'])
        self.assertEqual(myobj.try_rules('0', 'ab'), [])
        self.assertEqual(myobj.try_rules('0', 'aaaa'), [])
        self.assertEqual(myobj.try_rules('0', 'abbb'), [])
        self.assertEqual(myobj.try_rules('0', 'ababbb'), [''])
        self.assertEqual(myobj.try_rules('0', 'abbbab'), [''])
        self.assertEqual(myobj.try_rules('0', 'bababa'), [])
        self.assertEqual(myobj.try_rules('0', 'aaabbb'), [])
        self.assertEqual(myobj.try_rules('0', 'aaaabbb'), ['b'])
        self.assertEqual(myobj.try_rules('4 1 5', 'abbb'), [])
        self.assertEqual(myobj.try_rules('4 1 5', 'ababbb'), [''])
        self.assertEqual(myobj.try_rules('4 1 5', 'abbbab'), [''])
        self.assertEqual(myobj.try_rules('4 1 5', 'bababa'), [])
        self.assertEqual(myobj.try_rules('4 1 5', 'aaabbb'), [])
        self.assertEqual(myobj.try_rules('4 1 5', 'aaaabbb'), ['b'])

    def test_try_rule(self):
        "Test the Rules try_rule() method"

        # 1. Create Rules object from text
        myobj = rules.Rules(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.rules), 6)
        self.assertEqual(len(myobj.messages), 5)

        # 3. Check method
        self.assertEqual(myobj.try_rule(0, 'a'), [])
        self.assertEqual(myobj.try_rule(1, 'a'), [])
        self.assertEqual(myobj.try_rule(2, 'a'), [])
        self.assertEqual(myobj.try_rule(3, 'a'), [])
        self.assertEqual(myobj.try_rule(4, 'a'), [''])
        self.assertEqual(myobj.try_rule(5, 'a'), [])
        self.assertEqual(myobj.try_rule(5, 'b'), [''])
        self.assertEqual(myobj.try_rule(2, 'a'), [])
        self.assertEqual(myobj.try_rule(2, 'aa'), [''])
        self.assertEqual(myobj.try_rule(2, 'ab'), [])
        self.assertEqual(myobj.try_rule(2, 'bb'), [''])
        self.assertEqual(myobj.try_rule(2, 'aaaabb'), ['aabb'])
        self.assertEqual(myobj.try_rule(3, 'a'), [])
        self.assertEqual(myobj.try_rule(3, 'aa'), [])
        self.assertEqual(myobj.try_rule(3, 'ab'), [''])
        self.assertEqual(myobj.try_rule(3, 'bb'), [])
        self.assertEqual(myobj.try_rule(3, 'aaaabb'), [])
        self.assertEqual(myobj.try_rule(1, 'a'), [])
        self.assertEqual(myobj.try_rule(1, 'aa'), [])
        self.assertEqual(myobj.try_rule(1, 'ab'), [])
        self.assertEqual(myobj.try_rule(1, 'bb'), [])
        self.assertEqual(myobj.try_rule(1, 'aaaa'), [])
        self.assertEqual(myobj.try_rule(1, 'aaab'), [''])
        self.assertEqual(myobj.try_rule(1, 'abaa'), [''])
        self.assertEqual(myobj.try_rule(1, 'aaaabb'), [])
        self.assertEqual(myobj.try_rule(0, ''), [])
        self.assertEqual(myobj.try_rule(0, 'ababbb'), [''])
        self.assertEqual(myobj.try_rule(0, 'abbbab'), [''])
        self.assertEqual(myobj.try_rule(0, 'bababa'), [])
        self.assertEqual(myobj.try_rule(0, 'aaabbb'), [])
        self.assertEqual(myobj.try_rule(0, 'aaaabbb'), ['b'])

    def test_match_rule(self):
        "Test the Rules match_rule() method"

        # 1. Create Rules object from text
        myobj = rules.Rules(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.rules), 6)
        self.assertEqual(len(myobj.messages), 5)

        # 3. Check method
        self.assertEqual(myobj.match_rule(0, 'a'), False)
        self.assertEqual(myobj.match_rule(1, 'a'), False)
        self.assertEqual(myobj.match_rule(2, 'a'), False)
        self.assertEqual(myobj.match_rule(3, 'a'), False)
        self.assertEqual(myobj.match_rule(4, 'a'), True)
        self.assertEqual(myobj.match_rule(5, 'a'), False)
        self.assertEqual(myobj.match_rule(5, 'b'), True)
        self.assertEqual(myobj.match_rule(2, 'a'), False)
        self.assertEqual(myobj.match_rule(2, 'aa'), True)
        self.assertEqual(myobj.match_rule(2, 'ab'), False)
        self.assertEqual(myobj.match_rule(2, 'bb'), True)
        self.assertEqual(myobj.match_rule(2, 'aaaabb'), False)
        self.assertEqual(myobj.match_rule(3, 'a'), False)
        self.assertEqual(myobj.match_rule(3, 'aa'), False)
        self.assertEqual(myobj.match_rule(3, 'ab'), True)
        self.assertEqual(myobj.match_rule(3, 'bb'), False)
        self.assertEqual(myobj.match_rule(3, 'aaaabb'), False)
        self.assertEqual(myobj.match_rule(1, 'a'), False)
        self.assertEqual(myobj.match_rule(1, 'aa'), False)
        self.assertEqual(myobj.match_rule(1, 'ab'), False)
        self.assertEqual(myobj.match_rule(1, 'bb'), False)
        self.assertEqual(myobj.match_rule(1, 'aaaa'), False)
        self.assertEqual(myobj.match_rule(1, 'aaab'), True)
        self.assertEqual(myobj.match_rule(1, 'abaa'), True)
        self.assertEqual(myobj.match_rule(1, 'aaaabb'), False)
        self.assertEqual(myobj.match_rule(0, ''), False)
        self.assertEqual(myobj.match_rule(0, 'ababbb'), True)
        self.assertEqual(myobj.match_rule(0, 'abbbab'), True)
        self.assertEqual(myobj.match_rule(0, 'bababa'), False)
        self.assertEqual(myobj.match_rule(0, 'aaabbb'), False)
        self.assertEqual(myobj.match_rule(0, 'aaaabbb'), False)

    def test_part_one(self):
        "Test part one example of Rules object"

        # 1. Create Rules object from text
        myobj = rules.Rules(text=aoc_19.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Rules object"

        # 1. Create Rules object from text
        myobj = rules.Rules(part2=True, text=aoc_19.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r u l e s . p y                  end
# ======================================================================
