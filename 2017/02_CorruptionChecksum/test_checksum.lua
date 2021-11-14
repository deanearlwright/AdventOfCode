-- ======================================================================
-- Corruption Checksum
--   Advent of Code 2017 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ c h e c k s u m . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 02, Corruption Checksum

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local checksum = require('checksum')

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- Break the text into trimed, non-comment lines

  -- 1. We start with no lines
  local result = {}

  -- 2. Loop for lines in the text
  for line in text:gmatch('[^\r\n]+') do

    -- 3. But ignore blank and comment lines
    line = line:gsub("%s*$", "")
    if #line > 0 and "!" ~= line:sub(1, 1) then

      -- 4. Add the line
      table.insert(result, line)
    end
  end

  -- 5. Return a table of cleaned lines
  return result
end

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = [[
5 1 9 5
7 5 3
2 4 6 8
]]
local EXAMPLE_TWO = [[
5 9 2 8
9 4 7 3
3 8 6 5
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TWO

local PART_ONE_RESULT = 18
local PART_TWO_RESULT = 9

-- ======================================================================
--                                                           TestChecksum
-- ======================================================================

function test_empty_init()
  -- Test the default Checksum creation

  -- 1. Create default Checksum object
  local myobj = checksum:Checksum()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.rows, 0)

end

function test_text_init()
  -- Test the Checksum object creation from text

  -- 1. Create Checksum object from text
  local myobj = checksum:Checksum({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 3)
  luaunit.assertEquals(#myobj.rows, 3)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:row_min_max_diff(1), 8)
  luaunit.assertEquals(myobj:row_min_max_diff(2), 4)
  luaunit.assertEquals(myobj:row_min_max_diff(3), 6)
  
  luaunit.assertEquals(myobj:total(), 18)

end

function test_text_two()
  -- Test the Checksum object creation from text for part 2

  -- 1. Create Checksum object from text
  local myobj = checksum:Checksum({text=from_text(EXAMPLE_TWO), part2=true})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 3)
  luaunit.assertEquals(#myobj.rows, 3)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:row_div_even(1), 4)
  luaunit.assertEquals(myobj:row_div_even(2), 3)
  luaunit.assertEquals(myobj:row_div_even(3), 2)
  
  luaunit.assertEquals(myobj:total(), 9)

end

function test_part_one()
  -- Test part one example of Checksum object

  -- 1. Create Checksum object from text
  local myobj = checksum:Checksum({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Checksum object

  -- 1. Create Checksum object from text
  local myobj = checksum:Checksum({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                t e s t _ c h e c k s u m . l u a               end
-- ======================================================================
