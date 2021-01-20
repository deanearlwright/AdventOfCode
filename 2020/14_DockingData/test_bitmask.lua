-- ======================================================================
-- Docking Data
--   Advent of Code 2020 Day 14 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ b i t m a s k . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 14, Docking Data

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local bitmask = require('bitmask')

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
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
]]
local EXAMPLE_TWO = [[
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TWO

local PART_ONE_RESULT = 165
local PART_TWO_RESULT = 208

-- ======================================================================
--                                                            TestBitmask
-- ======================================================================


function test_empty_init()
  -- Test the default Bitmask creation

  -- 1. Create default Bitmask object
  local myobj = bitmask:Bitmask()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.bitmask, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
  luaunit.assertEquals(#myobj.memory, 0)

end

function test_text_init()
  -- Test the Bitmask object creation from text

  -- 1. Create Bitmask object from text
  local myobj = bitmask:Bitmask({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 4)
  luaunit.assertEquals(myobj.bitmask, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
  luaunit.assertEquals(#myobj.memory, 0)

  -- 3. Check methods
  luaunit.assertEquals(myobj:execute(), 165)
  luaunit.assertEquals(myobj.bitmask, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
end

function test_part_one()
  -- Test part one example of Bitmask object

  -- 1. Create Bitmask object from text
  local myobj = bitmask:Bitmask({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Bitmask object

  -- 1. Create Bitmask object from text
  local myobj = bitmask:Bitmask({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ b i t m a s k . l u a                end
-- ======================================================================
