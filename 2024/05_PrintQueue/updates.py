
# ======================================================================
# Print Queue
#   Advent of Code 2024 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         u p d a t e s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def middle(pages):
    "Get the middle number of a set of pages"
    plen = len(pages)
    if plen % 2 == 0:
        print("Asked for middle of even number of pages")
    return pages[plen // 2]


def is_afters(pages, before, afters):
    "Are all the afters OK"

    # 1. Get the index of before
    bindx = pages.index(before)

    # 2. Loop for all of the afters
    for after in afters:

        # 3. If after is also in the pages, it must be after the before
        if after in pages:
            aindx = pages.index(after)
            if aindx < bindx:
                return False

    # 4. Every thing is in order
    return True


def correct_afters(pages, before, afters):
    "Reorder the pages so that the afters are all after the before"

    # 1. Get the index of before
    bindx = pages.index(before)
    initial_len = len(pages)

    # 2. Loop for all of the afters
    for after in afters:

        # 3. If after is also in the pages, it must be after the before
        if after in pages:
            aindx = pages.index(after)
            if aindx < bindx:

                # 4. Move the after to after the before
                pages[bindx] = after
                pages[aindx] = before
                bindx = aindx
                # pages = pages[0:aindx] + pages[aindx + 1:bindx] + \
                #    [pages[bindx]] + [pages[aindx]] + pages[bindx + 1:]

    # 5. Return the updated pages
    assert initial_len == len(pages)
    return pages


# ======================================================================
#                                                                Updates
# ======================================================================


class Updates(object):   # pylint: disable=R0902, R0205
    "Object for Print Queue"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rules = {}
        self.pages = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for each line in the text
        for line in text:

            # 2. If it contains a vertical bar, process rule
            if "|" in line:
                before, after = [int(x) for x in line.split("|")]
                if before in self.rules:
                    self.rules[before].append(after)
                else:
                    self.rules[before] = [after]
                continue

            # 3. Else process pages to produce in the update
            pages = [int(x) for x in line.split(",")]
            self.pages.append(pages)

    def is_ordered(self, pages):
        "Return True if pages are in the correct order"

        # 1. Loop for all the rules
        for before, afters in self.rules.items():

            # 2. If the before in the pages?
            if before in pages:

                # 3. Are the afters OK
                if not is_afters(pages, before, afters):
                    return False

        # 4. All looks good
        return True

    def correct_order_once(self, pages):
        "Correct the page ordering"

        # 1. Loop for all the rules
        for before, afters in self.rules.items():

            # 2. If the before in the pages?
            if before in pages:

                # 3. Make the pages correct for this rule
                pages = correct_afters(pages, before, afters)

        # 4. Should be good to go now
        return pages

    def correct_order_multiple(self, pages):
        "Keep correcting until we get it right"

        # 1. Prevent run away sorting
        knt = 0

        # 2. Loop until perfection
        while not self.is_ordered(pages):

            # 3. Fix up the pages
            pages = self.correct_order_once(pages)

            # 4. Are we lost?
            knt += 1
            if knt > len(pages):
                print("Too far gone", knt, pages)
                return pages

        # 5. All is well
        return pages

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0
        if not self.text:
            return None

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the sets of pages
        for pages in self.pages:

            # 3. If the pages are correctly ordered, accumulate the middle page number
            if self.is_ordered(pages):
                result += middle(pages)

        # 4. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0
        if not self.text:
            return None

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the sets of pages
        for pages in self.pages:

            # 3. If the pages are not correctly ordered, fix them
            if not self.is_ordered(pages):
                pages = self.correct_order_multiple(pages)
                result += middle(pages)

        # 4. Return the solution for part one
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       u p d a t e s . p y                      end
# ======================================================================
