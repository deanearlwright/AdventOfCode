-- ======================================================================
-- Rain Risk
--   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ n a v i g a t i o n . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 12, Rain Risk

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local navigation = require('navigation')

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
F10
N3
F7
R90
F11
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 25
local PART_TWO_RESULT = 286

-- ======================================================================
--                                                         TestNavigation
-- ======================================================================


function test_empty_init()
  -- Test the default Navigation creation

  -- 1. Create default Navigation object
  local myobj = navigation:Navigation()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.ferry.facing, 1)

end

function test_text_init()
  -- Test the Navigation object creation from text

  -- 1. Create Navigation object from text
  local myobj = navigation:Navigation({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 5)
  luaunit.assertEquals(myobj.ferry.facing, 1)

end

function test_part_one()
  -- Test part one example of Navigation object

  -- 1. Create Navigation object from text
  local myobj = navigation:Navigation({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Navigation object

  -- 1. Create Navigation object from text
  local myobj = navigation:Navigation({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end              t e s t _ n a v i g a t i o n . l u a             end
-- ======================================================================
