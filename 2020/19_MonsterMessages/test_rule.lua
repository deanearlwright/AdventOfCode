-- ======================================================================
-- Monster Messages
--   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ r u l e . l u a
-- ======================================================================
-- Test Rule for Advent of Code 2020 day 19, Monster Messages

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local rule = require('rule')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "1: 2 3 | 3 2"
local EXAMPLE_TEXT4 = '4: "a"'

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
  luaunit.assertEquals(myobj.number, nil)
  luaunit.assertEquals(myobj.definition, nil)
  

end

function test_text_init()
  -- Test the Rule object creation from text

  -- 1. Create Rules object from text
  local myobj = rule:Rule({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT)
  luaunit.assertEquals(myobj.number, "1")
  luaunit.assertEquals(myobj.definition, "2 3 | 3 2")
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:is_constant(), false)
  luaunit.assertEquals(myobj:alternatives(), {"2 3", "3 2"})
end

function test_rule4()
  -- Test the Rule object creation from text

  -- 1. Create Rules object from text
  local myobj = rule:Rule({text=EXAMPLE_TEXT4})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT4)
  luaunit.assertEquals(myobj.number, "4")
  luaunit.assertEquals(myobj.definition, '"a"')
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:is_constant(), true)
  luaunit.assertEquals(myobj:letter(), "a")
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ r u l e . p y                end
-- ======================================================================
