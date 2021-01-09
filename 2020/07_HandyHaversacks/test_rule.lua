-- ======================================================================
-- Handy Haversacks
--   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ r u l e . l u a
-- ======================================================================
-- Test Rule for Advent of Code 2020 day 07, Handy Haversacks

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local rule = require('rule')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "light red bags contain 1 bright white bag, 2 muted yellow bags."

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

end

function test_text_init()
  -- Test the Rule object creation from text

  -- 1. Create Rules object from text
  local myobj = rule:Rule({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, #EXAMPLE_TEXT)
  luaunit.assertEquals(myobj.bag, "light red")
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:contains("bright white"), 1)
  luaunit.assertEquals(myobj:contains("muted yellow"), 2)
  luaunit.assertEquals(myobj:contains("forest green"), 0)
  luaunit.assertEquals(myobj:contains("light red"), 0)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                     t e s t _ r u l e . p y                    end
-- ======================================================================
