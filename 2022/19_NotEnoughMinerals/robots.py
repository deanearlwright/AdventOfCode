
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o b o t s . p y
# ======================================================================
"Robots for the Advent of Code 2022 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Robots
# ======================================================================


class Robots(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Not Enough Minerals"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.robots = {}
        self.cost = {}
        self.useful = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

            self.cost = {
                "ore": {"ore": self.needs("ore", "ore")},
                "clay": {"ore": self.needs("clay", "ore")},
                "obsidian": {"ore": self.needs("obsidian", "ore"),
                             "clay": self.needs("obsidian", "clay")},
                "geode": {"ore": self.needs("geode", "ore"),
                          "obsidian": self.needs("geode", "obsidian")}
            }

            self.useful = {
                "ore": max(self.cost["clay"]["ore"],
                           self.cost["obsidian"]["ore"],
                           self.cost["geode"]["ore"]),
                "clay": self.cost["obsidian"]["clay"],
                "obsidian": self.cost["geode"]["obsidian"],
                "geode": 9999999 #float("inf")
            }

    def _process_text(self, text):
        "Assign values from text"

        # 1. Divide the text into sentences
        for sentence in text.split(". "):

            # 2. Create a robot from the sentence
            a_robot = robot.Robot(text=sentence, part2=self.part2)

            # 3. Add it to the blue print
            self.robots[a_robot.produces] = a_robot

    def needs(self, bot, what):
        "Return the costs of the robot"
        return self.robots[bot].needs(what)

    @staticmethod
    def names():
        "Return the names of the ingredients"
        return robot.Robot.names()

    def __len__(self):
        return len(self.robots)

    def __getitem__(self, index):
        return self.robots[index]

    def __contains__(self, index):
        return index in self.robots


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       r o b o t s . p y                     end
# ======================================================================
