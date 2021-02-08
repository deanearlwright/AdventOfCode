-- ======================================================================
-- Crab Combat
--   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ g a m e . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 22, Crab Combat

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local game = require('game')

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
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 306
local PART_TWO_RESULT = 291

local ELPMAXE_TEXT = [[
Player 1:
5
8
4
7
10

Player 2:
9
2
6
3
1
]]

local INFINITE_TEXT = [[
Player 1:
43
19

Player 2:
2
29
14
]]
-- ======================================================================
--                                                              TestGame
-- ======================================================================


function test_empty_init()
  -- Test the default Game creation

  -- 1. Create default Game object
  local myobj = game:Game()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.players, 0)

end

function test_text_init()
  -- Test the Game object creation from text

  -- 1. Create Game object from text
  local myobj = game:Game({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 12)
  luaunit.assertEquals(#myobj.players, 2)
  luaunit.assertEquals(myobj.players[1]:score(), 45 + 8 + 18 + 6 + 1)
  luaunit.assertEquals(myobj.players[2]:score(), 25 + 32 + 12 + 14 + 10)
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 9, 2, 6, 3, 1')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 5, 8, 4, 7, 10')
  myobj:one_round() -- 1
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 2, 6, 3, 1, 9, 5')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 8, 4, 7, 10')
  myobj:one_round() -- 2
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 6, 3, 1, 9, 5')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 4, 7, 10, 8, 2')
  myobj:one_round() -- 3
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 3, 1, 9, 5, 6, 4')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 7, 10, 8, 2')
end

function test_text_init_two()
  -- Test the Game object creation from text for part2

  -- 1. Create Game object from text
  local myobj = game:Game({part2=true, text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 12)
  luaunit.assertEquals(#myobj.players, 2)
  luaunit.assertEquals(myobj.players[1]:score(), 45 + 8 + 18 + 6 + 1)
  luaunit.assertEquals(myobj.players[2]:score(), 25 + 32 + 12 + 14 + 10)
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 9, 2, 6, 3, 1')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 5, 8, 4, 7, 10')
  myobj:one_round_recursive() -- 1
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 2, 6, 3, 1, 9, 5')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 8, 4, 7, 10')
  myobj:one_round_recursive() -- 2
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 6, 3, 1, 9, 5')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 4, 7, 10, 8, 2')
  myobj:one_round_recursive() -- 3
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 3, 1, 9, 5, 6, 4')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 7, 10, 8, 2')
  myobj:one_round_recursive() -- 4
  myobj:one_round_recursive() -- 5
  myobj:one_round_recursive() -- 6
  myobj:one_round_recursive() -- 7
  myobj:one_round_recursive() -- 8
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 4, 9, 8, 5, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 3, 10, 1, 7, 6')
  myobj:one_round_recursive() -- 9 -- Going recursive
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 9, 8, 5, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 10, 1, 7, 6, 3, 4')
  myobj:one_round_recursive() -- 10
  myobj:one_round_recursive() -- 11
  myobj:one_round_recursive() -- 12
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 2, 8, 1')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 6, 3, 4, 10, 9, 7, 5')
  myobj:one_round_recursive() -- 13
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 8, 1')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 3, 4, 10, 9, 7, 5, 6, 2')
  myobj:one_round_recursive() -- 14
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 1, 8, 3')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 4, 10, 9, 7, 5, 6, 2')
  myobj:one_round_recursive() -- 15
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 8, 3')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 10, 9, 7, 5, 6, 2, 4, 1')
  myobj:one_round_recursive() -- 16
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 3')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 9, 7, 5, 6, 2, 4, 1, 10, 8')
  myobj:one_round_recursive() -- 17
  luaunit.assertEquals(myobj:winner(), 2)
  luaunit.assertEquals(myobj.players[2]:score(), 291)
end

function test_text_init_two_reversed()
  -- Test the Game object creation from text for part2

  -- 1. Create Game object from text
  local myobj = game:Game({part2=true, text=from_text(ELPMAXE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 12)
  luaunit.assertEquals(#myobj.players, 2)
  luaunit.assertEquals(myobj.players[1]:score(), 25 + 32 + 12 + 14 + 10)
  luaunit.assertEquals(myobj.players[2]:score(), 45 + 8 + 18 + 6 + 1)
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 5, 8, 4, 7, 10')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 9, 2, 6, 3, 1')
  myobj:one_round_recursive() -- 1
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 8, 4, 7, 10')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 2, 6, 3, 1, 9, 5')
  myobj:one_round_recursive() -- 2
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 4, 7, 10, 8, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 6, 3, 1, 9, 5')
  myobj:one_round_recursive() -- 3
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 7, 10, 8, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 3, 1, 9, 5, 6, 4')
  myobj:one_round_recursive() -- 4
  myobj:one_round_recursive() -- 5
  myobj:one_round_recursive() -- 6
  myobj:one_round_recursive() -- 7
  myobj:one_round_recursive() -- 8
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 3, 10, 1, 7, 6')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 4, 9, 8, 5, 2')
  myobj:one_round_recursive() -- 9 -- Going recursive
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 10, 1, 7, 6, 3, 4')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 9, 8, 5, 2')
  myobj:one_round_recursive() -- 10
  myobj:one_round_recursive() -- 11
  myobj:one_round_recursive() -- 12
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 6, 3, 4, 10, 9, 7, 5')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 2, 8, 1')
  myobj:one_round_recursive() -- 13
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 3, 4, 10, 9, 7, 5, 6, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 8, 1')
  myobj:one_round_recursive() -- 14
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 4, 10, 9, 7, 5, 6, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 1, 8, 3')
  myobj:one_round_recursive() -- 15
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 10, 9, 7, 5, 6, 2, 4, 1')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 8, 3')
  myobj:one_round_recursive() -- 16
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 9, 7, 5, 6, 2, 4, 1, 10, 8')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 3')
  myobj:one_round_recursive() -- 17
  luaunit.assertEquals(myobj:winner(), 1)
  luaunit.assertEquals(myobj.players[1]:score(), 291)
end

function test_text_init_two_infinite()
  -- Test the Game object infinite from text for part2

  -- 1. Create Game object from text
  local myobj = game:Game({part2=true, text=from_text(INFINITE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(#myobj.text, 7)
  luaunit.assertEquals(#myobj.players, 2)
  luaunit.assertEquals(tostring(myobj.players[1]), "1: 43, 19")
  luaunit.assertEquals(tostring(myobj.players[2]), "2: 2, 29, 14")
  
  -- 3. Test methods
  myobj:one_round_recursive() -- 1
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 19, 43, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 29, 14')
  myobj:one_round_recursive() -- 2
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 43, 2')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 14, 29, 19')
  myobj:one_round_recursive() -- 3
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 2, 43, 14')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 29, 19')
  myobj:one_round_recursive() -- 4
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 43, 14')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 19, 29, 2')
  myobj:one_round_recursive() -- 5
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 14, 43, 19')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 29, 2')
  myobj:one_round_recursive() -- 6
  luaunit.assertEquals(myobj:winner(), 0)
  luaunit.assertEquals(tostring(myobj.players[1]), '1: 43, 19')
  luaunit.assertEquals(tostring(myobj.players[2]), '2: 2, 29, 14')
  myobj:one_round_recursive() -- 7
  luaunit.assertEquals(myobj:winner(), 1)
  
end

function test_part_one()
  -- Test part one example of Game object

  -- 1. Create Game object from text
  local myobj = game:Game({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Game object

  -- 1. Create Game object from text
  local myobj = game:Game({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ g a m e . l u a                end
-- ======================================================================
