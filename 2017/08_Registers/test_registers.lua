-- ======================================================================
-- Registers
--   Advent of Code 2017 Day 08 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                   t e s t _ r e g i s t e r s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2017 day 08, Registers

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local registers = require('registers')

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
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 1
local PART_TWO_RESULT = 10

-- ======================================================================
--                                                          TestRegisters
-- ======================================================================

function dict_len(d)
    local result = 0
    for _ in pairs(d) do 
      result = result + 1
    end
    return result
end

function test_empty_init()
  -- Test the default Registers creation

  -- 1. Create default Registers object
  local myobj = registers:Registers()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(dict_len(myobj.regs), 0)
end

function test_text_init()
  -- Test the Registers object creation from text

  -- 1. Create Registers object from text
  local myobj = registers:Registers({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 4)
  luaunit.assertEquals(dict_len(myobj.regs), 0)

  -- 3. Check methods
  luaunit.assertEquals(myobj:decode_inst(myobj.text[1]), {"b", 5, "a", ">", 1})
  luaunit.assertEquals(myobj:decode_inst(myobj.text[3]), {"c", 10, "a", ">=", 1})
  luaunit.assertEquals(myobj:get_register("a"), 0)
  luaunit.assertEquals(myobj:set_register("a", 42), 0)
  luaunit.assertEquals(myobj:get_register("a"), 42)
  luaunit.assertEquals(myobj:set_register("a", 0), 42)
  
  luaunit.assertEquals(myobj:get_register("a"), 0)
  luaunit.assertEquals(myobj:get_register("b"), 0)
  luaunit.assertEquals(myobj:get_register("c"), 0)
  luaunit.assertEquals(myobj:one_inst(1), false)
  luaunit.assertEquals(myobj:get_register("a"), 0)
  luaunit.assertEquals(myobj:get_register("b"), 0)
  luaunit.assertEquals(myobj:get_register("c"), 0)
  luaunit.assertEquals(myobj:one_inst(2), true)
  luaunit.assertEquals(myobj:get_register("a"), 1)
  luaunit.assertEquals(myobj:get_register("b"), 0)
  luaunit.assertEquals(myobj:get_register("c"), 0)
  luaunit.assertEquals(myobj:one_inst(3), true)
  luaunit.assertEquals(myobj:get_register("a"), 1)
  luaunit.assertEquals(myobj:get_register("b"), 0)
  luaunit.assertEquals(myobj:get_register("c"), 10)
  luaunit.assertEquals(myobj:one_inst(4), true)
  luaunit.assertEquals(myobj:get_register("a"), 1)
  luaunit.assertEquals(myobj:get_register("b"), 0)
  luaunit.assertEquals(myobj:get_register("c"), -10)
  
  luaunit.assertEquals(myobj:largest(), 1)
  
end

function test_part_one()
  -- Test part one example of Registers object

  -- 1. Create Registers object from text
  local myobj = registers:Registers({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Registers object

  -- 1. Create Registers object from text
  local myobj = registers:Registers({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end               t e s t _ r e g i s t e r s . l u a              end
-- ======================================================================
