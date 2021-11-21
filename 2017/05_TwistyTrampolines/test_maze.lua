-- ======================================================================
-- TwistyTrampolines
--   Advent of Code 2017 Day 05 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ m a z e . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 05, TwistyTrampolines

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local maze = require('maze')

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
0
3
0
1
-3
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 5
local PART_TWO_RESULT = 10

-- ======================================================================
--                                                               TestMaze
-- ======================================================================

function test_empty_init()
  -- Test the default Maze creation

  -- 1. Create default Maze object
  local myobj = maze:Maze()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.numbers, 0)

end

function test_text_init()
  -- Test the Maze object creation from text

  -- 1. Create Maze object from text
  local myobj = maze:Maze({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 5)
  luaunit.assertEquals(#myobj.numbers, 5)

end

function test_part_one()
  -- Test part one example of Maze object

  -- 1. Create Maze object from text
  local myobj = maze:Maze({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)
  luaunit.assertEquals(myobj.numbers[1], 2)
  luaunit.assertEquals(myobj.numbers[2], 5)
  luaunit.assertEquals(myobj.numbers[3], 0)
  luaunit.assertEquals(myobj.numbers[4], 1)
  luaunit.assertEquals(myobj.numbers[5], -2)
end

function test_part_two()
  -- Test part two example of Maze object

  -- 1. Create Maze object from text
  local myobj = maze:Maze({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)
  luaunit.assertEquals(myobj.numbers[1], 2)
  luaunit.assertEquals(myobj.numbers[2], 3)
  luaunit.assertEquals(myobj.numbers[3], 2)
  luaunit.assertEquals(myobj.numbers[4], 3)
  luaunit.assertEquals(myobj.numbers[5], -1)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                    t e s t _ m a z e . l u a                   end
-- ======================================================================
