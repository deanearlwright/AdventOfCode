-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ t i c k e t . l u a
-- ======================================================================
-- Test Ticket for Advent of Code 2020 day 16, Ticket Translation

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local ticket = require('ticket')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "7,1,14"

-- ======================================================================
--                                                             TestTicket
-- ======================================================================

function test_empty_init()
  -- Test the default Ticket creation

  -- 1. Create default Ticket object
  local myobj = ticket:Ticket()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.numbers, 0)
  luaunit.assertEquals(myobj.valid, true)

end

function test_text_init()
  -- Test the Ticket object creation from text

  -- 1. Create Tickets object from text
  local myobj = ticket:Ticket({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 6)
  luaunit.assertEquals(#myobj.numbers, 3)
  luaunit.assertEquals(myobj.numbers[1], 7)
  luaunit.assertEquals(myobj.numbers[2], 1)
  luaunit.assertEquals(myobj.numbers[3], 14)
  luaunit.assertEquals(myobj.valid, true)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ t i c k e t . p y                  end
-- ======================================================================
