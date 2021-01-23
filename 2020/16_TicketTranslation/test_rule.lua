-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ r u l e . l u a
-- ======================================================================
-- Test Rule for Advent of Code 2020 day 16, Ticket Translation

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local rule = require('rule')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "row: 6-11 or 33-44"

-- ======================================================================
--                                                               TestRule
-- ======================================================================

function test_empty_init()
  -- Test the default Rule creation

  -- 1. Create default Rule object
  local myobj = rule:Rule()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.name, '???')
  luaunit.assertEquals(#myobj.numbers, 0)

end

function test_text_init()
  -- Test the Rule object creation from text

  -- 1. Create Tickets object from text
  local myobj = rule:Rule({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT)
  luaunit.assertEquals(myobj.name, 'row')
  luaunit.assertEquals(#myobj.numbers, 4)
  luaunit.assertEquals(myobj.numbers[1], 6)
  luaunit.assertEquals(myobj.numbers[2], 11)
  luaunit.assertEquals(myobj.numbers[3], 33)
  luaunit.assertEquals(myobj.numbers[4], 44)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:is_valid(0), false)
  luaunit.assertEquals(myobj:is_valid(5), false)
  luaunit.assertEquals(myobj:is_valid(6), true)
  luaunit.assertEquals(myobj:is_valid(8), true)
  luaunit.assertEquals(myobj:is_valid(11), true)
  luaunit.assertEquals(myobj:is_valid(12), false)
  luaunit.assertEquals(myobj:is_valid(15), false)
  luaunit.assertEquals(myobj:is_valid(32), false)
  luaunit.assertEquals(myobj:is_valid(33), true)
  luaunit.assertEquals(myobj:is_valid(38), true)
  luaunit.assertEquals(myobj:is_valid(44), true)
  luaunit.assertEquals(myobj:is_valid(45), false)
  luaunit.assertEquals(myobj:is_valid(55), false)
  
  luaunit.assertEquals(myobj:are_all_valid({}), true)
  luaunit.assertEquals(myobj:are_all_valid({5}), false)
  luaunit.assertEquals(myobj:are_all_valid({5, 8}), false)
  luaunit.assertEquals(myobj:are_all_valid({8, 5}), false)
  luaunit.assertEquals(myobj:are_all_valid({8, 38}), true)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                     t e s t _ r u l e . p y                    end
-- ======================================================================
