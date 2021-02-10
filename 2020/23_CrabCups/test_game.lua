-- ======================================================================
-- Crab Cups
--   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ g a m e . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 23, Crab Cups

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local game = require('game')

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
389125467
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = '67384529'
local PART_TWO_RESULT = 149245887792

-- ======================================================================
--                                                              TestGame
-- ======================================================================


function test_empty_init()
  -- Test the default Game creation

  -- 1. Create default Game object
  local myobj = game:Game()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.cups, 0)
  luaunit.assertEquals(myobj.current, 0)
  luaunit.assertEquals(myobj.maximum, 0)
  
  -- 3. Check methods
  luaunit.assertEquals(tostring(myobj), "cups: (0)")

end

function test_text_init()
  -- Test the Game object creation from text

  -- 1. Create Game object from text
  local myobj = game:Game({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 1)
  luaunit.assertEquals(#myobj.cups, 9)
  luaunit.assertEquals(myobj.current, 3)
  luaunit.assertEquals(myobj.maximum, 9)

  -- 3. Check methods
  luaunit.assertEquals(tostring(myobj), "cups: (3) 8  9  1  2  5  4  6  7 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (2) 8  9  1  5  4  6  7  3 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (5) 4  6  7  8  9  1  3  2 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (8) 9  1  3  4  6  7  2  5 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (4) 6  7  9  1  3  2  5  8 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (1) 3  6  7  9  2  5  8  4 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (9) 3  6  7  2  5  8  4  1 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (2) 5  8  3  6  7  4  1  9 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (6) 7  4  1  5  8  3  9  2 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (5) 7  4  1  8  3  9  2  6 ")
  myobj:move()
  luaunit.assertEquals(tostring(myobj), "cups: (8) 3  7  4  1  9  2  6  5 ")
  luaunit.assertEquals(myobj:labels(), '92658374')

end

function test_part_one()
  -- Test part one example of Game object

  -- 1. Create Game object from text
  local myobj = game:Game({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Game object

  -- 1. Create Game object from text
  local myobj = game:Game({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ g a m e . l u a                end
-- ======================================================================
