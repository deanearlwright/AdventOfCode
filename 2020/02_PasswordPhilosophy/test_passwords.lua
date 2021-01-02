-- ======================================================================
-- Password Philosophy
--   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p a s s w o r d s . l u a
-- ======================================================================
-- "Test solver for Advent of Code 2020 day 02, Password Philosophy"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
luaunit = require('luaunit')

passwords = require('passwords')

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- "Break the text into trimed, non-comment lines"

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
EXAMPLE_TEXT = [[
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
]]
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 2
PART_TWO_RESULT = 1

-- ======================================================================
--                                                          TestPasswords
-- ======================================================================


function test_empty_init()
  -- "Test the default Passwords creation"

  -- 1. Create default Passwords object
  local myobj = passwords:Passwords()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.policies, 0)

end

function test_text_init()
  -- "Test the Passwords object creation from text"

  -- 1. Create Passwords object from text
  local myobj = passwords:Passwords({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 3)
  luaunit.assertEquals(#myobj.policies, 3)

end

function test_part_one()
  -- "Test part one example of Passwords object"

  -- 1. Create Passwords object from text
  local myobj = passwords:Passwords({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- "Test part two example of Passwords object"

  -- 1. Create Passwords object from text
  local myobj = passwords:Passwords({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end               t e s t _ p a s s w o r d s . l u a              end
-- ======================================================================
