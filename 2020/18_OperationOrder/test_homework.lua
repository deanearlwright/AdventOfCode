-- ======================================================================
-- Operation Order
--   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ h o m e w o r k . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 18, Operation Order

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local homework = require('homework')

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
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 26 + 437 + 12240 + 13632
local PART_TWO_RESULT = 46 + 1445 + 669060 + 23340

-- ======================================================================
--                                                           TestHomework
-- ======================================================================


function test_empty_init()
  -- Test the default Homework creation

  -- 1. Create default Homework object
  local myobj = homework:Homework()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.expressions, 0)

end

function test_text_init()
  -- Test the Homework object creation from text

  -- 1. Create Homework object from text
  local myobj = homework:Homework({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 4)
  luaunit.assertEquals(#myobj.expressions, 4)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:evaluate_all(), PART_ONE_RESULT)

end

function test_part_one()
  -- Test part one example of Homework object

  -- 1. Create Homework object from text
  local myobj = homework:Homework({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Homework object

  -- 1. Create Homework object from text
  local myobj = homework:Homework({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                t e s t _ h o m e w o r k . l u a               end
-- ======================================================================
