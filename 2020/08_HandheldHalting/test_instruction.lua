-- ======================================================================
-- Handheld Halting
--   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ i n s t r u c t i o n . l u a
-- ======================================================================
-- Test Instruction for Advent of Code 2020 day 08, Handheld Halting

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local instruction = require('instruction')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "jmp +4"

-- ======================================================================
--                                                        TestInstruction
-- ======================================================================

function test_empty_init()
  -- Test the default Instruction creation

  -- 1. Create default Instruction object
  local myobj = instruction:Instruction()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.operation, 0)
  luaunit.assertEquals(myobj.argument, 0)
  luaunit.assertEquals(myobj.visited, false)

end

function test_text_init()
  -- Test the Instruction object creation from text

  -- 1. Create Console object from text
  local myobj = instruction:Instruction({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT)
  luaunit.assertEquals(myobj.operation, "jmp")
  luaunit.assertEquals(myobj.argument, 4)
  luaunit.assertEquals(myobj.visited, false)
  
  -- 3. Check methods
  acc, pc = myobj:execute(1)
  luaunit.assertEquals(acc, 1)
  luaunit.assertEquals(pc, 4)
  luaunit.assertEquals(myobj.visited, true)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end              t e s t _ i n s t r u c t i o n . p y             end
-- ======================================================================
