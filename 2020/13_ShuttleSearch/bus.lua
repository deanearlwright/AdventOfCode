-- ======================================================================
-- Shuttle Search
--   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                           b u s . l u a
-- ======================================================================
-- Bus for the Advent of Code 2020 Day 13 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Bus = { part2=false, bid=0, offset=0 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                    Bus
-- ======================================================================


function Bus:Bus (o)
  -- Object for Shuttle Search


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.bid = o.bid or 0
  o.offset = o.offset or 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  return o
end

function Bus:next_departure(time)
  -- Return the next time the bus departs after specified time
  time = time or 0
  
  local delta = time % self.bid
  if delta == 0 then
    return time
  end  
  return time + self.bid - delta
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Bus

-- ======================================================================
-- end                          b u s . l u a                         end
-- ======================================================================
