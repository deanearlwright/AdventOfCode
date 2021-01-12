-- ======================================================================
-- Encoding Error
--   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ c y p h e r . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 09, Encoding Error

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local cypher = require('cypher')

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
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = ""

local PART_ONE_RESULT = 127
local PART_TWO_RESULT = nil

-- ======================================================================
--                                                             TestCypher
-- ======================================================================


function test_empty_init()
  -- Test the default Cypher creation

  -- 1. Create default Cypher object
  local myobj = cypher:Cypher()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.numbers, 0)
  luaunit.assertEquals(myobj.preamble, 25)

end

function test_text_init()
  -- Test the Cypher object creation from text

  -- 1. Create Cypher object from text
  local myobj = cypher:Cypher({preamble = 5, text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 20)
  luaunit.assertEquals(#myobj.numbers, 20)
  luaunit.assertEquals(myobj.preamble, 5)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:rule_breaker(), 127)
  luaunit.assertEquals(myobj:weakness(), 62)
  

end

function test_part_one()
  -- Test part one example of Cypher object

  -- 1. Create Cypher object from text
  local myobj = cypher:Cypher({preamble=5, text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Cypher object

  -- 1. Create Cypher object from text
  local myobj = cypher:Cypher({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                  t e s t _ c y p h e r . l u a                 end
-- ======================================================================
