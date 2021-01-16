-- ======================================================================
-- Rain Risk
--   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ f e r r y . l u a
-- ======================================================================
-- Test Ferry for Advent of Code 2020 day 12, Rain Risk

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local ferry = require('ferry')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                              TestFerry
-- ======================================================================

function test_part_one()
  -- Test the Ferry for part one

  -- 1. Create default Ferry object
  local myobj = ferry:Ferry()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.start, {0, 0})
  luaunit.assertEquals(myobj.loc, {0, 0})
  luaunit.assertEquals(myobj.facing, 1)
  
  -- 3. Test methods
  myobj:execute('F10')
  luaunit.assertEquals(myobj.loc, {10, 0})
  luaunit.assertEquals(myobj.facing, 1)
  myobj:execute('N3')
  luaunit.assertEquals(myobj.loc, {10, -3})
  luaunit.assertEquals(myobj.facing, 1)
  myobj:execute('F7')
  luaunit.assertEquals(myobj.loc, {17, -3})
  luaunit.assertEquals(myobj.facing, 1)
  myobj:execute('R90')
  luaunit.assertEquals(myobj.loc, {17, -3})
  luaunit.assertEquals(myobj.facing, 2)
  myobj:execute('F11')
  luaunit.assertEquals(myobj.loc, {17, 8})
  luaunit.assertEquals(myobj.facing, 2)
  luaunit.assertEquals(myobj:manhattan_distance(), 25)
end

function test_part_two()
  -- Test the Ferry for part two

  -- 1. Create default Ferry object
  local myobj = ferry:Ferry({part2=true})

  -- 2. Make sure it has the default true
  luaunit.assertEquals(myobj.part2, true)
  luaunit.assertEquals(myobj.start, {0, 0})
  luaunit.assertEquals(myobj.loc, {0, 0})
  luaunit.assertEquals(myobj.facing, 1)
  luaunit.assertEquals(myobj.waypoint, {10, -1})
  
  -- 3. Test methods
  myobj:execute('F10')
  luaunit.assertEquals(myobj.loc, {100, -10})
  luaunit.assertEquals(myobj.facing, 1)
  luaunit.assertEquals(myobj.waypoint, {10, -1})
  myobj:execute('N3')
  luaunit.assertEquals(myobj.loc, {100, -10})
  luaunit.assertEquals(myobj.facing, 1)
  luaunit.assertEquals(myobj.waypoint, {10, -4})
  myobj:execute('F7')
  luaunit.assertEquals(myobj.loc, {170, -38})
  luaunit.assertEquals(myobj.facing, 1)
  luaunit.assertEquals(myobj.waypoint, {10, -4})
  myobj:execute('R90')
  luaunit.assertEquals(myobj.loc, {170, -38})
  luaunit.assertEquals(myobj.facing, 1)
  luaunit.assertEquals(myobj.waypoint, {4, 10})
  myobj:execute('F11')
  luaunit.assertEquals(myobj.loc, {214, 72})
  luaunit.assertEquals(myobj.facing, 1)
  luaunit.assertEquals(myobj.waypoint, {4, 10})
  luaunit.assertEquals(myobj:manhattan_distance(), 286)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                    t e s t _ f e r r y . p y                   end
-- ======================================================================
