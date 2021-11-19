-- ======================================================================
-- SpiralMemory
--   Advent of Code 2017 Day 03 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ s p i r a l . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 03, SpiralMemory

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local spiral = require('spiral')

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
1024
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 31
local PART_TWO_RESULT = 1968

-- ======================================================================
--                                                             TestSpiral
-- ======================================================================

function test_empty_init()
  -- Test the default Spiral creation

  -- 1. Create default Spiral object
  local myobj = spiral:Spiral()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.value, 0)
  luaunit.assertEquals(myobj.x, 0)
  luaunit.assertEquals(myobj.y, 0)
  luaunit.assertEquals(myobj.dir, "E")
  luaunit.assertEquals(myobj.steps, 1)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:location(), "0,0")
  luaunit.assertEquals(myobj:distance(), 0)
  myobj:grow()
  luaunit.assertEquals(myobj.x, 1)
  luaunit.assertEquals(myobj.y, 0)
  luaunit.assertEquals(myobj.dir, "N")
  luaunit.assertEquals(myobj.steps, 2)
  luaunit.assertEquals(myobj:location(), "1,0")
  luaunit.assertEquals(myobj:distance(), 1)
  myobj:grow()
  luaunit.assertEquals(myobj.x, 1)
  luaunit.assertEquals(myobj.y, 1)
  luaunit.assertEquals(myobj.dir, "W")
  luaunit.assertEquals(myobj.steps, 3)
  luaunit.assertEquals(myobj:location(), "1,1")
  luaunit.assertEquals(myobj:distance(), 2)
  myobj:grow()
  luaunit.assertEquals(myobj.x, 0)
  luaunit.assertEquals(myobj.y, 1)
  luaunit.assertEquals(myobj.dir, "W")
  luaunit.assertEquals(myobj.steps, 4)
  luaunit.assertEquals(myobj:location(), "0,1")
  luaunit.assertEquals(myobj:distance(), 1)
  myobj:grow()
  luaunit.assertEquals(myobj.x, -1)
  luaunit.assertEquals(myobj.y, 1)
  luaunit.assertEquals(myobj.dir, "S")
  luaunit.assertEquals(myobj.steps, 5)
  luaunit.assertEquals(myobj:location(), "-1,1")
  luaunit.assertEquals(myobj:distance(), 2)
  

end

function test_text_init()
  -- Test the Spiral object creation from text

  -- 1. Create Spiral object from text
  local myobj = spiral:Spiral({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 1)
  luaunit.assertEquals(myobj.value, 1024)
  luaunit.assertEquals(myobj.x, 0)
  luaunit.assertEquals(myobj.y, 0)
  luaunit.assertEquals(myobj.dir, "E")
  luaunit.assertEquals(myobj.steps, 1)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:grow_until(12), 3)
  luaunit.assertEquals(myobj:grow_until(23), 2)
  luaunit.assertEquals(myobj:grow_until(1024), 31)

end

function test_two_init()
  -- Test the Spiral object creation from text

  -- 1. Create Spiral object from text
  local myobj = spiral:Spiral({text=from_text(EXAMPLE_TEXT), part2=true})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 1)
  luaunit.assertEquals(myobj.value, 1024)
  luaunit.assertEquals(myobj.x, 0)
  luaunit.assertEquals(myobj.y, 0)
  luaunit.assertEquals(myobj.dir, "E")
  luaunit.assertEquals(myobj.steps, 1)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:location(), "0,0")
  luaunit.assertEquals(myobj.grid["0,0"], 1)
  myobj:grow()
  luaunit.assertEquals(myobj:location(), "1,0")
  luaunit.assertEquals(myobj.grid["1,0"], 1)
  myobj:grow()
  luaunit.assertEquals(myobj:location(), "1,1")
  luaunit.assertEquals(myobj.grid["1,1"], 2)

  luaunit.assertEquals(myobj:grow_until(12), 23)
  luaunit.assertEquals(myobj:grow_until(23), 25)
  luaunit.assertEquals(myobj:grow_until(1024), 1968)

end
function test_part_one()
  -- Test part one example of Spiral object

  -- 1. Create Spiral object from text
  local myobj = spiral:Spiral({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Spiral object

  -- 1. Create Spiral object from text
  local myobj = spiral:Spiral({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                  t e s t _ s p i r a l . l u a                 end
-- ======================================================================
