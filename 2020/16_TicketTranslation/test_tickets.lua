-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ t i c k e t s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 16, Ticket Translation

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local tickets = require('tickets')

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
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
]]

local EXAMPLE_TWO = [[
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
]]

local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TWO

local PART_ONE_RESULT = 71
local PART_TWO_RESULT = 1

-- ======================================================================
--                                                            TestTickets
-- ======================================================================


function test_empty_init()
  -- Test the default Tickets creation

  -- 1. Create default Tickets object
  local myobj = tickets:Tickets()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.rules, nil)
  luaunit.assertEquals(myobj.mine, nil)
  luaunit.assertEquals(#myobj.nearby, 0)

end

function test_text_init()
  -- Test the Tickets object creation from text

  -- 1. Create Tickets object from text
  local myobj = tickets:Tickets({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 10)
  luaunit.assertEquals(#myobj.rules.rules, 3)
  luaunit.assertEquals(myobj.rules.rules[1].name, 'class')
  luaunit.assertEquals(myobj.rules.rules[2].name, 'row')
  luaunit.assertEquals(myobj.rules.rules[3].name, 'seat')
  luaunit.assertNotEquals(myobj.mine, nil)
  luaunit.assertEquals(#myobj.mine.numbers, 3)
  luaunit.assertEquals(myobj.mine.numbers[1], 7)
  luaunit.assertEquals(myobj.mine.numbers[2], 1)
  luaunit.assertEquals(myobj.mine.numbers[3], 14)
  luaunit.assertEquals(#myobj.nearby, 4)
  luaunit.assertEquals(myobj.nearby[1].numbers[1], 7)
  luaunit.assertEquals(myobj.nearby[2].numbers[1], 40)
  luaunit.assertEquals(myobj.nearby[3].numbers[1], 55)
  luaunit.assertEquals(myobj.nearby[4].numbers[1], 38)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:scanning_error_rate(), 71)
  luaunit.assertEquals(myobj.nearby[1].valid, true)
  luaunit.assertEquals(myobj.nearby[2].valid, false)
  luaunit.assertEquals(myobj.nearby[3].valid, false)
  luaunit.assertEquals(myobj.nearby[4].valid, false)
  
end

function test_text_two()
  -- Test the Tickets object creation from the example two text

  -- 1. Create Tickets object from text
  local myobj = tickets:Tickets({part2=true, text=from_text(EXAMPLE_TWO)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 9)
  luaunit.assertEquals(#myobj.rules.rules, 3)
  luaunit.assertEquals(myobj.rules.rules[1].name, 'class')
  luaunit.assertEquals(myobj.rules.rules[2].name, 'row')
  luaunit.assertEquals(myobj.rules.rules[3].name, 'seat')
  luaunit.assertNotEquals(myobj.mine, nil)
  luaunit.assertEquals(#myobj.mine.numbers, 3)
  luaunit.assertEquals(myobj.mine.numbers[1], 11)
  luaunit.assertEquals(myobj.mine.numbers[2], 12)
  luaunit.assertEquals(myobj.mine.numbers[3], 13)
  luaunit.assertEquals(#myobj.nearby, 3)
  luaunit.assertEquals(myobj.nearby[1].numbers[1], 3)
  luaunit.assertEquals(myobj.nearby[2].numbers[1], 15)
  luaunit.assertEquals(myobj.nearby[3].numbers[1], 5)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:scanning_error_rate(), 0)
  luaunit.assertEquals(myobj.nearby[1].valid, true)
  luaunit.assertEquals(myobj.nearby[2].valid, true)
  luaunit.assertEquals(myobj.nearby[3].valid, true)
  
  luaunit.assertEquals(myobj:scanning_error_rate(), 0)
  luaunit.assertEquals(myobj:departure_fields(), 1)
  luaunit.assertEquals(myobj.rules.rules[1].positions[1], 2)
  luaunit.assertEquals(myobj.rules.rules[2].positions[1], 1)
  luaunit.assertEquals(myobj.rules.rules[3].positions[1], 3)
  
  
  
end

function test_part_one()
  -- Test part one example of Tickets object

  -- 1. Create Tickets object from text
  local myobj = tickets:Tickets({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Tickets object

  -- 1. Create Tickets object from text
  local myobj = tickets:Tickets({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ t i c k e t s . l u a                end
-- ======================================================================
