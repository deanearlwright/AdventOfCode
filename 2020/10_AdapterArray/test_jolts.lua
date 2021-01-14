-- ======================================================================
-- Adapter Array
--   Advent of Code 2020 Day 10 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ j o l t s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 10, Adapter Array

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local jolts = require('jolts')

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
local EXAMPLE_ONE_TEXT = [[
16
10
15
5
1
11
7
19
6
12
4
]]
local EXAMPLE_TWO_TEXT = [[
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
]]
local PART_ONE_TEXT = EXAMPLE_TWO_TEXT
local PART_TWO_TEXT = EXAMPLE_TWO_TEXT

local PART_ONE_RESULT = 220
local PART_TWO_RESULT = 19208

-- ======================================================================
--                                                              TestJolts
-- ======================================================================


function test_empty_init()
  -- Test the default Jolts creation

  -- 1. Create default Jolts object
  local myobj = jolts:Jolts()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.numbers, 0)
  luaunit.assertEquals(myobj.device, 0)

end

function test_text_init()
  -- Test the Jolts object creation from text

  -- 1. Create Jolts object from text
  local myobj = jolts:Jolts({text=from_text(EXAMPLE_ONE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(#myobj.numbers, 11)
  luaunit.assertEquals(myobj.device, 22)

  -- 3. Check methods
  local one, three = myobj:count_diff()
  luaunit.assertEquals(one, 7)
  luaunit.assertEquals(three, 5)
  luaunit.assertEquals(myobj:count_arrangements(), 8)
  
  
end

function test_text_two()
  -- Test the Jolts object creation from text

  -- 1. Create Jolts object from text
  local myobj = jolts:Jolts({text=from_text(EXAMPLE_TWO_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 31)
  luaunit.assertEquals(#myobj.numbers, 31)
  luaunit.assertEquals(myobj.device, 52)

  -- 3. Check methods
  local one, three = myobj:count_diff()
  luaunit.assertEquals(one, 22)
  luaunit.assertEquals(three, 10)
  
end

function test_part_one()
  -- Test part one example of Jolts object

  -- 1. Create Jolts object from text
  local myobj = jolts:Jolts({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Jolts object

  -- 1. Create Jolts object from text
  local myobj = jolts:Jolts({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ j o l t s . l u a                  end
-- ======================================================================
