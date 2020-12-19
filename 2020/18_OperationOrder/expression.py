# ======================================================================
# Operation Order
#   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        e x p r e s s i o n . p y
# ======================================================================
"An Expression object for the Advent of Code 2020 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Expression
# ======================================================================


class Expression(object):   # pylint: disable=R0902, R0205
    "Object for Operation Order"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.tokens = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.tokens = text.replace('+', ' + ').replace('-', ' - ').replace('(', ' ( ').replace(')', ' ) ').split()

    def evaluate(self):
        "Returns the result of the expression"

        # 1. Return the result of evaluating the tokens
        return int(self.evaluate_tokens(self.tokens)[0])

    def evaluate_tokens(self, tokens):
        "Evaluate the tokens"

        # 1. Get the next operand
        #print('evaluate_tokens %s' % tokens)
        left, tokens = self.get_operand(tokens, '+')
        if len(left) == 1:
            left_value = int(left[0])
        else:
            left_value = int(self.evaluate_tokens(left)[0])
        if len(tokens) == 0:
            return [str(left_value)]

        # 2. Get the operation
        operation, tokens = self.get_operation(tokens)

        # 3. Get the other operand
        right, tokens = self.get_operand(tokens, operation)
        if len(right) == 1:
            right_value = int(right[0])
        else:
            right_value = int(self.evaluate_tokens(right)[0])

        # 4. Execute the operation
        if operation == '+':
            result = left_value + right_value
        else:
            result = left_value * right_value

        # 5. If no more tokens, we are done
        if len(tokens) == 0:
            return [str(result)]
        else:
            more = [str(result)]
            more.extend(tokens)
            final = self.evaluate_tokens(more)
            return final

    def get_operand(self, tokens, last_op):
        "Get the next operand"

        # 0. Precondition axioms
        assert len(tokens) > 0

        # 1. Easy to handle single token
        if len(tokens) == 1:
            return tokens, []

        # 2. Get operand token(s)
        if self.part2 and last_op == '*':
            operand = self.evaluate_tokens(tokens)
            tokens = []
        elif tokens[0] == '(':
            operand, tokens = self.get_paren(tokens[1:])
        else:
            operand = [tokens[0]]
            tokens = tokens[1:]

        return operand, tokens

    def get_operation(self, tokens):
        "Get the next operation"

        return tokens[0], tokens[1:]

    def get_paren(self, tokens):
        "Return the expression with the outer parens removed and the rest of the tokens"

        # 1. Start with nothing
        within = []
        depth = 0

        # 2. Loop until we find the closing paren
        for index, token in enumerate(tokens):

            # 3. If this is the closing paren, return left and remaing tokens
            if token == ')' and depth == 0:
                #print('parens of ( %s: within=%s' % (tokens, within))
                return within, tokens[index + 1:]

            # 4. If a closing paren but not the closing paren, decrease paren depth
            elif token == ')':
                depth -= 1
                assert depth >= 0

            # 5. If an opening paren, increase paren depth
            elif token == '(':
                depth += 1

            # 6. Add token to within
            within.append(token)

        # 7. Never found closing paren
        print('Unable to find closing paren at depth %d in %s' % (depth, tokens))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    e x p r e s s i o n . p y                   end
# ======================================================================
