-- ======================================================================
-- Toboggan Trajectory
--   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ t r e e s . l u a
-- ======================================================================
-- "Test solver for Advent of Code 2020 day 03, Toboggan Trajectory"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
luaunit = require('luaunit')

trees = require('trees')

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
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
]]
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7
PART_TWO_RESULT = 336

-- ======================================================================
--                                                              TestTrees
-- ======================================================================


function test_empty_init()
  -- "Test the default Trees creation"

  -- 1. Create default Trees object
  local myobj = trees:Trees()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.rows, 0)
  luaunit.assertEquals(myobj.cols, 0)

end

function test_text_init()
  -- "Test the Trees object creation from text"

  -- 1. Create Trees object from text
  local myobj = trees:Trees({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(myobj.rows, 11)
  luaunit.assertEquals(myobj.cols, 11)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:is_below(1), false)
  luaunit.assertEquals(myobj:is_below(6), false)
  luaunit.assertEquals(myobj:is_below(10), false)
  luaunit.assertEquals(myobj:is_below(11), false)
  luaunit.assertEquals(myobj:is_below(12), true)
  luaunit.assertEquals(myobj:is_below(13), true)

  luaunit.assertEquals(myobj:is_tree(1, 1), false)
  luaunit.assertEquals(myobj:is_tree(4, 2), false)
  luaunit.assertEquals(myobj:is_tree(7, 3), true)
  luaunit.assertEquals(myobj:is_tree(10, 4), false)
  luaunit.assertEquals(myobj:is_tree(13, 5), true)
  luaunit.assertEquals(myobj:is_tree(16, 6), true)
  luaunit.assertEquals(myobj:is_tree(19, 7), false)
  luaunit.assertEquals(myobj:is_tree(22, 8), true)
  luaunit.assertEquals(myobj:is_tree(25, 9), true)
  luaunit.assertEquals(myobj:is_tree(28, 10), true)
  luaunit.assertEquals(myobj:is_tree(31, 11), true)
  luaunit.assertEquals(myobj:is_tree(34, 12), false)
  luaunit.assertEquals(myobj:is_tree(39, 13), false)
  
  luaunit.assertEquals(myobj:count_trees(3, 1), 7)
  luaunit.assertEquals(myobj:count_trees(1, 1), 2)
  luaunit.assertEquals(myobj:count_trees(5, 1), 3)
  luaunit.assertEquals(myobj:count_trees(7, 1), 4)
  luaunit.assertEquals(myobj:count_trees(1, 2), 2)
end

function test_part_one()
  -- "Test part one example of Trees object"

  -- 1. Create Trees object from text
  local myobj = trees:Trees({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- "Test part two example of Trees object"

  -- 1. Create Trees object from text
  local myobj = trees:Trees({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ t r e e s . l u a                end
-- ======================================================================
