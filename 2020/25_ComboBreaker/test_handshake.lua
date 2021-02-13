-- ======================================================================
-- Combo Breaker
--   Advent of Code 2020 Day 25 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ h a n d s h a k e . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 25, Combo Breaker

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local handshake = require('handshake')

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
5764801
17807724
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = ""

local PART_ONE_RESULT = 14897079
local PART_TWO_RESULT = nil

-- ======================================================================
--                                                          TestHandshake
-- ======================================================================


function test_empty_init()
  -- Test the default Handshake creation

  -- 1. Create default Handshake object
  local myobj = handshake:Handshake()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.card_public, nil)
  luaunit.assertEquals(myobj.door_public, nil)
  luaunit.assertEquals(myobj.card_private, nil)
  luaunit.assertEquals(myobj.door_private, nil)


end

function test_text_init()
  -- Test the Handshake object creation from text

  -- 1. Create Handshake object from text
  local myobj = handshake:Handshake({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 2)
  luaunit.assertEquals(myobj.card_public, 5764801)
  luaunit.assertEquals(myobj.door_public, 17807724)
  luaunit.assertEquals(myobj.card_private, nil)
  luaunit.assertEquals(myobj.door_private, nil)

  -- 3. Check methods
  luaunit.assertEquals(myobj:transform_number(17807724, 8), 14897079)
  luaunit.assertEquals(myobj:transform_number(5764801, 11), 14897079)

  luaunit.assertEquals(myobj:guess_private(5764801), 8)
  luaunit.assertEquals(myobj:guess_private(17807724), 11)

  luaunit.assertEquals(myobj:guess_encryption_key(), 14897079)

end

function test_part_one()
  -- Test part one example of Handshake object

  -- 1. Create Handshake object from text
  local myobj = handshake:Handshake({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Handshake object

  -- 1. Create Handshake object from text
  local myobj = handshake:Handshake({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end              t e s t _ h a n d s h a k e . l u a               end
-- ======================================================================
