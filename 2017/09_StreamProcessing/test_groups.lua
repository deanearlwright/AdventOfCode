-- ======================================================================
-- StreamProcessing
--   Advent of Code 2017 Day 09 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ g r o u p s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 09, StreamProcessing

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require("luaunit")

local groups = require("groups")

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- Break the text into trimed, non-comment lines

  -- 1. We start with no lines
  local result = {}

  -- 2. Loop for lines in the text
  for line in text:gmatch("[^\r\n]+") do

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
{{<a!>},{<a!>},{<a!>},{<ab>}}
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 3
local PART_TWO_RESULT = 17

-- ======================================================================
--                                                             TestGroups
-- ======================================================================

function test_empty_init()
  -- Test the default Groups creation

  -- 1. Create default Groups object
  local myobj = groups:Groups()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)

end

function test_text_init()
  -- Test the Groups object creation from text

  -- 1. Create Groups object from text
  local myobj = groups:Groups({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 1)

  -- 3. Check methods
  luaunit.assertEquals(myobj:next_state(1, "{"), 7)
  luaunit.assertEquals(myobj:next_state(1, "<"), 9)
  luaunit.assertEquals(myobj:next_state(1, ">"), 9)
  luaunit.assertEquals(myobj:next_state(1, "}"), 9)
  luaunit.assertEquals(myobj:next_state(1, ","), 9)
  luaunit.assertEquals(myobj:next_state(1, "!"), 9)
  luaunit.assertEquals(myobj:next_state(1, "a"), 9)
  luaunit.assertEquals(myobj:next_state(2, "{"), 7)
  luaunit.assertEquals(myobj:next_state(2, "<"), 3)
  luaunit.assertEquals(myobj:next_state(2, ">"), 9)
  luaunit.assertEquals(myobj:next_state(2, "}"), 8)
  luaunit.assertEquals(myobj:next_state(2, ","), 2)
  luaunit.assertEquals(myobj:next_state(2, "!"), 9)
  luaunit.assertEquals(myobj:next_state(2, "a"), 9)
  luaunit.assertEquals(myobj:next_state(3, "{"), 6)
  luaunit.assertEquals(myobj:next_state(3, "<"), 6)
  luaunit.assertEquals(myobj:next_state(3, ">"), 2)
  luaunit.assertEquals(myobj:next_state(3, "}"), 6)
  luaunit.assertEquals(myobj:next_state(3, ","), 6)
  luaunit.assertEquals(myobj:next_state(3, "!"), 4)
  luaunit.assertEquals(myobj:next_state(3, "a"), 6)
  luaunit.assertEquals(myobj:next_state(4, "{"), 3)
  luaunit.assertEquals(myobj:next_state(4, "<"), 3)
  luaunit.assertEquals(myobj:next_state(4, ">"), 3)
  luaunit.assertEquals(myobj:next_state(4, "}"), 3)
  luaunit.assertEquals(myobj:next_state(4, ","), 3)
  luaunit.assertEquals(myobj:next_state(4, "!"), 3)
  luaunit.assertEquals(myobj:next_state(4, "a"), 3)
  
  luaunit.assertEquals(myobj:score_braces("{}"), 1)
  luaunit.assertEquals(myobj:score_braces("{{{}}}"), 6)
  luaunit.assertEquals(myobj:score_braces("{{},{}}"), 5)
  luaunit.assertEquals(myobj:score_braces("{{{},{},{{}}}}"), 16)
  luaunit.assertEquals(myobj:score_braces("{<a>,<a>,<a>,<a>}"), 1)
  luaunit.assertEquals(myobj:score_braces("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
  luaunit.assertEquals(myobj:score_braces("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
  luaunit.assertEquals(myobj:score_braces("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)
  
  luaunit.assertEquals(myobj:score_garbage("{}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{{{}}}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{{},{}}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{{{},{},{{}}}}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{<a>,<a>,<a>,<a>}"), 4)
  luaunit.assertEquals(myobj:score_garbage("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 8)
  luaunit.assertEquals(myobj:score_garbage("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 17)
  
  luaunit.assertEquals(myobj:score_garbage("{<>}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{<random characters>}"), 17)
  luaunit.assertEquals(myobj:score_garbage("{<<<<>}"), 3)
  luaunit.assertEquals(myobj:score_garbage("{<{!>}>}"), 2)
  luaunit.assertEquals(myobj:score_garbage("{<!!>}"), 0)
  luaunit.assertEquals(myobj:score_garbage("{<!!!>>}"), 0)
  luaunit.assertEquals(myobj:score_garbage('{<{o"i!a,<{i<a>}'), 10)

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
-- end                  t e s t _ g r o u p s . l u a                 end
-- ======================================================================
