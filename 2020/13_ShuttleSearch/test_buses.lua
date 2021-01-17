-- ======================================================================
-- Shuttle Search
--   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ b u s e s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 13, Shuttle Search

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local buses = require('buses')

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
939
7,13,x,x,59,x,31,19
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 295
local PART_TWO_RESULT = 1068781

-- ======================================================================
--                                                              TestBuses
-- ======================================================================


function test_empty_init()
  -- Test the default Buses creation

  -- 1. Create default Buses object
  local myobj = buses:Buses()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.earliest, 0)
  luaunit.assertEquals(#myobj.buses, 0)

end

function test_text_init()
  -- Test the Buses object creation from text

  -- 1. Create Buses object from text
  local myobj = buses:Buses({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 2)
  luaunit.assertEquals(myobj.earliest, 939)
  luaunit.assertEquals(#myobj.buses, 5)
  luaunit.assertEquals(myobj.buses[1].bid, 7)
  luaunit.assertEquals(myobj.buses[1].offset, 0)
  luaunit.assertEquals(myobj.buses[2].bid, 13)
  luaunit.assertEquals(myobj.buses[2].offset, 1)
  luaunit.assertEquals(myobj.buses[3].bid, 59)
  luaunit.assertEquals(myobj.buses[3].offset, 4)
  luaunit.assertEquals(myobj.buses[4].bid, 31)
  luaunit.assertEquals(myobj.buses[4].offset, 6)
  luaunit.assertEquals(myobj.buses[5].bid, 19)
  luaunit.assertEquals(myobj.buses[5].offset, 7)
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:waiting(), 295)
  luaunit.assertEquals(myobj:contest(), 1068781)

end

function test_part_two_examples()
  -- Test the multiple part 2 examples
  
  -- 1. The earliest timestamp that matches the list 17,x,13,19 is 3417
  local myobj = buses:Buses({text=from_text("0\n17,x,13,19")})
  luaunit.assertEquals(myobj:contest(), 3417)
  
  -- 2. 67,7,59,61 first occurs at timestamp 754018.
  myobj = buses:Buses({text=from_text("0\n67,7,59,61")})
  luaunit.assertEquals(myobj:contest(), 754018)
  
  -- 3. 67,x,7,59,61 first occurs at timestamp 779210.
  myobj = buses:Buses({text=from_text("0\n67,x,7,59,61")})
  luaunit.assertEquals(myobj:contest(), 779210)
  
  -- 4. 67,7,x,59,61 first occurs at timestamp 1261476.
  myobj = buses:Buses({text=from_text("0\n67,7,x,59,61")})
  luaunit.assertEquals(myobj:contest(), 1261476)
  
  -- 5. 1789,37,47,1889 first occurs at timestamp 1202161486.
  myobj = buses:Buses({text=from_text("0\n1789,37,47,1889")})
  luaunit.assertEquals(myobj:contest(), 1202161486)
end

function test_part_one()
  -- Test part one example of Buses object

  -- 1. Create Buses object from text
  local myobj = buses:Buses({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Buses object

  -- 1. Create Buses object from text
  local myobj = buses:Buses({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ b u s e s . l u a                  end
-- ======================================================================
