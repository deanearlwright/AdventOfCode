-- ======================================================================
-- Custom Customs
--   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ g r o u p s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 06, Custom Customs

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local groups = require('groups')

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- Break the text into trimed, non-comment lines

  -- 1. We start with no lines
  local SAVE_BLANK_LINES = true
  local result = {}

  -- 2. Set up to save blank lines (if desired)
  text = text:gsub('[\r]', '')
  if SAVE_BLANK_LINES then
    text = text:gsub('\n\n', '\n \n')
  end

  -- 3. Loop for lines in the text
  for line in text:gmatch('[^\n]+') do
    line = line:gsub("%s*$", "")

    -- 4. Ignore comment lines
    if #line > 0 and "!" == line:sub(1, 1) then
      -- Ignore
    else -- not a comment line
      if #line > 0 or SAVE_BLANK_LINES then
        table.insert(result, line)
      end
    end
  end

  -- 5. Return a table of cleaned text lines
  return result
end

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local SAVE_BLANK_LINES = true

local EXAMPLE_TEXT = [[
abc

a
b
c

ab
ac

a
a
a
a

b
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 11
local PART_TWO_RESULT = 6

-- ======================================================================
--                                                              TestGroups
-- ======================================================================


function test_empty_init()
  -- Test the default Groups creation

  -- 1. Create default Groups object
  local myobj = groups:Groups()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.groups, 0)

end

function test_text_init()
  -- Test the Groups object creation from text

  -- 1. Create Groups object from text
  local myobj = groups:Groups({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 15)
  luaunit.assertEquals(#myobj.groups, 5)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:total_yes(), 11)

end

function test_part_one()
  -- Test part one example of Groups object

  -- 1. Create Groups object from text
  local myobj = groups:Groups({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Groups object

  -- 1. Create Groups object from text
  local myobj = groups:Groups({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ g r o u p s . l u a                end
-- ======================================================================
