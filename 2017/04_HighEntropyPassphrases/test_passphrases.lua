-- ======================================================================
-- HighEntropyPassphrases
--   Advent of Code 2017 Day 04 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p a s s p h r a s e s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 04, HighEntropyPassphrases

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local passphrases = require('passphrases')

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
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
abc bb cc dd cab
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 3
local PART_TWO_RESULT = 2

-- ======================================================================
--                                                        TestPassphrases
-- ======================================================================

function test_empty_init()
  -- Test the default Passphrases creation

  -- 1. Create default Passphrases object
  local myobj = passphrases:Passphrases()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.words, 0)

end

function test_text_init()
  -- Test the Passphrases object creation from text

  -- 1. Create Passphrases object from text
  local myobj = passphrases:Passphrases({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 4)
  luaunit.assertEquals(#myobj.words, 0)

end

function test_part_one()
  -- Test part one example of Passphrases object

  -- 1. Create Passphrases object from text
  local myobj = passphrases:Passphrases({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Passphrases object

  -- 1. Create Passphrases object from text
  local myobj = passphrases:Passphrases({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end             t e s t _ p a s s p h r a s e s . l u a            end
-- ======================================================================
