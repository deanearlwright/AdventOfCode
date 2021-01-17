-- ======================================================================
-- Shuttle Search
--   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                       t e s t _ b u s . l u a
-- ======================================================================
-- Test Bus for Advent of Code 2020 day 13, Shuttle Search

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local bus = require('bus')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                TestBus
-- ======================================================================

function test_empty_init()
  -- Test the default Bus creation

  -- 1. Create default Bus object
  local myobj = bus:Bus()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.bid, 0)
  luaunit.assertEquals(myobj.offset, 0)

end

function test_text_init()
  -- Test the Bus object creation from text

  -- 1. Create Buses object from text
  local myobj = bus:Bus({bid=13, offset=1})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.bid, 13)
  luaunit.assertEquals(myobj.offset, 1)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:next_departure(929), 936)
  luaunit.assertEquals(myobj:next_departure(939), 949)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                      t e s t _ b u s . p y                     end
-- ======================================================================
