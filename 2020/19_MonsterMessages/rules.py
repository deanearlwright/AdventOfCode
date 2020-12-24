# ======================================================================
# Monster Messages
#   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r u l e s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rule

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Rules
# ======================================================================


class Rules(object):   # pylint: disable=R0902, R0205
    "Object for Monster Messages"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rules = {}
        self.messages = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        "Process the input text lines"

        # 1. Loop for all of the lines
        for line in text:

            # 2. If it is a rule, add the rule
            if line.find(':') > 0:
                new_rule = rule.Rule(text=line, part2=self.part2)
                self.rules[new_rule.number] = new_rule

            # 3. Else add the message
            else:
                self.messages.append(line)

    def try_rule(self, number, message, verbose=False):
        """Try to match the message against the specified rule,
        Returns [] on failure or list of chars to match"""

        if verbose:
            print("try_rule: Trying rule %d against %s" % (number, message))

        # 1. Get the rule in question
        rul = self.rules[number]

        # 2. If rule is "a" or "b", the message must start with that
        if rul.is_constant():
            if message and message[0] == rul.letter():
                return [message[1:]]
            if verbose:
                print('try_rule: Trying rule %d for "%s" does not match %s' %
                      (number, rul.letter(), message))
            return []

        # 3. Start with nothing
        result = []

        # 4. Try to match each (or only) alternate of the rule
        for alternative in rul.alternatives():
            if verbose:
                print("try_rule: Checking %s of rule %d against %s" %
                      (alternative, number, message))

            # 5. Try matchin and get the remainder of the message after matching
            remaining = self.try_rules(alternative, message, verbose=verbose)

            # 6. if match, remember what still needs to be matched
            if remaining:
                result += remaining

        # 7. Return the result of the matches (the remains of the rule)
        return result

    def try_rules(self, rule_nums, message, verbose=False):
        """Try to match a string of rules to the message,
        Returns [] on failure or list of chars to match"""

        if verbose:
            print("try_rules: Checking %s against %s" % (rule_nums, message))

        # 1. We want to match the entire message initially but
        #    as we match the rules we match against the remaining
        #    characters in the messages (which may have different possibilities)
        messages = [message]

        # 5. Loop for each rule in the (partial) rule definition
        for rule_num in rule_nums.split():
            rule_int = int(rule_num)

            # 6. Match each rule in the definition keeping track of what remains
            remains = []
            for msg in messages:
                remains += self.try_rule(rule_int, msg, verbose=verbose)

            # 7. If we matched nothing, this definition is a bust
            if not remains:
                if verbose:
                    print("try_rules: Unable to match rule %d against %s" % (rule_int, msg))
                return []

            # 8. What the rest of the rule must match next
            messages = remains

        # 9. Return what this rule definition did not match
        return messages

    def match_rule(self, number, message, verbose=False):
        "Returns true if the specified rule matches the message"

        if verbose:
            print("match_rule: Matching rule %d against %s" % (number, message))

        # 1. Loop for each match
        for match in self.try_rule(number, message, verbose=verbose):

            # 2. Return True if we have an exact match?
            if verbose:
                if match == '':
                    print('match_rule: Rule %d exactly matched %s' % (number, message))
                else:
                    print('match_rule: Rule %d left %s remaining of %s' % (number, match, message))
            if match == '':
                return True

        # 3. Nothing matched, return False
        return False

    def count_rule0(self, verbose=False, limit=0):
        "Count the number of messages that match rule 0:"

        # 1. Start with nothing
        assert limit >= 0
        result = 0

        # 2. Loop for all of the messages
        for message in self.messages:

            # 3. Count it if the message matches rule 0
            if self.match_rule(0, message, verbose=verbose):
                result += 1

        # 4. Return the count of the messages that match the specified rule
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.count_rule0(verbose=verbose, limit=limit)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Alter a few choice rules
        new_8 = rule.Rule(text="8: 42 | 42 8")
        new_11 = rule.Rule(text="11: 42 31 | 42 11 31")
        self.rules[8] = new_8
        self.rules[11] = new_11

        # 2. Return the solution for part two
        return self.count_rule0(verbose=verbose, limit=limit)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r u l e s . p y                       end
# ======================================================================
