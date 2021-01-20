-- ======================================================================
-- Rambunctious Recitation
--   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ m e m o r y . l u a
-- ======================================================================
-- Test Memory for Advent of Code 2020 day 15, Rambunctious Recitation

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local memory = require('memory')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "0,3,6"
local EXAMPLE_AGES = "0,3,3,1,0,4,0"

-- ======================================================================
--                                                             TestMemory
-- ======================================================================

function test_empty_init()
  -- Test the default Memory creation

  -- 1. Create default Memory object
  local myobj = memory:Memory()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.age, nil)
  luaunit.assertEquals(myobj.turn, 0)
  luaunit.assertEquals(#myobj.numbers, 0)

end

function test_text_init()
  -- Test the Memory object creation from text

  -- 1. Create Game object from text
  local myobj = memory:Memory({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 5)
  luaunit.assertEquals(myobj.age, 0)
  luaunit.assertEquals(myobj.turn, 3)
  luaunit.assertEquals(myobj.numbers[0], 1)
  luaunit.assertEquals(myobj.numbers[3], 2)
  luaunit.assertEquals(myobj.numbers[6], 3)
  
  -- 3. Speak more numbers
  for age in EXAMPLE_AGES:gmatch("[0-9]+") do
    age = tonumber(age)
    luaunit.assertEquals(myobj.age, age)
    myobj:add(age)
  end
  
  -- 4. Final check
  luaunit.assertEquals(myobj.turn, 10)
  luaunit.assertEquals(myobj.age, 2)
  
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ m e m o r y . p y                  end
-- ======================================================================
