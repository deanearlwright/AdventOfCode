-- ======================================================================
-- Conway Cubes
--   Advent of Code 2020 Day 17 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p o c k e t . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 17, Conway Cubes

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local pocket = require('pocket')

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
.#.
..#
###
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 112
local PART_TWO_RESULT = 848

-- ======================================================================
--                                                             TestPocket
-- ======================================================================


function test_empty_init()
  -- Test the default Pocket creation

  -- 1. Create default Pocket object
  local myobj = pocket:Pocket()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.cycle, 0)
  luaunit.assertEquals(#myobj.active, 0)

end

function test_text_init()
  -- Test the Pocket object creation from text

  -- 1. Create Pocket object from text
  local myobj = pocket:Pocket({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 3)
  luaunit.assertEquals(myobj.cycle, 0)

  -- 3. Check methods
  luaunit.assertEquals(myobj:count_active(), 5)
  luaunit.assertEquals(#myobj:nearby("0,0,0"), 26)
  luaunit.assertEquals(myobj:count_nearby("2,1,0"), 1)
  luaunit.assertEquals(myobj:count_nearby("1,3,0"), 1)
  luaunit.assertEquals(myobj:count_nearby("2,2,0"), 5)
  luaunit.assertEquals(myobj:count_nearby("2,2,1"), 5)
  
  myobj:one_cycle()
  luaunit.assertEquals(myobj:count_active(), 11)
  myobj:one_cycle()
  luaunit.assertEquals(myobj:count_active(), 21)
  myobj:one_cycle()
  luaunit.assertEquals(myobj:count_active(), 38)
  luaunit.assertEquals(myobj:run_until(6), 112)

end

function test_text_part2()
  -- Test the Pocket object creation from text for part2

  -- 1. Create Pocket object from text
  local myobj = pocket:Pocket({part2=true, text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 3)
  luaunit.assertEquals(myobj.cycle, 0)

  -- 3. Check methods
  luaunit.assertEquals(myobj:count_active(), 5)
  luaunit.assertEquals(#myobj:nearby("0,0,0,0"), 80)
  luaunit.assertEquals(myobj:count_nearby("2,1,0,0"), 1)
  luaunit.assertEquals(myobj:count_nearby("1,3,0,0"), 1)
  luaunit.assertEquals(myobj:count_nearby("2,2,0,0"), 5)
  luaunit.assertEquals(myobj:count_nearby("2,2,1,0"), 5)
  
  myobj:one_cycle()
  luaunit.assertEquals(myobj:count_active(), 29)
  myobj:one_cycle()
  luaunit.assertEquals(myobj:count_active(), 60)
  luaunit.assertEquals(myobj:run_until(6), 848)

end

function test_part_one()
  -- Test part one example of Pocket object

  -- 1. Create Pocket object from text
  local myobj = pocket:Pocket({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Pocket object

  -- 1. Create Pocket object from text
  local myobj = pocket:Pocket({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                  t e s t _ p o c k e t . l u a                 end
-- ======================================================================
