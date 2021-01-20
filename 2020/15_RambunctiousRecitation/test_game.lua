-- ======================================================================
-- Rambunctious Recitation
--   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ g a m e . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 15, Rambunctious Recitation

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
0,3,6
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 436
local PART_TWO_RESULT = 175594

local EXAMPLES = {
    {text = '1,3,2', spoken = 1},
    {text = '2,1,3', spoken = 10},
    {text = '1,2,3', spoken = 27},
    {text = '2,3,1', spoken = 78},
    {text = '3,2,1', spoken = 438},
    {text = '3,1,2', spoken = 1836},
}
-- ======================================================================
--                                                               TestGame
-- ======================================================================


function test_empty_init()
  -- Test the default Game creation

  -- 1. Create default Game object
  local myobj = game:Game()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.memory.age, nil)
  luaunit.assertEquals(myobj.memory.turn, 0)

end

function test_text_init()
  -- Test the Game object creation from text

  -- 1. Create Game object from text
  local myobj = game:Game({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 1)
  luaunit.assertEquals(myobj.memory.age, 0)
  luaunit.assertEquals(myobj.memory.turn, 3)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:number_spoken(9), 4)
  

end

function test_examples()
  -- Test the several part one examples
  
  -- 1. Loop for the part one examples
  for _, example in ipairs(EXAMPLES) do
    
    -- 2. Create the Game object from text
    local myobj = game:Game({text=from_text("\n" .. example.text)})
  
    -- 3. Check the part one result
    luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), example.spoken)
  end
end


function test_part_one()
  -- Test part one example of Game object

  -- 1. Create Game object from text
  local myobj = game:Game({text=from_text(PART_ONE_TEXT)})
  luaunit.assertEquals(myobj.memory.age, 0)
  luaunit.assertEquals(myobj.memory.turn, 3)

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
-- end                    t e s t _ g a m e . l u a                   end
-- ======================================================================
