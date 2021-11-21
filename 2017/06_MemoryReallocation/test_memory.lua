-- ======================================================================
-- MemoryReallocation
--   Advent of Code 2017 Day 06 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ m e m o r y . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 06, MemoryReallocation

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local memory = require('memory')

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
0 2 7 0
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 5
local PART_TWO_RESULT = 4

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
  luaunit.assertEquals(#myobj.banks, 0)
  luaunit.assertEquals(#myobj.history, 0)

end

function test_text_init()
  -- Test the Memory object creation from text

  -- 1. Create Memory object from text
  local myobj = memory:Memory({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 1)
  luaunit.assertEquals(#myobj.banks, 4)
  luaunit.assertEquals(#myobj.history, 1)
  luaunit.assertEquals(myobj.history[1], "0,2,7,0")

-- 3. Check methods
  luaunit.assertEquals(myobj:most_blocks(), 3)
  luaunit.assertEquals(myobj:next_bank(3), 4)
  luaunit.assertEquals(myobj:next_bank(4), 1)
  
  myobj:redistribute(3)
  luaunit.assertEquals(#myobj.history, 2)
  luaunit.assertEquals(myobj.history[2], "2,4,1,2")
  luaunit.assertEquals(myobj:deja_vu(), 2)
  
  luaunit.assertEquals(myobj:most_blocks(), 2)
  myobj:redistribute(2)
  luaunit.assertEquals(#myobj.history, 3)
  luaunit.assertEquals(myobj.history[3], "3,1,2,3")
  luaunit.assertEquals(myobj:deja_vu(), 3)
  
  luaunit.assertEquals(myobj:most_blocks(), 1)
  myobj:redistribute(1)
  luaunit.assertEquals(#myobj.history, 4)
  luaunit.assertEquals(myobj.history[4], "0,2,3,4")
  luaunit.assertEquals(myobj:deja_vu(), 4)
  
  luaunit.assertEquals(myobj:most_blocks(), 4)
  myobj:redistribute(4)
  luaunit.assertEquals(#myobj.history, 5)
  luaunit.assertEquals(myobj.history[5], "1,3,4,1")
  luaunit.assertEquals(myobj:deja_vu(), 5)
  
  luaunit.assertEquals(myobj:most_blocks(), 3)
  myobj:redistribute(3)
  luaunit.assertEquals(#myobj.history, 6)
  luaunit.assertEquals(myobj.history[6], "2,4,1,2")
  luaunit.assertEquals(myobj:deja_vu(), 2)

end

function test_part_one()
  -- Test part one example of Memory object

  -- 1. Create Memory object from text
  local myobj = memory:Memory({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Memory object

  -- 1. Create Memory object from text
  local myobj = memory:Memory({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                  t e s t _ m e m o r y . l u a                 end
-- ======================================================================
