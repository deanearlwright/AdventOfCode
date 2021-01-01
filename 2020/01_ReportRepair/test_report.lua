-- ======================================================================
-- Report Repair
--   Advent of Code 2020 Day 01 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ r e p o r t . l u a
-- ======================================================================
-- "Test solver for Advent of Code 2020 day 01, Report Repair"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
luaunit = require('luaunit')

report = require('report')

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
1721
979
366
299
675
1456
]]
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 514579
PART_TWO_RESULT = 241861950

-- ======================================================================
--                                                             TestReport
-- ======================================================================


function test_empty_init()
  -- "Test the default Report creation"

  -- 1. Create default Report object
  local myobj = report:Report()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, {})
  luaunit.assertEquals(myobj.numbers, {})

end

function test_text_init()
  -- "Test the Report object creation from text"

  -- 1. Create Report object from text
  local myobj = report:Report({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 6)
  luaunit.assertEquals(#myobj.numbers, 6)

end

function test_part_one()
  -- "Test part one example of Report object"

  -- 1. Create Report object from text
  local myobj = report:Report({text=from_text(PART_ONE_TEXT)})
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 6)
  luaunit.assertEquals(#myobj.numbers, 6)

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- "Test part two example of Report object"

  -- 1. Create Report object from text
  local myobj = report:Report({part2=true, text=from_text(PART_TWO_TEXT)})
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 6)
  luaunit.assertEquals(#myobj.numbers, 6)

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ r e p o r t . l u a                  end
-- ======================================================================
