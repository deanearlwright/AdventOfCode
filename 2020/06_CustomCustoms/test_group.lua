-- ======================================================================
-- Custom Customs
--   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ g r o u p . l u a
-- ======================================================================
-- Test Group for Advent of Code 2020 day 06, Custom Customs

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local group = require('group')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = { "abcx", "abcy", "abcz" }

-- ======================================================================
--                                                              TestGroup
-- ======================================================================

function test_empty_init()
  -- Test the default Group creation

  -- 1. Create default Group object
  local myobj = group:Group()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.questions, 0)

end

function test_text_init()
  -- Test the Group object creation from text

  -- 1. Create Groups object from text
  local myobj = group:Group({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 3)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:count_yes(), 6)
  

end

function test_part2()
  -- Test the Group object creation from text for part2

  -- 1. Create Groups object from text
  local myobj = group:Group({part2=true, text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 3)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:count_yes(), 3)
  

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                    t e s t _ g r o u p . p y                   end
-- ======================================================================
