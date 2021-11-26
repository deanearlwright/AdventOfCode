-- ======================================================================
-- Recursive Circus
--   Advent of Code 2017 Day 07 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ t o w e r . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 07, Recursive Circus

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local tower = require('tower')

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
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
]]

local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = "tknk"
local PART_TWO_RESULT = 60

-- ======================================================================
--                                                              TestTower
-- ======================================================================

function dict_len(d)
    local result = 0
    for _ in pairs(d) do 
      result = result + 1
    end
    return result
end

function test_empty_init()
  -- Test the default Tower creation

  -- 1. Create default Tower object
  local myobj = tower:Tower()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(dict_len(myobj.weights), 0)
  luaunit.assertEquals(dict_len(myobj.supporting), 0)
  luaunit.assertEquals(dict_len(myobj.supported), 0)
  luaunit.assertEquals(dict_len(myobj.heights), 0)
  luaunit.assertEquals(dict_len(myobj.combined), 0)
end

function test_text_init()
  -- Test the Tower object creation from text

  -- 1. Create Tower object from text
  local myobj = tower:Tower({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 13)
  luaunit.assertEquals(dict_len(myobj.weights), 13)
  luaunit.assertEquals(dict_len(myobj.supporting), 4)
  luaunit.assertEquals(dict_len(myobj.supported), 12)
  luaunit.assertEquals(dict_len(myobj.heights), 0)
  luaunit.assertEquals(dict_len(myobj.combined), 0)
  luaunit.assertEquals(myobj.weights["tknk"], 41)
  luaunit.assertEquals(myobj.weights["ugml"], 68)
  luaunit.assertEquals(myobj.weights["xhth"], 57)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:bottom(), "tknk")
  
  myobj:set_all_heights()
  luaunit.assertEquals(dict_len(myobj.heights), 13)
  luaunit.assertEquals(myobj.heights["tknk"], 1)
  luaunit.assertEquals(myobj.heights["ugml"], 2)
  luaunit.assertEquals(myobj.heights["xhth"], 3)
  
  myobj:set_all_combined()
  luaunit.assertEquals(dict_len(myobj.combined), 13)
  luaunit.assertEquals(myobj.combined["tknk"], 41+251+243+243)
  luaunit.assertEquals(myobj.combined["ugml"], 251)
  luaunit.assertEquals(myobj.combined["xhth"], 57)
  
  myobj:find_unbalanced()
  luaunit.assertEquals(dict_len(myobj.unbalanced), 1)
  luaunit.assertEquals(myobj.unbalanced["tknk"], 1)
  luaunit.assertEquals(myobj:highest_unbalanced(), "tknk")
  
  luaunit.assertEquals(myobj:balance("tknk"), 60)
  
end

function test_part_one()
  -- Test part one example of Tower object

  -- 1. Create Tower object from text
  local myobj = tower:Tower({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Tower object

  -- 1. Create Tower object from text
  local myobj = tower:Tower({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ t o w e r . l u a                  end
-- ======================================================================
