-- ======================================================================
-- Binary Boarding
--   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ b p a s s . l u a
-- ======================================================================
-- "Test Bpass for Advent of Code 2020 day 05, Binary Boarding"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local bpass = require('bpass')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "FBFBBFFRLR"
local EXAMPLES = {
  { text = "BFFFBBFRRR", row=70, column=7, seat=567 },
  { text = "FFFBBBFRRR", row=14, column=7, seat=119 },
  { text = "BBFFBBFRLL", row=102, column=4, seat=820}
}

-- ======================================================================
--                                                             TestBpass
-- ======================================================================

function test_empty_init()
  -- "Test the default Bpass creation"

  -- 1. Create default Bpass object
  local myobj = bpass:Bpass()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.row, 0)
  luaunit.assertEquals(myobj.column, 0)
  luaunit.assertEquals(myobj.seat, 0)

end

function test_text_init()
  -- "Test the Bpass object creation from text"

  -- 1. Create Phone object from text
  local myobj = bpass:Bpass({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 10)
  luaunit.assertEquals(myobj.row, 44)
  luaunit.assertEquals(myobj.column, 5)
  luaunit.assertEquals(myobj.seat, 357)

end

function test_examples_one()
  -- Test multiple passports
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES) do
    
    -- 2. Create a passport from the example text
    local myobj = bpass:Bpass({text=example['text']})
    
    -- 3. Check the passport
    luaunit.assertEquals(myobj.row, example['row'])
    luaunit.assertEquals(myobj.column, example['column'])
    luaunit.assertEquals(myobj.seat, example['seat'])
  end
end
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ b p a s s . p y                end
-- ======================================================================
