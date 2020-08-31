# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ p e r s o n . p y
# ======================================================================
"Test persons and people for Advent of Code 2018 day 15, Beverage Bandits"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import person

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             TestPerson
# ======================================================================


class TestPerson(unittest.TestCase):  # pylint: disable=R0904
    "Test Person object"

    def test_empty_init(self):
        "Test the default Person creation"

        # 1. Create default Person object
        myobj = person.Person()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.letter, '#')
        self.assertEqual(myobj.location, 0)
        self.assertEqual(myobj.hitpoints, 200)
        self.assertEqual(myobj.attack, 3)

    def test_value_init(self):
        "Test the Person object creation with values"

        # 1. Create Combat object from text
        myobj = person.Person(letter='E', location=203)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.letter, 'E')
        self.assertEqual(myobj.location, 203)
        self.assertEqual(myobj.hitpoints, 200)
        self.assertEqual(myobj.attack, 3)

        # 3. Check distance and adjacent
        self.assertEqual(myobj.distance(406), 2+3)
        self.assertEqual(myobj.adjacent(), [103, 202, 204, 303])

# ======================================================================
#                                                             TestPeople
# ======================================================================


class TestPeople(unittest.TestCase):  # pylint: disable=R0904
    "Test People object"

    def test_empty_init(self):
        "Test the default Person creation"

        # 1. Create default People object
        myobj = person.People()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.letter, '#')
        self.assertEqual(len(myobj.persons), 0)
        self.assertEqual(len(myobj), 0)

    def test_value_init(self):
        "Test the Person object creation with values"

        # 1. Create Combat object from text
        myobj = person.People(letter='E')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.letter, 'E')
        self.assertEqual(len(myobj), 0)

        # 3. Check add
        person1 = person.Person(letter='E', location=304)
        person2 = person.Person(letter='E', location=404)
        myobj.add(person1)
        myobj.add(person2)
        self.assertEqual(len(myobj), 2)

        # 4. Check locations
        person3 = person.Person(letter='E', location=201)
        myobj.add(person3)
        self.assertEqual(len(myobj), 3)
        self.assertEqual(myobj.locations(), [201, 304, 404])

        # 5. Check in
        self.assertEqual(101 in myobj, False)
        self.assertEqual(201 in myobj, True)

        # 6. Check hitpoints
        self.assertEqual(myobj.hitpoints(), 600)
        person1.attacks(person2)
        person1.attacks(person2)
        person1.attacks(person2)
        self.assertEqual(myobj.hitpoints(), 591)
        person2.hitpoints = 2
        self.assertEqual(myobj.hitpoints(), 402)
        person1.attacks(person2)
        self.assertEqual(myobj.hitpoints(), 400)



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p e r s o n . p y                  end
# ======================================================================
