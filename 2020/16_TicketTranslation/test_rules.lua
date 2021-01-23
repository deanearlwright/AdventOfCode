-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ r u l e s . l u a
-- ======================================================================
-- Test Rules for Advent of Code 2020 day 16, Ticket Translation

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local rules = require('rules')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = {
  "class: 1-3 or 5-7",
  "row: 6-11 or 33-44",
  "seat: 13-40 or 45-50",
  "your ticket:",
  "7,1,14"
}


-- ======================================================================
--                                                              TestRules
-- ======================================================================

function test_empty_init()
  -- Test the default Rules creation

  -- 1. Create default Rules object
  local myobj = rules:Rules()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.rules, 0)

end

function test_text_init()
  -- Test the Rules object creation from text

  -- 1. Create Tickets object from text
  local myobj = rules:Rules({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 5)
  luaunit.assertEquals(#myobj.rules, 3)
  luaunit.assertEquals(myobj.rules[1].name, 'class')
  luaunit.assertEquals(myobj.rules[2].name, 'row')
  luaunit.assertEquals(myobj.rules[3].name, 'seat')
  luaunit.assertEquals(myobj.rules[1].numbers[1], 1)
  luaunit.assertEquals(myobj.rules[2].numbers[1], 6)
  luaunit.assertEquals(myobj.rules[3].numbers[1], 13)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:is_valid(0), false)
  luaunit.assertEquals(myobj:is_valid(2), true)
  luaunit.assertEquals(myobj:is_valid(4), false)
  luaunit.assertEquals(myobj:is_valid(55), false)
  luaunit.assertEquals(myobj:is_valid(12), false)
  luaunit.assertEquals(myobj:is_valid(7), true)
  luaunit.assertEquals(myobj:is_valid(3), true)
  luaunit.assertEquals(myobj:is_valid(47), true)
  
  luaunit.assertEquals(myobj:are_all_valid({7,3,47}), true)
  luaunit.assertEquals(myobj:are_all_valid({40,4,50}), false)
  luaunit.assertEquals(myobj:are_all_valid({55,2,20}), false)
  luaunit.assertEquals(myobj:are_all_valid({38,6,12}), false)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                    t e s t _ r u l e s . p y                   end
-- ======================================================================
