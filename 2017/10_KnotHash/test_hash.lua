-- ======================================================================
-- Knot Hash
--   Advent of Code 2017 Day 10 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ h a s h . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 10, Knot Hash

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local hash = require('hash')

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
--                                                               dict_len
-- ----------------------------------------------------------------------
function dict_len(d)
    local result = 0
    for _ in pairs(d) do 
      result = result + 1
    end
    return result
end

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = [[
3, 4, 1, 5
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = ""

local PART_ONE_RESULT = nil
local PART_TWO_RESULT = nil

-- ======================================================================
--                                                               TestHash
-- ======================================================================

function test_empty_init()
  -- Test the default Hash creation

  -- 1. Create default Hash object
  local myobj = hash:Hash()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.length, 256)
  luaunit.assertEquals(myobj.current, 0)
  luaunit.assertEquals(myobj.skip, 0)
  luaunit.assertEquals(#myobj.numbers, 256)
  luaunit.assertEquals(#myobj.lengths, 0)

end

function test_text_init()
  -- Test the Hash object creation from text

  -- 1. Create Hash object from text
  local myobj = hash:Hash({text=from_text(EXAMPLE_TEXT), length=5})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 1)
  luaunit.assertEquals(myobj.length, 5)
  luaunit.assertEquals(myobj.current, 0)
  luaunit.assertEquals(myobj.skip, 0)
  luaunit.assertEquals(#myobj.numbers, 5)
  luaunit.assertEquals(#myobj.lengths, 4)

end

function test_part_one()
  -- Test part one example of Hash object

  -- 1. Create Hash object from text
  local myobj = hash:Hash({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Hash object

  -- 1. Create Hash object from text
  local myobj = hash:Hash({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                    t e s t _ h a s h . l u a                   end
-- ======================================================================
