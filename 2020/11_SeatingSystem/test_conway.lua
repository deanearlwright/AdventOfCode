-- ======================================================================
-- Seating System
--   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ c o n w a y . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 11, Seating System

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local conway = require('conway')

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
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 37
local PART_TWO_RESULT = 26

-- ======================================================================
--                                                             TestConway
-- ======================================================================


function test_empty_init()
  -- Test the default Conway creation

  -- 1. Create default Conway object
  local myobj = conway:Conway()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.seats, 0)

end

function test_text_init()
  -- Test the Conway object creation from text

  -- 1. Create Conway object from text
  local myobj = conway:Conway({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 10)
  luaunit.assertEquals(#myobj.seats, 10)
  luaunit.assertEquals(#myobj.seats[1], 10)
  
  -- 3. Test methods
  -- myobj:show(0)
  luaunit.assertEquals(myobj:count_occupied(), 0)
  luaunit.assertEquals(myobj:seat(1, 1), 'L')
  luaunit.assertEquals(myobj:neighbors(1, 1), 0)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 1
  -- myobj:show(1)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 2)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 2
  -- myobj:show(2)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 3
  -- myobj:show(3)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 4
  -- myobj:show(4)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 5
  -- myobj:show(5)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1) 
  luaunit.assertEquals(myobj:next_round(), false) -- Round 6
  -- myobj:show(6)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:count_occupied(), 37)  

end

function test_text_part2()
  -- Test the Conway object creation from text

  -- 1. Create Conway object from text
  local myobj = conway:Conway({part2=true, text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 10)
  luaunit.assertEquals(#myobj.seats, 10)
  luaunit.assertEquals(#myobj.seats[1], 10)
  
  -- 3. Test methods
  -- myobj:show(0)
  luaunit.assertEquals(myobj:count_occupied(), 0)
  luaunit.assertEquals(myobj:seat(1, 1), 'L')
  luaunit.assertEquals(myobj:neighbors(1, 1), 0)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 1
  -- myobj:show(1)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 3)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 2
  -- myobj:show(2)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:count_occupied(), 7)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 3
  -- myobj:show(3)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 4
  -- myobj:show(4)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:count_occupied(), 18)
  luaunit.assertEquals(myobj:next_round(), true) -- Round 5
  -- myobj:show(5)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1) 
  luaunit.assertEquals(myobj:next_round(), true) -- Round 6
  -- myobj:show(6)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:count_occupied(), 26)  
  luaunit.assertEquals(myobj:next_round(), false) -- Round 7
  -- myobj:show(7)
  luaunit.assertEquals(myobj:seat(1, 1), '#')
  luaunit.assertEquals(myobj:neighbors(1, 1), 1)
  luaunit.assertEquals(myobj:count_occupied(), 26)  

end
function test_part_one()
  -- Test part one example of Conway object

  -- 1. Create Conway object from text
  local myobj = conway:Conway({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Conway object

  -- 1. Create Conway object from text
  local myobj = conway:Conway({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                  t e s t _ c o n w a y . l u a                 end
-- ======================================================================
